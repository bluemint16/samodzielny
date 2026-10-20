# Tryb 2. Frazy: jak klienci szukają Twoich produktów

Cel: lista prawdziwych fraz pogrupowana w tematy, a każdy temat przypisany do jednej strony sklepu.

## Zasada najważniejsza

Każda fraza ma źródło. Nie wymyślasz liczby wyszukiwań. Jeśli nie masz danych o liczbie wyszukiwań, piszesz "brak danych o liczbie wyszukiwań" i oceniasz frazy po intencji i dopasowaniu do oferty.

## Krok 1. Punkt startu

Z `dane/sklep.md` weź 3–5 najważniejszych kategorii. Zapytaj właściciela, od której zaczynamy (jedna kategoria na jeden przebieg).

## Krok 2. Zbieraj frazy ze źródeł

Dla wybranej kategorii zbierz 20–40 fraz. Przy każdej zapisz źródło.

1. **Podpowiedzi Google** (to, co Google proponuje podczas wpisywania). Pobierz dla nazwy kategorii i jej odmian, także z dopiskami "jak", "jaki", "najlepszy", "czy", "dla", "do", "ranking", "opinie":
   ```bash
   curl -s "https://suggestqueries.google.com/complete/search?client=firefox&hl=pl&gl=pl&q=buty%20do%20biegania%20dla"
   ```
2. **Search Console** (jeśli są pliki w `dane/gsc/`): frazy, na które sklep już się wyświetla.
3. **Język klientów**: pytania i słowa z `dane/klienci.md`, opinie, maile.
4. **Allegro i porównywarki**: jak nazywane są podobne produkty w tytułach ofert (sprawdź 2–3 wyniki).
5. **Narzędzia właściciela**: jeśli ma eksport z Planera słów kluczowych Google, Senuto, Semstorm, Ahrefs albo innego narzędzia, poproś o plik CSV do `dane/`. Tylko stąd bierzesz liczby wyszukiwań.

## Krok 3. Oznacz intencję

Każda fraza dostaje jedną etykietę:
- **zakup**: chce kupić konkretną rzecz ("buty do biegania damskie 38", "krem z witaminą c sklep") → kategoria albo produkt,
- **wybór**: porównuje i wybiera ("jakie buty do biegania na asfalt", "x czy y", "najlepszy...") → poradnik albo porównanie, z linkami do kategorii,
- **wiedza**: chce zrozumieć ("jak dobrać rozmiar butów do biegania") → poradnik albo FAQ,
- **marka**: szuka konkretnej firmy albo produktu po nazwie → strona marki albo produktu.

## Krok 4. Grupuj w tematy i przypisz strony

1. Frazy, na które odpowie ta sama strona, tworzą jeden temat.
2. **Jeden temat = jedna strona.** Dwie strony sklepu na ten sam temat konkurują ze sobą i obie tracą.
3. Dla każdego tematu sprawdź, czy sklep ma już pasującą stronę (kategoria, podkategoria, produkt, wpis na blogu). Jeśli tak, przypisz ją. Lepiej poprawić istniejącą stronę niż tworzyć nową.
4. Nowa strona tylko wtedy, gdy temat jest wart osobnej strony, a sklep żadnej nie ma (np. podkategoria "buty do biegania w terenie", poradnik "jak dobrać rozmiar").

## Krok 5. Wybór na teraz

Wybierz 5 tematów do pracy w pierwszej kolejności. Kryteria: blisko zakupu, sklep ma dobrą ofertę w tym temacie, istniejąca strona do poprawy (szybciej daje efekt niż nowa).

Dla każdego zapisz obietnicę strony: jedno zdanie, co strona musi dać klientowi, żeby fraza miała sens.

## Wynik

Zapisz `wyniki/seo/frazy_[kategoria]_[RRRR-MM-DD].md`:

```markdown
# Frazy: [kategoria], [data]

## Tematy
| Temat | Frazy (źródło) | Intencja | Strona w sklepie | Nowa / istniejąca | Obietnica strony | Kolejność |
|---|---|---|---|---|---|---|

## Na teraz (5 tematów)
1. [temat] → [strona] → [co zrobić]

## Czego nie wiem
- [np. brak danych o liczbie wyszukiwań]
```

Kontrola przed zapisem: każda fraza ma źródło, każda ma intencję, żaden temat nie ma dwóch stron, żadna liczba nie pojawiła się bez narzędzia.

Zaproponuj następny krok: tryb 3 dla pierwszej strony z listy "Na teraz".
