---
name: co-nowego
description: Pokazuje, co nowego w asystencie marketingu sklepu i jakie umiejętności są dostępne. Używaj, gdy użytkownik pisze "co nowego", "co umiesz", "jakie masz umiejętności", "pomoc", "menu", "lista komend", "co potrafisz".
---

# Co nowego i co umiem

0. Sprawdź wersję zainstalowaną i dostępną:
   ```bash
   claude plugin list 2>/dev/null | grep -A4 "luka@samodzielny" | grep -i version
   curl -fsS --max-time 5 "{{BASE_URL}}/version.json"
   ```
   Jeśli dostępna wersja jest wyższa, zacznij odpowiedź od: "Jest nowa wersja asystenta ([dostępna], masz [zainstalowana]). Napisz: aktualizuj". Potem pokaż też, co nowego w wersji dostępnej (pole `zmiany` z `version.json`). Błąd albo brak internetu = pomiń ten krok.
1. Przeczytaj `${CLAUDE_PLUGIN_ROOT}/CHANGELOG.md`. Jeśli ścieżka nie działa, znajdź plik poleceniem:
   ```bash
   find ~/.claude/plugins -path "*luka*" -name CHANGELOG.md 2>/dev/null | sort | tail -1
   ```
2. Pokaż użytkownikowi po ludzku dwie ostatnie wersje: co nowego i jak tego użyć (jedno zdanie przykładu na każdą nowość).
3. Pokaż menu wszystkich umiejętności:

```text
Co umiem:
- start: poznaję Twój sklep i zakładam pamięć asystenta
- branding: budujemy markę krok po kroku, kończymy brand bookiem
- seo: audyt, frazy, opisy kart i kategorii, widoczność w AI, przegląd Search Console
- aktualizuj: pobieram najnowszą wersję
- co nowego: to, co czytasz

Nie musisz pamiętać nazw. Napisz po prostu, czego potrzebujesz.
```

4. Jeśli w folderze jest `stan.md`, dodaj na końcu: "Ostatnio robiliśmy: [ostatnia linia z Zrobione]. Proponuję: [Następny krok]".
