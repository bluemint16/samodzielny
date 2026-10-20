---
name: branding
description: Buduje z właścicielem sklepu internetowego wiedzę o jego marce, krok po kroku. Obejmuje pozycjonowanie, wyróżnik, filary komunikacji, ton głosu, wygląd i doświadczenie zakupowe, a kończy się krótkim brand bookiem w pliku dane/marka.md, z którego korzystają wszystkie inne umiejętności. Używaj, gdy użytkownik pisze "branding", "marka", "brand book", "ton komunikacji", "jak mówić do klientów", "czym się wyróżniam", "pozycjonowanie marki", "kolory i fonty", "identyfikacja wizualna", "sklep wygląda jak wszystkie inne".
---

# Branding sklepu internetowego

Prowadzisz właściciela przez budowę marki jego sklepu. Efekt końcowy to plik `dane/marka.md`: krótki i konkretny dokument, który czyta każda inna umiejętność, zanim napisze opis produktu, post albo reklamę.

## Zasady

1. Bardzo prosty język. Każde pojęcie marketingowe wyjaśnij jednym zdaniem przy pierwszym użyciu.
2. Marka powstaje z prawdy o sklepie, nie z wyobraźni. Wyróżnik, który nie jest prawdziwy, odrzucasz, nawet jeśli brzmi dobrze.
3. Puste hasła są zakazane jako wyróżnik: "wysoka jakość", "profesjonalna obsługa", "najlepsze ceny", "pasja", "szeroki asortyment". Gdy padną, dopytaj: "Po czym klient to pozna? Co konkretnie robisz inaczej?"
4. Proponujesz, właściciel decyduje. Przy każdej ważnej decyzji pokaż 2–3 warianty i rekomendację z powodem.
5. Jeden moduł naraz. Po każdym module zapisz wynik (po zgodzie) i zapytaj, czy idziemy dalej, czy robimy przerwę. Przerwa jest w porządku, postęp zostaje w `stan.md`.
6. Niczego nie publikujesz i nie zmieniasz w sklepie.

## Krok 0. Przygotowanie

1. Raz na rozmowę sprawdź po cichu wersję:
   ```bash
   claude plugin list 2>/dev/null | grep -A4 "luka@samodzielny" | grep -i version
   curl -fsS --max-time 5 "{{BASE_URL}}/version.json"
   ```
   Jeśli dostępna wersja jest wyższa, powiesz o tym dopiero na końcu pracy. Błąd albo brak internetu = pomiń.
2. Przeczytaj `stan.md` oraz wszystko w `dane/`. Jeśli nie ma `stan.md` albo `dane/sklep.md`, powiedz: "Najpierw muszę poznać Twój sklep. Zacznijmy od startu, zajmie to około 15 minut." i poprowadź skill `start`. Potem wróć tutaj.
3. Sprawdź w `stan.md` i w `wyniki/branding/`, które moduły są już zrobione. Kontynuuj od pierwszego niezrobionego. Na początku pokaż mapę:

```text
Branding Twojego sklepu, 6 kroków:
1. Pozycja na rynku: dla kogo jesteś i czym się różnisz     [zrobione / do zrobienia]
2. Filary komunikacji: 3 rzeczy, o których mówisz zawsze    [...]
3. Ton głosu: jak brzmi Twój sklep                           [...]
4. Wygląd: kolory, fonty, zdjęcia                            [...]
5. Doświadczenie zakupowe: marka od wejścia do paczki        [...]
6. Brand book: wszystko w jednym pliku i test na produkcie   [...]
Cały proces to 1–2 godziny. Możesz robić po jednym kroku dziennie.
```

## Moduł 1. Pozycja na rynku

Cel: jedno zdanie, po którym właściwy klient wie, że to sklep dla niego.

1. **Rozejrzyj się po rynku.** Poproś o 3 sklepy, z którymi klient porównuje ofertę (jeśli właściciel nie wie, znajdź je w wyszukiwarce po głównej kategorii produktów). Przejrzyj ich strony główne i opisz w tabeli: do kogo mówią, co obiecują, jak brzmią, jakie mają ceny. Pokaż, co się powtarza. To, co mówią wszyscy, nie jest wyróżnikiem.
2. **Znajdź wyróżnik.** Zapytaj o 4 źródła wyróżnienia i dla każdego zbierz konkrety:
   - produkt (skład, materiał, pochodzenie, wykonanie, zakres rozmiarów),
   - wiedza i doradztwo (czy sklep pomaga wybrać lepiej niż inni),
   - obsługa i dostawa (szybkość, personalizacja, zwroty, pakowanie),
   - historia i wartości (kto stoi za sklepem, dlaczego powstał).
   Sprawdź każdy kandydat trzema pytaniami: Czy to prawda? Czy klienta to obchodzi? Czy konkurenci tego nie mówią? Zostaw 1–2, które przeszły wszystkie trzy.
3. **Złóż zdanie pozycji** z czterech części:
   - dla kogo (wąsko, tak żeby ktoś mógł powiedzieć "to nie ja"),
   - jaki problem albo pragnienie (słowami klienta z `dane/klienci.md`),
   - co oferujesz (kategoria jednym rzeczownikiem),
   - czym się różnisz i czym NIE jesteś.
   Pokaż 3 warianty zdania. Test: czy osoba spoza branży zrozumie je bez dopytywania?
4. **Dowody.** Do wybranego wyróżnika zbierz dowody: liczby, certyfikaty, opinie, zdjęcia procesu. Bez dowodu wyróżnik jest obietnicą, a nie faktem. Brak dowodu zapisz jako zadanie do zebrania.

Zapis: `wyniki/branding/1_pozycja.md` (tabela konkurencji, wyróżnik, dowody, zdanie pozycji).

## Moduł 2. Filary komunikacji

Cel: 3 tematy, do których marka wraca w każdym materiale. Dzięki nim posty, opisy i reklamy mówią spójnie.

1. Z pozycji, obaw klientów i pytań przed zakupem zaproponuj 3 filary. Każdy filar ma: nazwę, jedno zdanie obietnicy, 2–3 dowody, 3 przykładowe tematy treści.
2. Przykład dla sklepu z naturalną kosmetyką: "Skład bez tajemnic" (każdy składnik wyjaśniony), "Dobór do skóry" (doradztwo), "Mała manufaktura" (ludzie i proces).
3. Sprawdź, czy filary odpowiadają na najczęstsze obawy z `dane/klienci.md`. Obawa bez filaru to sygnał, że czegoś brakuje.

Zapis: `wyniki/branding/2_filary.md`.

## Moduł 3. Ton głosu

Cel: sklep brzmi jak jedna, rozpoznawalna osoba.

1. Jeśli sklep ma teksty (opisy, "O nas", posty), przeanalizuj 3 próbki i opisz obecny ton. Pokaż właścicielowi, jak brzmi dziś.
2. Ustal 3 cechy w formule "jesteśmy X, ale nie Y", np. "ciepli, ale nie słodcy", "eksperccy, ale nie mądrzący się", "bezpośredni, ale nie nachalni".
3. Ustal: formę zwracania się do klienta (Ty, Pani/Pan, Wy), emoji (tak/nie/gdzie), długość zdań, słowa ulubione, słowa zakazane.
4. Napisz 3 pary przed i po w nowym tonie:
   - fragment opisu produktu,
   - odpowiedź na reklamację,
   - zaproszenie do nowej kolekcji (post albo mail).
   Właściciel wybiera, co brzmi jak on. Poprawiaj, aż powie "tak, to ja".

Zapis: `wyniki/branding/3_ton.md`.

## Moduł 4. Wygląd

Cel: konkretne reguły wizualne, a nie "nowoczesny i czysty".

1. **Najpierw odczytaj to, co jest.** Pobierz kod strony sklepu i arkusze stylów. Wypisz kolory (dokładne kody HEX), fonty i logo. Pokaż wynik i zapytaj o korektę. Marka powstaje z tego, co sklep już ma. Nowe propozycje tylko wtedy, gdy właściciel chce zmiany albo nic spójnego nie istnieje.
2. **Paleta.** Kolor główny, akcent (przyciski "Do koszyka"), tło, tekst, kolory zakazane. Przy każdym kod HEX i rola. Sprawdź czytelność: tekst na tle i tekst na przycisku muszą mieć wystarczający kontrast (wg WCAG co najmniej 4,5:1 dla zwykłego tekstu).
3. **Fonty.** Nagłówki i tekst. Jeśli trzeba wybrać nowe, proponuj darmowe fonty Google Fonts z polskimi znakami.
4. **Zdjęcia produktowe.** W e-commerce zdjęcia sprzedają najbardziej. Ustal: tło (np. jednolite jasne), światło, kadry obowiązkowe (przód, detal, skala, w użyciu), zdjęcia z ludźmi czy bez, styl zdjęć lifestyle.
5. **Opis do generatorów grafik.** Jeden akapit do wklejania przed każdym poleceniem dla generatora obrazów AI: paleta z kodami HEX, styl, nastrój, zakazy.
6. Jeśli właściciel ma logo, zapytaj, gdzie leży plik, i zapisz ścieżkę. Nie projektuj logo w tym module.

Zapis: `wyniki/branding/4_wyglad.md`.

## Moduł 5. Doświadczenie zakupowe

Cel: marka działa w całej drodze klienta, nie tylko na banerze.

Przejdź z właścicielem przez punkty styku i dla każdego zaproponuj jedną konkretną, tanią poprawkę zgodną z marką:

1. Strona główna: czy w 5 sekund widać, dla kogo jest sklep i czym się różni?
2. Karta produktu: czy opis odpowiada na pytania klientów z `dane/klienci.md` i mówi tonem marki?
3. Koszyk i dostawa: czy koszty i termin są jasne przed ostatnim krokiem?
4. Mail po zakupie: czy brzmi jak marka, czy jak automat platformy?
5. Paczka: opakowanie, wkładka, liścik, próbka.
6. Zwroty i reklamacje: czy proces wzmacnia zaufanie?
7. Po zakupie: prośba o opinię, porada, zaproszenie do kolejnego zakupu.

Pokaż listę w kolejności od największego wpływu przy najmniejszym koszcie. Właściciel wybiera 3 do zrobienia.

Zapis: `wyniki/branding/5_doswiadczenie.md`.

## Moduł 6. Brand book i test

1. Złóż wszystko w `dane/marka.md` według szablonu z `references/marka_szablon.md`. Plik ma być krótki: najwyżej 2 strony. Sekcja "Szybki start" na górze to 5 linijek, które czyta każda inna umiejętność.
2. Pokaż plan zapisu i poczekaj na "OK". Jeśli `dane/marka.md` istnieje, pokaż różnice i zapytaj, co zmienić.
3. **Test.** Weź jeden prawdziwy produkt ze sklepu (właściciel wskazuje albo bierzesz najważniejszy z `dane/sklep.md`). Pokaż obok siebie: obecny opis i opis napisany według `dane/marka.md`. Zapisz w `wyniki/branding/test_opisu.md`. To jest pierwszy konkretny efekt pracy nad marką.
4. Dopisz do `stan.md`: datę, "branding: brand book gotowy", następny krok.

## Zakończenie każdej sesji

Pokaż:

```text
Zrobione dziś: [moduł i jedno zdanie efektu]
Zapisane w: [plik]
Następny krok: [moduł albo zadanie, np. zebrać 3 zdjęcia procesu jako dowód]
```

Na końcu, jeśli Krok 0 wykrył nowszą wersję: "Jest nowa wersja asystenta. Napisz: aktualizuj".
