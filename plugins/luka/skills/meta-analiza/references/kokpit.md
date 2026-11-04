# Kokpit: układ kolumn w Menedżerze reklam

Źródło: praktyka Blue Mint (e-book Patryka Kamelskiego, 2026, rozdz. 3). Domyślne kolumny pokazują wynik, ale nie przyczynę. Ten układ pokazuje drogę od reklamy do zakupu. Tworzy się go raz.

## Jak zbudować

Menedżer reklam → **Kolumny** (nad tabelą, po prawej) → **Dostosuj kolumny** → usuń obecne → dodaj kolumny poniżej w tej kolejności → zapisz jako własny układ z nazwą (np. „Kokpit sklepu”). Zapisany układ znajdziesz też w „Wyświetl ustawienia domyślne kolumn”, gdy zniknie z ostatnio używanych.

**Wskaźnik niestandardowy:** w oknie Dostosuj kolumny → utwórz wskaźnik niestandardowy → nazwa, formuła (nazwy wskaźników i znaki + − × ÷), format (liczba, procent, waluta) → Utwórz.

## Kolumny

**Czas i status:** data utworzenia; ostatnia istotna zmiana (pokazuje, czy zestaw mógł wrócić do fazy uczenia); realizacja (status).

**Pieniądze i efektywność:**
- budżet; wydana kwota (np. pierwsza ocena nowego zestawu po wydaniu ok. 5× Max CPA); wyniki; koszt wyniku,
- obserwujący na Instagramie, gdy prowadzisz kampanie na profil; **koszt obserwacji** (niestandardowy: wydana kwota / obserwujący na Instagramie); **konwersja odwiedzin na obserwujących** (niestandardowy: obserwujący / unikatowe kliknięcia linku; orientacyjnie co najmniej 10%),
- ROAS z zakupów (łącznie, brutto); **ROAS netto** (niestandardowy: ROAS / 1,23 przy VAT 23%), porównywany z BE ROAS (`rentownosc.md`).

**Jakość ruchu:**
- CTR (wszystkie): czy reklama zatrzymuje (każde kliknięcie, także rozwinięcie opisu czy polubienie),
- CTR linku: czy kieruje do sklepu; orientacyjnie od ok. 2% dobrze, niżej popraw reklamę,
- CPC (kliknięcie linku): pomocniczy; tani ruch ze złej grupy nic nie daje,
- CPM: zatłoczenie aukcji. Nagły wzrost = więcej reklamodawców licytuje tę samą grupę (np. w listopadzie). Odpowiedź: nowe, angażujące reklamy, bo wysoki CTR obniża koszt wyświetleń,
- wyświetlenia strony docelowej i ich koszt: koszt dużo wyższy niż CPC = problem z wczytywaniem strony,
- wyświetlenia, zasięg, częstotliwość.

**Retencja wideo** (niestandardowe):
- 3-sekundowe odtworzenia = (współczynnik 3-sekundowych odtworzeń do wyświetleń / 100) × wyświetlenia; sam współczynnik mówi o sile haczyka,
- 3 s → 25% = odtworzenia do 25% / 3-sekundowe odtworzenia,
- 25% → 50% = odtworzenia do 50% / odtworzenia do 25%,
- 50% → 75%, 75% → 95%, 95% → 100% analogicznie.
Cel orientacyjny: ok. 65–75% na każdym etapie. Spadek w danym przedziale wskazuje słaby fragment filmu (początek = haczyk lub za długi wstęp, koniec = zakończenie). Porównuj filmy o podobnej długości. Decyduje jednak sprzedaż: film słabiej oglądany, ale sprzedający, poprawiaj, nie wyłączaj.

**Dowód społeczny:** komentarze, reakcje.

**Ścieżka zakupu:** dodania do koszyka, rozpoczęcia zakupu, dodania informacji o płatności, zakupy, koszt zakupu, wartość zakupów, średnia wartość zakupu (średni koszyk z reklam). Spadek między etapami pokazuje, gdzie klienci odpadają (np. dużo koszyków, mało zakupów = koszt dostawy, płatności, kasa).

Własne zdarzenia (np. zapis do newslettera, wypełnienie formularza) też można dodać jako kolumny.

## Jak używać w analizie

Gdy właściciel przysyła eksport, poproś o eksport z tym układem kolumn. Jeśli go nie ma, zaproponuj zbudowanie (10 minut) i przeprowadź krok po kroku. Wnioski czytaj od góry lejka: CTR i retencja (reklama) → wyświetlenia strony (ruch) → koszyk i kasa (sklep i oferta) → ROAS netto i koszt zakupu wobec progów (rentowność).
