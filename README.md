# samodzielny: asystent marketingu dla społeczności sklepów

Katalog pluginów Claude Code z jednym pluginem `luka`. Uczestnicy instalują go raz, nowe umiejętności dostają w aktualizacjach.

## Struktura

```
.claude-plugin/marketplace.json   katalog roboczy do testów na Twoim komputerze (samodzielny-dev)
plugins/luka/                     plugin, czyli to, co dostają uczestnicy
  .claude-plugin/plugin.json       nazwa i WERSJA (podnieś przy każdym wydaniu)
  CHANGELOG.md                     co nowego (czyta skill co-nowego i version.json)
  skills/start                     poznanie sklepu, pamięć w folderze uczestnika
  skills/branding                  6 modułów marki, brand book dane/marka.md
  skills/seo                       audyt, frazy, teksty stron, AI, Search Console
  skills/aktualizuj                aktualizacja na prośbę uczestnika
  skills/co-nowego                 przegląd nowości i menu
scripts/build.py                   buduje dist/: zip pluginu, marketplace.json, version.json, index.html
.github/workflows/publish.yml      po każdym pushu na main publikuje dist/ na GitHub Pages
docs/index.html                    strona instalacji dla uczestników
docs/PROWADZENIE.md                instrukcja dla Ciebie krok po kroku
docs/OGLOSZENIE.md                 gotowe teksty do społeczności
```

## Wydanie nowej wersji w skrócie

1. Zmień albo dodaj skill w `plugins/luka/skills/`.
2. Przetestuj lokalnie (`docs/PROWADZENIE.md`, Etap 2).
3. Dopisz wpis na górze `plugins/luka/CHANGELOG.md`.
4. Podnieś `version` w `plugins/luka/.claude-plugin/plugin.json`.
5. Commit i push na `main`. Publikacja dzieje się sama.

Bez podniesienia wersji uczestnicy nie dostaną zmian.
