#!/usr/bin/env python3
"""Buduje wydanie dla uczestników: paczkę zip pluginu, marketplace.json i version.json.

Użycie:
    python3 scripts/build.py --base-url https://TWOJ-LOGIN.github.io/samodzielny

Wynik trafia do katalogu dist/, który GitHub Actions publikuje na GitHub Pages.
"""
import argparse
import hashlib
import json
import re
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGINS_DIR = ROOT / "plugins"
DIST = ROOT / "dist"
MARKETPLACE_NAME = "samodzielny"
OWNER = {"name": "Blue Mint", "email": "biuro@blue-mint.pl"}
TEXT_SUFFIXES = {".md", ".json", ".txt"}
FIXED_DATE = (2026, 1, 1, 0, 0, 0)  # stała data w zip = ta sama treść daje ten sam sha256


def latest_changes(changelog: Path) -> str:
    if not changelog.exists():
        return ""
    sections = re.split(r"^## ", changelog.read_text(encoding="utf-8"), flags=re.M)
    if len(sections) < 2:
        return ""
    lines = sections[1].strip().splitlines()[1:]
    return " ".join(line.lstrip("- ").strip().replace("**", "") for line in lines if line.strip())


def build_plugin(plugin_dir: Path, base_url: str) -> dict:
    manifest = json.loads((plugin_dir / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    name, version = manifest["name"], manifest["version"]
    zip_path = DIST / "plugins" / f"{name}-{version}.zip"
    zip_path.parent.mkdir(parents=True, exist_ok=True)

    files = sorted(p for p in plugin_dir.rglob("*") if p.is_file() and p.name != ".DS_Store")
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in files:
            data = path.read_bytes()
            if path.suffix in TEXT_SUFFIXES:
                data = data.decode("utf-8").replace("{{BASE_URL}}", base_url).encode("utf-8")
            info = zipfile.ZipInfo(path.relative_to(plugin_dir).as_posix(), FIXED_DATE)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            zf.writestr(info, data)

    sha256 = hashlib.sha256(zip_path.read_bytes()).hexdigest()
    print(f"  {name} {version}  ->  {zip_path.relative_to(ROOT)}  sha256={sha256[:12]}...")
    return {
        "entry": {
            "name": name,
            "description": manifest.get("description", ""),
            "source": {
                "source": "archive",
                "url": f"{base_url}/plugins/{zip_path.name}",
                "sha256": sha256,
            },
        },
        "version": version,
        "changes": latest_changes(plugin_dir / "CHANGELOG.md"),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", required=True, help="Publiczny adres, pod którym będzie katalog dist/")
    args = parser.parse_args()
    base_url = args.base_url.rstrip("/")
    if not base_url.startswith("https://"):
        print("BŁĄD: --base-url musi zaczynać się od https://", file=sys.stderr)
        return 1

    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()

    print(f"Buduję wydanie dla {base_url}")
    built = [build_plugin(p, base_url) for p in sorted(PLUGINS_DIR.iterdir()) if (p / ".claude-plugin" / "plugin.json").exists()]

    marketplace = {
        "name": MARKETPLACE_NAME,
        "description": "Asystent marketingu dla społeczności właścicieli sklepów internetowych.",
        "owner": OWNER,
        "plugins": [b["entry"] for b in built],
    }
    (DIST / "marketplace.json").write_text(json.dumps(marketplace, ensure_ascii=False, indent=2), encoding="utf-8")

    versions = {b["entry"]["name"]: b["version"] for b in built}
    versions["zmiany"] = {b["entry"]["name"]: b["changes"] for b in built}
    (DIST / "version.json").write_text(json.dumps(versions, ensure_ascii=False, indent=2), encoding="utf-8")

    (DIST / ".nojekyll").write_text("")
    index = (ROOT / "docs" / "index.html").read_text(encoding="utf-8").replace("{{BASE_URL}}", base_url)
    (DIST / "index.html").write_text(index, encoding="utf-8")
    print("Gotowe: dist/marketplace.json, dist/version.json, dist/index.html")
    return 0


if __name__ == "__main__":
    sys.exit(main())
