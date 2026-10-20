# Tryb 4. Widoczność w asystentach AI

Cel: sprawdzić, czy ChatGPT, Perplexity, Gemini, Copilot i podsumowania AI w Google polecają sklep przy pytaniach zakupowych, i co miesiąc robić jedną konkretną rzecz na każde pytanie.

Powiedz właścicielowi na starcie, prosto:
"Asystenci AI polecają głównie sklepy i strony, które już są dobrze widoczne w zwykłym Google i mają treści odpowiadające wprost na pytania kupujących. Dlatego zaczynamy od podstaw, a pomiar powtarzamy co miesiąc. Nikt nie może zagwarantować polecenia przez AI."

## Krok 1. Bank 10 pytań kupujących

Ułóż z właścicielem 10 pytań, które klient zadaje asystentowi tuż przed zakupem. Źródła: `dane/klienci.md`, frazy z trybu 2, Search Console (długie frazy brzmiące jak pytanie), pytania z obsługi klienta.

Mieszanka pytań:
- 3 o wybór kategorii: "jakie [produkt] do [zastosowanie] polecasz?"
- 2 porównawcze: "[typ A] czy [typ B] dla [osoba]?"
- 2 o sklep: "gdzie kupić [produkt] w Polsce z [cecha]?"
- 2 o problem: "jak [rozwiązać problem], który rozwiązuje produkt?"
- 1 o markę: "[nazwa sklepu] opinie" albo "czy [nazwa sklepu] jest wiarygodny?"

Zasada: brzmienie pytania jest zamrożone. Zmiana brzmienia to nowe pytanie z nowym numerem. Inaczej porównanie miesiąc do miesiąca nic nie znaczy.

## Krok 2. Pomiar

Nie masz bezpośredniego dostępu do ChatGPT ani innych asystentów, więc pomiar robi właściciel. Przygotuj mu plik `wyniki/seo/ai_pomiar_[RRRR-MM].md` z pytaniami do skopiowania i tabelą:

```markdown
| Nr | Pytanie | Asystent | Status | Kogo poleca zamiast nas | Czy podał link do nas |
|---|---|---|---|---|---|
| P1 | ... | ChatGPT | | | |
```

Statusy: **POLECA** (sklep wymieniony jako rekomendacja), **WSPOMINA** (pada nazwa, ale bez rekomendacji), **BRAK** (sklepu nie ma).

Instrukcja dla właściciela: zadaj każde pytanie w nowej rozmowie, bez logowania albo w trybie bez historii (żeby wcześniejsze rozmowy nie wpływały na wynik), na przynajmniej 2 asystentach. Wklej wynik albo wpisz statusy. Zajmie to około 30 minut miesięcznie.

Gdy właściciel wróci z wynikami, przeanalizuj je i sprawdź: jakie strony i sklepy asystenci cytują zamiast niego. Pobierz 2–3 z nich i opisz, co mają, czego sklepowi brakuje.

## Krok 3. Jedna akcja na pytanie

Każde pytanie dostaje w danym miesiącu dokładnie jedną akcję:

| Sytuacja | Co zrobić |
|---|---|
| BRAK, a sklep nie ma strony odpowiadającej na to pytanie | Napisz poradnik albo porównanie odpowiadające wprost na pytanie (tryb 3 dla nowej strony) |
| BRAK, a strona jest, ale słaba w Google | Popraw istniejącą stronę: odpowiedź w pierwszych zdaniach, konkrety, FAQ |
| Asystent cytuje ranking albo artykuł innego serwisu | Zgłoś sklep autorowi rankingu z konkretnym powodem (test produktu, próbka, dane). Nie płać za ukryte wpisy |
| WSPOMINA bez polecenia | Dodaj na stronie dowody: opinie, liczby, certyfikaty, uczciwe "dla kogo to jest, a dla kogo nie" |
| Różne informacje o sklepie w sieci | Ujednolić dane: strona, Profil Firmy w Google, Allegro, Ceneo, social media |
| POLECA | Nic nowego. Pilnuj aktualności strony (ceny, dostępność, data aktualizacji) |

Jeśli ta sama akcja przez 2 miesiące nic nie zmienia, wróć do diagnozy zamiast powtarzać.

## Krok 4. Cechy strony, którą AI chętnie cytuje

Przy pisaniu nowych treści (tryb 3) dopilnuj:
1. Odpowiedź na pytanie w pierwszych 2–3 zdaniach, przed historią i wstępem.
2. Krótkie zdania, które są prawdziwe po wyjęciu z akapitu.
3. Przy porównaniu: jedna tabela, te same kryteria dla każdej opcji, przy każdej opcji "dla kogo".
4. Uczciwe ograniczenie także własnego produktu ("nie polecamy, jeśli..."). To buduje wiarygodność.
5. Konkrety ze źródłem: wymiary, skład, testy, dane własne sklepu.
6. Widoczna data aktualizacji i autor (osoba ze sklepu).
7. Treść w kodzie HTML, nie tylko po uruchomieniu skryptów.

## Krok 5. Podstawy techniczne (jeśli nie było audytu)

Sprawdź z trybu 1, sekcja E: roboty AI w `robots.txt`, treść w HTML, spójność danych o sklepie, pomiar ruchu z asystentów w Google Analytics.

Produkty w zakupach AI: asystenci rozwijają wyszukiwanie produktów (np. zakupy w ChatGPT, Perplexity, Google). Programy dla sprzedawców zmieniają się szybko. Przed rekomendacją sprawdź w internecie aktualne zasady dodawania produktów sklepu i podaj źródło z datą. Dobry fundament prawie zawsze ten sam: kompletny i aktualny plik produktów (np. w Google Merchant Center) i poprawne dane strukturalne.

## Rytm

Pomiar co miesiąc tymi samymi pytaniami. Po 3 miesiącach porównaj z pierwszym pomiarem i pokaż różnicę w tabeli. Zapisuj w `stan.md` datę kolejnego pomiaru.
