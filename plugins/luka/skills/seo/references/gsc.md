# Tryb 5. Przegląd miesiąca z Google Search Console

Google Search Console (w skrócie GSC) to darmowe narzędzie Google. Pokazuje, na jakie frazy sklep wyświetla się w Google, ile osób klika i na jakiej pozycji jest strona. Bez tych danych zgadujemy, z nimi decydujemy.

## Podłączenie (jeśli właściciel jeszcze nie ma)

Poprowadź krok po kroku, jedno polecenie naraz:
1. Wejdź na `https://search.google.com/search-console` i zaloguj się kontem Google firmy.
2. Dodaj usługę typu "Domena" (wymaga dodania wpisu DNS u dostawcy domeny) albo "Prefiks URL" (prostsze, np. przez tag HTML albo Google Analytics).
3. Sprawdź, czy platforma sklepu ma prostą drogę weryfikacji (`references/platformy.md`).
4. Po weryfikacji dodaj mapę strony: menu Mapy witryn, wpisz adres mapy (np. `sitemap.xml`).
5. Dane zaczną się zbierać od tego dnia. Pierwszy sensowny przegląd za około 4 tygodnie.

## Eksport danych (co miesiąc)

Instrukcja dla właściciela:
1. Search Console → Skuteczność → Wyniki wyszukiwania.
2. Ustaw zakres dat: ostatnie 3 miesiące.
3. Kliknij "Eksportuj" (prawy górny róg) → "Pobierz CSV".
4. Rozpakuj plik i wrzuć całą zawartość do folderu `dane/gsc/[RRRR-MM]/`.

Pliki, z których korzystasz: `Zapytania.csv` (frazy), `Strony.csv` (adresy). Nazwy mogą się różnić zależnie od języka konta. Rozpoznaj je po zawartości.

## Analiza

Wczytaj pliki (np. prostym skryptem Python albo czytając CSV). Pokaż wyniki w 4 grupach:

1. **Szybkie wygrane**: frazy na pozycjach około 4–20 z dużą liczbą wyświetleń. Strona jest blisko pierwszej strony wyników. Poprawa istniejącej strony (tryb 3) daje tu najszybszy efekt.
2. **Wyświetlenia bez kliknięć**: dużo wyświetleń, bardzo niski CTR (procent osób, które kliknęły). Zwykle tytuł albo opis meta nie przekonuje. Zaproponuj nowe wersje.
3. **Nowe tematy**: frazy, na które sklep się wyświetla, choć nie ma dla nich dobrej strony. Kandydaci na podkategorię albo poradnik (tryb 2).
4. **Spadki**: strony, które straciły kliknięcia względem poprzedniego miesiąca (jeśli jest poprzedni eksport w `dane/gsc/`).

## Kontrola konkurencji własnych stron

Zanim zaproponujesz nową stronę na frazę, sprawdź, czy sklep już ma stronę, która się na nią wyświetla (w GSC: filtr zapytania, zakładka Strony; albo w Google: `site:adres-sklepu fraza`). Jeśli tak, popraw tę stronę zamiast tworzyć drugą, bo dwie strony na ten sam temat konkurują ze sobą.

## Wynik

Zapisz `wyniki/seo/przeglad_[RRRR-MM].md`:

```markdown
# Przegląd SEO, [miesiąc]

## Liczby miesiąca
Kliknięcia: [ ] (poprzednio [ ]), wyświetlenia: [ ], średnia pozycja: [ ]

## Szybkie wygrane (do poprawy w tym miesiącu)
| Fraza | Strona | Pozycja | Wyświetlenia | Co zrobić |

## Tytuły do zmiany
| Strona | Wyświetlenia | CTR | Nowy tytuł | Nowy opis meta |

## Nowe tematy
| Fraza | Czy mamy stronę | Propozycja |

## Spadki
| Strona | Było | Jest | Możliwy powód |

## Plan na miesiąc (najwyżej 3 zadania)
1. ...
```

Najwyżej 3 zadania na miesiąc. Lepiej zrobić 3 niż zaplanować 15. Liczby bierzesz tylko z plików. Nie zaokrąglaj w górę i nie interpretuj jednego miesiąca jako trendu.
