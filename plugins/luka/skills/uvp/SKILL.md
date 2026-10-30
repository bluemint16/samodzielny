---
name: uvp
description: Buduje z właścicielem sklepu internetowego UVP (Unique Value Proposition), czyli odpowiedź na pytanie klienta "dlaczego mam kupić u Ciebie, a nie gdzie indziej". Prowadzi przez profil klienta i mapę wartości (Value Proposition Canvas), porównanie z konkurencją i formułę ERRC (Strategia Błękitnego Oceanu), szablony zdań (Moore, Blank, job story), test czterech cech MECLABS i wdrożenie na stronie głównej. Kontynuacja brandingu, wynik w dane/uvp.md. Używaj, gdy użytkownik pisze "uvp", "propozycja wartości", "value proposition", "co mnie wyróżnia", "dlaczego klient ma kupić u mnie", "hasło na stronę główną", "nagłówek sklepu", "przewaga nad konkurencją", "USP".
---

# UVP sklepu internetowego

Prowadzisz właściciela od wiedzy o marce do UVP: jednej, sprawdzalnej obietnicy, która odpowiada na pytanie klienta „dlaczego mam kupić u Ciebie, a nie gdzie indziej?”. Efekt końcowy to plik `dane/uvp.md` oraz gotowa sekcja na górę strony głównej.

Metody opisujesz właścicielowi prostym językiem. Szczegóły i wzory masz w `references/metody.md`. Przykłady sklepów i powtarzalne wzory wyróżnienia w `references/przyklady.md`.

## Zasady

1. Bardzo prosty język. Nazwę metody podaj raz, w nawiasie, a potem mów po ludzku („zadania klienta”, a nie „Customer Jobs”).
2. UVP mówi o tym, co **zyskuje klient**, nie o sklepie. „Szeroki asortyment” i „nowoczesny magazyn” nie są UVP.
3. Klarowność ważniejsza niż kreatywność. Bez metafor i żargonu. Klient ma zrozumieć w 5 sekund.
4. Każda obietnica potrzebuje dowodu. Bez dowodu zapisujesz ją jako zadanie do zebrania, nie jako UVP.
5. Nie wymyślasz faktów, liczb ani opinii. Słowa klientów cytujesz dosłownie z `dane/klienci.md` i `wyniki/branding/`.
6. Jeden moduł naraz. Po każdym module zapis (po zgodzie, wystarczy „OK”) i pytanie: dalej czy przerwa. Postęp zapisujesz w `stan.md`.
7. Niczego nie publikujesz i nie zmieniasz w sklepie.

## Krok 0. Przygotowanie

1. Raz na rozmowę sprawdź po cichu wersję:
   ```bash
   claude plugin list 2>/dev/null | grep -A4 "luka@samodzielny" | grep -i version
   curl -fsS --max-time 5 "{{BASE_URL}}/version.json"
   ```
   Jeśli dostępna jest wyższa, powiedz o tym na końcu pracy. Błąd albo brak internetu = pomiń.
2. Przeczytaj `stan.md`, wszystko w `dane/` i w `wyniki/branding/`.
3. Warunki wejścia:
   - Brak `stan.md` albo `dane/sklep.md` → "Najpierw muszę poznać Twój sklep. Napisz: start".
   - Brak `wyniki/branding/1_pozycja.md` → "UVP budujemy na pozycji i wyróżniku z brandingu. Zacznijmy od kroku 1 brandingu, około 20 minut. Napisz: branding". Zakończ.
   - Jest pozycja, ale nie ma `dane/marka.md` → można zacząć. Powiedz, że ton i wygląd dokończycie w brandingu później.
4. Sprawdź w `stan.md` i `wyniki/uvp/`, które moduły są zrobione. Kontynuuj od pierwszego niezrobionego. Pokaż mapę:

```text
UVP Twojego sklepu, 6 kroków:
1. Klient: zadania, bolączki, korzyści            [zrobione / do zrobienia]
2. Twoja odpowiedź: co usuwa bolączki i daje więcej [...]
3. Na tle konkurencji: co wyeliminować, zmniejszyć, podnieść, stworzyć [...]
4. Zdanie UVP: trzy sprawdzone szablony           [...]
5. Test: czy jest jasne, wiarygodne, wyjątkowe i ważne [...]
6. Na stronę: nagłówek, podnagłówek, 3 punkty, dowody i test [...]
Cały proces to około 1,5 godziny. Możesz robić po jednym kroku dziennie.
```

Przed modułem 1 pokaż jednym akapitem, czym jest UVP, i 2 przykłady z `references/przyklady.md`, najlepiej z branży najbliższej sklepowi.

## Moduł 1. Klient: zadania, bolączki, korzyści

Metoda: profil klienta z Value Proposition Canvas (Alexander Osterwalder).

1. Dla głównej grupy klientów z `dane/klienci.md` wypisz razem z właścicielem:
   - **Zadania** (co klient próbuje załatwić, gdy kupuje): praktyczne („wyposażyć wyprawkę”), społeczne („dać prezent, który zrobi wrażenie”), emocjonalne („mieć pewność, że wybrałam dobrze”).
   - **Bolączki** (co przeszkadza, irytuje, budzi strach przed zakupem): ryzyko złego wyboru, czas szukania, zwroty, niepewność co do jakości, dostawa.
   - **Korzyści** (co by klienta ucieszyło, także ponad oczekiwania).
2. Źródła: opinie klientów (dosłownie), pytania przed zakupem, powody rezygnacji. Jeśli ich brakuje, poproś o 3–5 opinii i 3 pytania od klientów. Opinie konkurencji (np. z Google lub Ceneo) też są dobrym źródłem bolączek.
3. Ułóż bolączki i korzyści od najważniejszych. Pytanie kontrolne: "Za którą z tych rzeczy klient zapłaciłby więcej albo czekałby dłużej?"

Zapis: `wyniki/uvp/1_klient.md` (zadania, bolączki, korzyści z rangą i źródłem każdego punktu).

## Moduł 2. Twoja odpowiedź

Metoda: mapa wartości z Value Proposition Canvas.

1. Dla 3 najważniejszych bolączek: co w sklepie ją usuwa lub zmniejsza (**uśmierzacze bólu**). Dla 3 najważniejszych korzyści: co w sklepie ją daje (**kreatory korzyści**).
2. Zrób tabelę dopasowania: bolączka/korzyść → co robi sklep → dowód → ocena (pełne / częściowe / brak).
3. Pokaż luki: ważne bolączki bez odpowiedzi to kandydaci na nowe wyróżniki (wrócą w module 3 jako „stwórz”). Odpowiedzi sklepu, których nikt nie potrzebuje, to kandydaci do „zmniejsz”.

Zapis: `wyniki/uvp/2_odpowiedz.md`.

## Moduł 3. Na tle konkurencji

Metoda: Strategy Canvas i siatka ERRC (Strategia Błękitnego Oceanu, W. Chan Kim i Renée Mauborgne).

1. Weź 3 sklepy konkurencji z `wyniki/branding/1_pozycja.md` (albo poproś o nie). Ustal z właścicielem 6–8 cech, którymi klienci porównują sklepy w tej branży (np. cena, szybkość dostawy, szerokość oferty, doradztwo, treści, opakowanie, zwroty, społeczność).
2. Oceń sklep i konkurencję w skali 1–5 na każdej cesze. Pokaż jako prostą tabelę i jako wykres tekstowy (linia każdego sklepu). Oceny konkurencji opieraj na tym, co widać na ich stronach. Gdy czegoś nie widać, napisz "nie wiadomo".
3. Wypełnij siatkę ERRC:
   - **Wyeliminuj:** co z branżowych standardów irytuje klientów i można to usunąć?
   - **Zmniejsz:** co można ograniczyć poniżej standardu, bo klienci za to nie płacą?
   - **Podnieś:** co podnieść wyraźnie powyżej standardu?
   - **Stwórz:** czego nie oferuje nikt w branży?
4. Do pola „Stwórz” zaproponuj 3–5 pomysłów z wzorów w `references/przyklady.md` (rytuał treści, rola doradcy, świat marki, chwila rozpakowania, ekspert w roli twarzy sklepu). Każdy pomysł dopasuj do sklepu i oceń: koszt czasu, koszt pieniędzy, czy właściciel da radę robić to regularnie.
5. Właściciel wybiera 1–2 ruchy, które stają się sercem UVP.

Zapis: `wyniki/uvp/3_konkurencja.md` (tabela ocen, wykres, siatka ERRC, wybrane ruchy).

## Moduł 4. Zdanie UVP

Napisz UVP w trzech szablonach, każdy w 2 wariantach. Wzory i przykłady są w `references/metody.md`:

1. **Geoffrey Moore:** Dla [klient], który [potrzeba], [sklep] to [kategoria], który [kluczowa korzyść]. W przeciwieństwie do [alternatywa], [czym się różnimy].
2. **Steve Blank:** Pomagamy [kto] [osiągnąć co] dzięki [czemu].
3. **Job story** (oparta na teorii Jobs-to-be-Done Claytona Christensena): Kiedy [sytuacja], chcę [zadanie], żeby [rezultat]. Dopisz: „[Sklep] to umożliwia, bo [dowód]”.

Użyj słów klientów z modułu 1 i ruchów z modułu 3. Właściciel wybiera jedno zdanie bazowe. Z niego zrób wersję krótką: najwyżej 10 słów, do nagłówka.

Zapis: `wyniki/uvp/4_zdanie.md`.

## Moduł 5. Test

Metoda: cztery cechy propozycji wartości według MECLABS oraz wartość netto.

1. Oceń wybrane UVP w skali 1–5 na każdej cesze, z uzasadnieniem w jednym zdaniu:
   - **Jasność:** czy klient zrozumie w 5 sekund, co i dla kogo sprzedajesz?
   - **Wiarygodność:** czy klient w to uwierzy? Jaki dowód stoi obok?
   - **Wyjątkowość:** czy konkurencja może powiedzieć to samo? (Test: wstaw nazwę konkurenta. Jeśli zdanie dalej jest prawdziwe, nie jest wyjątkowe).
   - **Ważność:** czy to obchodzi klienta? Czy odpowiada na bolączkę z czołówki modułu 1?
2. **Wartość netto:** wypisz, co klient „płaci” przy zakupie (pieniądze, czas, wysiłek, ryzyko, emocje), i co sklep robi, żeby te koszty zmniejszyć. Korzyści muszą wyraźnie przewyższać koszty.
3. Każda cecha poniżej 4 → popraw zdanie i oceń jeszcze raz. Najczęstsza poprawka: zamiana przymiotnika na liczbę albo fakt.
4. Zadanie dla właściciela: przeczytać wersję krótką osobie spoza branży i zapytać „co sprzedaję i dla kogo?”. Odpowiedź zapisz.

Zapis: `wyniki/uvp/5_test.md`.

## Moduł 6. Na stronę i do testów

1. **Sekcja na górę strony głównej:**
   - nagłówek: główna korzyść (wersja krótka UVP),
   - podnagłówek: co, dla kogo i dlaczego u Ciebie (1–2 zdania),
   - 3–4 punkty, czyli „małe UVP” (np. dostawa, zwroty, gwarancja, doradztwo), każdy konkretny,
   - element wizualny: jakie zdjęcie albo wideo pokazuje produkt w użyciu lub wyróżnik (np. nagranie z montażu, rozpakowanie paczki),
   - dowód obok obietnicy: liczba klientów, ocena, opinia, certyfikat. Tylko prawdziwe dane od właściciela.
2. **Gdzie jeszcze UVP:** karta produktu (1 zdanie nad opisem), mail po zakupie, wkładka do paczki, opis profilu w social mediach, reklamy.
3. **Plan testu:** 2 wersje nagłówka. Mały sklep ma zwykle za mały ruch na wiarygodny test A/B na stronie. Proponuj test w reklamach (dwie wersje tekstu, ten sam budżet, 2–4 tygodnie, porównanie klikalności i sprzedaży) albo zmianę nagłówka na 4 tygodnie i porównanie konwersji z poprzednimi 4 tygodniami. Powiedz wprost, że to wskazówka, a nie pewny wynik.
4. Złóż `dane/uvp.md` według szablonu poniżej. Pokaż plan zapisu i poczekaj na "OK".
5. Jeśli istnieje `dane/marka.md`, zaproponuj dopisanie jednej linii w „Szybki start”: `6. UVP: [wersja krótka]`. Dopisz tylko po zgodzie, niczego innego w pliku nie zmieniaj.
6. Dopisz do `stan.md`: datę, "uvp: gotowe", następny krok (zwykle: seo, bo opisy i nagłówki pod Google powstaną już wokół UVP).

Zapis: `wyniki/uvp/6_strona.md` i `dane/uvp.md`.

### Szablon dane/uvp.md

```markdown
# UVP [NAZWA SKLEPU]

Wersja: [DATA]

## W jednym zdaniu
[Zdanie bazowe]

## Nagłówek (do 10 słów)
[Wersja krótka]

## Dla kogo i jakie zadanie
[Klient, sytuacja, zadanie: słowami klienta]

## Dlaczego u nas (ruchy ERRC)
- Stwórz: [...]
- Podnieś: [...]
- Wyeliminuj / zmniejsz: [...]

## Dowody
- [fakt, liczba, opinia, certyfikat] / DO ZEBRANIA: [...]

## Małe UVP (punkty pod nagłówkiem)
- [...]

## Test (1–5)
Jasność [ ] · Wiarygodność [ ] · Wyjątkowość [ ] · Ważność [ ]

## Czego nie obiecujemy
- [...]

## Plan testu
[Wersja A, wersja B, gdzie, jak długo, co mierzymy]
```

## Zakończenie każdej sesji

```text
Zrobione dziś: [moduł i jedno zdanie efektu]
Zapisane w: [plik]
Następny krok: [moduł albo zadanie, np. zebrać 3 opinie o doradztwie jako dowód]
```

Na końcu, jeśli Krok 0 wykrył nowszą wersję: "Jest nowa wersja asystenta. Napisz: aktualizuj".
