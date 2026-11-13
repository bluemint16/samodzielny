# Ruch 01. Radar tematów

**Po co:** dobre posty sklepu zaczynają się od pytań i problemów, które klienci naprawdę mają, a nie od pomysłu „co by tu wrzucić”. Dzisiaj nie piszemy posta. Budujemy radar, który będzie regularnie znajdował tematy.

**Wynik ruchu:**
1. wynik początkowy jednej metryki (punkt odniesienia na 30 dni),
2. 10 prawdziwych sygnałów od klientów,
3. 3 najmocniejsze tematy,
4. jeden temat startowy,
5. sposób ponownego uruchamiania radaru,
6. sekcja `WEJŚCIE DO RUCHU 02`, od której zacznie następny ruch.

## Etap A. Rozpoznanie (tylko do odczytu)

Niczego nie zapisuj. Przeczytaj:
- `dane/sklep.md` (oferta, produkty, ceny), `dane/klienci.md` (grupy klientów), `dane/marka.md` (ton, filary), `dane/uvp.md` (obietnica i dowody), `dane/marketing.md` (kanały, profile, statystyki),
- `wyniki/uvp/` (profil klienta: zadania, bóle, zyski), `wyniki/branding/` (opinie, konkurencja), `wyniki/seo/` (frazy i pytania z Google), `wyniki/meta-ads/` (reklamy i komentarze), `wyniki/black-week/`,
- `import/` i `dane/marka_z_importu.md` (dawne rozmowy),
- każdy plik z opiniami, wiadomościami, komentarzami, pytaniami klientów, eksportami (szukaj w folderze projektu słów: opinie, recenzje, pytania, komentarze, wiadomości, reklamacje, zwroty),
- `wyniki/social-media/`, jeśli istnieje (wtedy to kontynuacja, nie nowy system).

Pokaż właścicielowi krótko (najwyżej 12 linijek):
1. co już wiesz (oferta, odbiorcy, UVP) i skąd,
2. ile sygnałów od klientów jest już w projekcie i w jakich plikach,
3. czy system social media istnieje (`wyniki/social-media/`), czy go założysz,
4. **plan zmian**: jakie pliki powstaną albo zostaną uzupełnione (`README.md`, `dziennik.md`, `[DATA]_radar-tematow.md`, linia w `stan.md`),
5. prośba o jedno „OK” przed zapisem.

Jeśli w projekcie jest mało sygnałów od klientów, dodaj jedno zdanie: „Najlepsze tematy dają Twoi klienci. Jeśli możesz, wrzuć do folderu zrzuty kilku wiadomości, komentarzy albo opinii, albo wklej je tutaj. Jeśli nie, poszukam w źródłach publicznych.”

## Etap B. Oferta i odbiorcy

Wybierz **jedną** aktualną ofertę (produkt, kategoria albo kolekcja) i **jedną** grupę odbiorców. Kolejność źródeł: `dane/uvp.md` → `dane/klienci.md` → `dane/sklep.md` (bestsellery, marża, sezon). Uwzględnij sezon (listopad: Black Week i prezenty, sprawdź `wyniki/black-week/`).

Gdy dane nie rozstrzygają: jedna rekomendacja z uzasadnieniem i jedno pytanie („Proponuję zacząć od [oferta] dla [grupa], bo [powód]. Zgoda, czy wolisz inną ofertę?”).

## Etap C. Wynik początkowy (jedna metryka na 30 dni)

Wybierz jedną metrykę, którą właściciel **naprawdę może sprawdzić** dziś i za 30 dni. Kolejność preferencji:

| Metryka | Gdzie ją sprawdzić |
|---|---|
| Rozmowy: wiadomości prywatne i komentarze z pytaniem o produkt, zamówienie, rozmiar, dostawę (30 dni) | Instagram i Facebook: skrzynka wiadomości (Meta Business Suite → Skrzynka odbiorcza), policzenie ręczne |
| Kliknięcia w link z profilu albo z postów (30 dni) | Instagram: Profil → Panel profesjonalny → Statystyki → Interakcje (kliknięcia linku), Meta Business Suite → Statystyki |
| Sesje z social media w sklepie (30 dni) | Google Analytics 4: Raporty → Pozyskanie → Pozyskiwanie ruchu, kanał „Organic Social” |
| Zamówienia z kodu rabatowego dla obserwujących | panel sklepu, raport kodów rabatowych |
| Gdy nic z powyższych: zasięg albo wyświetlenia profilu (30 dni) | Statystyki Instagrama lub Facebooka (słabsza metryka: mówi o widoczności, nie o kliencie) |

Sprawdź najpierw `dane/marketing.md`. Jeśli liczby nie ma, poproś właściciela o odczyt (podaj dokładną ścieżkę kliknięć) albo zrzut ekranu. **Nigdy nie wpisuj zera, gdy stan jest nieznany.** Wtedy zapisz: `nieznany`, metodę pomiaru, datę pierwszego pomiaru i kto go zrobi. Zapisz też: wartość, okres (od–do), źródło, datę odczytu, datę ponownego pomiaru (+30 dni).

## Etap D. Przebieg radaru: dokładnie 10 sygnałów

**Sygnał** to prawdziwe pytanie albo problem klienta (obecnego albo potencjalnego), związany z wybraną ofertą i grupą odbiorców.

Kolejność:
1. **Najpierw własne źródła** z projektu (opinie, wiadomości, komentarze, pytania przed zakupem, zwroty i reklamacje, profil klienta z UVP, pytania z SEO). Własny klient to najmocniejszy dowód.
2. **Potem źródła publiczne**, jeśli masz wyszukiwanie: według `references/zrodla-sygnalow.md`. Otwórz stronę, zanim ją podasz jako źródło.

Każdy sygnał ma:
- **pytanie albo problem** słowami klienta (krótki dosłowny fragment, najwyżej 2 zdania, albo wiernie streszczony, oznaczony „streszczenie”),
- **źródło** (ścieżka pliku albo adres strony; przy danych klienta zanonimizowany opis),
- **datę** (data wypowiedzi; gdy nieznana: „data nieznana, odczyt [DATA]”),
- **dlaczego pasuje do oferty** (jedno zdanie: który produkt lub która cecha z UVP odpowiada na ten problem).

Zasady:
- Nie łącz kilku wypowiedzi w jeden wymyślony cytat. Podobne sygnały z różnych źródeł zapisz jako jeden sygnał z kilkoma źródłami (to podnosi ocenę dowodu).
- Sygnał nie musi dotyczyć sklepu wprost. Pytanie z forum „jak dobrać rozmiar bransoletki na prezent?” jest dobrym sygnałem dla sklepu z bransoletkami.
- Odrzuć: reklamy konkurencji udające pytania, wypowiedzi starsze niż 3 lata (chyba że temat jest ponadczasowy, wtedy zaznacz), treści z prywatnych grup bez zgody właściciela grupy.
- **Gdy nie da się znaleźć 10 prawdziwych sygnałów**, zapisz tyle, ile jest prawdziwych, a brakujące miejsca oznacz `DO ZEBRANIA` z podpowiedzią, gdzie je zebrać (np. „zapytaj 3 ostatnie klientki, co je powstrzymywało przed zakupem”). Nie dopełniaj listy wymysłami. Powiedz o tym właścicielowi.

## Etap E. Ocena 0–3

Każdy sygnał oceń w trzech kryteriach (suma 0–9). Każdą ocenę uzasadnij kilkoma słowami.

| Ocena | Siła problemu | Dopasowanie do oferty | Jakość dowodu |
|---|---|---|---|
| 0 | ciekawostka, nikt za nią nie zapłaci | oferta nie odpowiada na problem | przypuszczenie, brak źródła |
| 1 | drobna niewygoda | odpowiada pośrednio | jedna wypowiedź bez daty albo bardzo stara |
| 2 | realny kłopot, klient szuka rozwiązania | odpowiada wprost jeden produkt | prawdziwa wypowiedź ze źródłem i datą |
| 3 | boli, blokuje zakup albo wraca stale | oferta i UVP odpowiadają wprost, z dowodem | powtarza się w kilku niezależnych źródłach albo pochodzi od własnych klientów |

## Etap F. 3 tematy i temat startowy

1. **3 najmocniejsze tematy:** najwyższe sumy. Przy remisie wygrywa wyższa jakość dowodu, potem dopasowanie. Tematy muszą być różne (nie trzy warianty tego samego problemu; wtedy połącz je w jeden temat i weź następny).
2. Każdy temat zapisz jako **temat posta** jednym zdaniem z perspektywy klienta (np. „Jak dobrać bransoletkę na prezent, nie znając rozmiaru nadgarstka”) i dopisz: sygnały źródłowe, sumę ocen, jaki produkt lub dowód z UVP pasuje.
3. **Temat startowy:** jeden z trzech. Domyślnie najwyższa suma. Wybierz inny tylko z podanym powodem (np. własny dowód klientów, sezon, właściciel ma gotowe zdjęcia albo wiedzę, by o tym mówić od razu).

**Nie pisz posta**, nagłówków ani gotowych tekstów. To praca Ruchu 02.

## Etap G. Ponowne uruchomienie radaru

Zapisz w pliku radaru i w `wyniki/social-media/README.md`:
- **kiedy:** raz w tygodniu (np. w poniedziałek) i zawsze przed planem treści na nowy miesiąc albo akcję (Black Week, święta),
- **jak:** właściciel pisze „socialmedia: uruchom radar” i wrzuca nowe materiały (zrzuty wiadomości, komentarzy, opinii z ostatniego tygodnia) do folderu `wyniki/social-media/sygnaly/`,
- **co się dzieje:** asystent czyta nowe materiały i poprzedni radar, szuka nowych sygnałów (źródła publiczne z listy źródeł zapisanej w radarze), nie powtarza tematów już wykorzystanych, zapisuje nowy plik `[DATA]_radar-tematow.md`,
- **lista źródeł tego sklepu:** konkretne źródła użyte w tym przebiegu (adresy forów, sklepy konkurencji z opiniami, frazy w Google), żeby następny przebieg zaczął od nich.

Utwórz folder `wyniki/social-media/sygnaly/` (z krótkim plikiem `CO-TU-WRZUCAC.md`).

### Ponowne uruchomienie (gdy Ruch 01 już jest)

Przeczytaj poprzedni radar (sekcja „Źródła tego sklepu”, wykorzystane tematy) i nowe pliki w `sygnaly/`. Bez etapów B i C (chyba że minęło 30 dni: wtedy przypomnij o ponownym pomiarze metryki i zapisz wynik obok wyniku początkowego). Etapy D–F, plik z nową datą, porównanie: które tematy wracają (mocniejszy dowód), które są nowe.

## Etap H. Zapis (po „OK” z Etapu A)

Plik `wyniki/social-media/[DATA]_radar-tematow.md` według szablonu z `references/szablony.md`, z sekcjami:
1. Oferta i odbiorcy,
2. Wynik początkowy,
3. 10 sygnałów (tabela),
4. Ocena (tabela),
5. 3 tematy,
6. Temat startowy,
7. Jak uruchomić radar ponownie i źródła tego sklepu,
8. Kontrola jakości,
9. `WEJŚCIE DO RUCHU 02`: temat startowy (zdanie), jego sygnały i źródła (z cytatami), główna metryka z wynikiem początkowym, oferta i grupa odbiorców, otwarte pytania do właściciela.

Potem Krok 2 z `SKILL.md` (kontrola jakości, dziennik, README, `stan.md`).

## Podsumowanie dla właściciela

Pokaż:
1. wynik początkowy (wartość albo „nieznany” i jak zmierzymy),
2. 3 najlepsze tematy ze źródłami,
3. temat startowy i dlaczego,
4. dokładną ścieżkę zapisanego pliku,
5. wynik kontroli jakości,
6. jedno zdanie „Dowód ruchu” do wklejenia w społeczności, np.: „Ruch 01 gotowy: radar znalazł 10 sygnałów od klientów, zaczynam od tematu »[temat]«, punkt wyjścia: [metryka i wartość].”

Następny krok: „Jutro Ruch 02: zbierzemy prawdziwe słowa klientów o tym temacie i zobaczysz 3 sposoby, jak o tym napisać.”
