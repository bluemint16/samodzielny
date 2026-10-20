---
name: aktualizuj
description: Aktualizuje asystenta marketingu sklepu do najnowszej wersji z nowymi umiejętnościami. Używaj, gdy użytkownik pisze "aktualizuj", "aktualizacja", "zaktualizuj asystenta", "nowa wersja", "update", "pobierz nowe umiejętności".
---

# Aktualizacja asystenta

Aktualizacja podmienia tylko umiejętności asystenta. Pliki właściciela (`dane/`, `wyniki/`, `stan.md`, `CLAUDE.md`) zostają nietknięte.

## Kroki

1. Sprawdź wersję zainstalowaną i dostępną:
   ```bash
   claude plugin list 2>/dev/null | grep -A4 "luka@samodzielny" | grep -i version
   curl -fsS --max-time 10 "{{BASE_URL}}/version.json"
   ```
2. Jeśli wersje są równe, napisz: "Masz najnowszą wersję [X]." i zakończ.
3. Jeśli jest nowsza, pokaż po ludzku, co się zmieni (pole `zmiany` z `version.json`), i zapytaj: "Zaktualizować? Wystarczy OK."
4. Po zgodzie uruchom:
   ```bash
   claude plugin marketplace update samodzielny
   claude plugin update luka@samodzielny
   ```
5. Sprawdź wynik ponownie poleceniem z punktu 1.
   - Sukces: "Zaktualizowano do wersji [X]. Zamknij tę rozmowę i otwórz nową, żeby nowe umiejętności zaczęły działać. Potem napisz: co nowego". W terminalu wystarczy też polecenie `/reload-plugins`.
   - Błąd: pokaż w jednym prostym zdaniu, co się stało (bez surowego komunikatu, chyba że użytkownik poprosi), i zaproponuj: "Spróbuj jeszcze raz za kilka minut. Jeśli dalej nie działa, napisz w społeczności w wątku Pomoc i wklej ten opis: [krótki opis błędu]".

## Automatyczne aktualizacje

Jeśli użytkownik pyta, jak dostawać aktualizacje samemu:
"W terminalu Claude Code wpisz `/plugin`, przejdź do zakładki Marketplaces, wybierz samodzielny i kliknij Enable auto-update. Od tej pory nowe wersje pobiorą się same, a zadziałają od kolejnej rozmowy."

Nie zmieniaj plików ustawień Claude na własną rękę.
