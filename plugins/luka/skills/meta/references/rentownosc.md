# Rentowność reklam: zysk ważniejszy niż wskaźniki

Źródła: praktyka Blue Mint (e-book Patryka Kamelskiego, 2026, rozdz. 5) i przewodnik Meta Ads 2026 (Blue Mint). Wszystkie przykłady liczbowe to ilustracje, nie normy rynkowe.

## Faktur nie płaci się ROAS-em

| | Wydatki | Przychód | ROAS | Zysk przy marży 30% |
|---|---|---|---|---|
| A | 1 000 zł | 10 000 zł | 10 | 3 000 zł |
| B | 50 000 zł | 150 000 zł | 3 | 45 000 zł |

Wraz ze wzrostem budżetu ROAS zwykle spada. To naturalne. Pilnujemy, żeby nie spadł poniżej progu rentowności. ROAS zależy też od ceny produktu: ROAS 10 przy meblach za 5 000 zł to 500 zł na klienta, przy etui za 50 zł to 5 zł na klienta. **Nie porównuj swojego ROAS z cudzym.**

## Dwie czerwone linie: BE ROAS i Max CPA

Do wyliczenia: kalkulator Blue Mint **kalkulator.blue-mint.pl** albo wzory poniżej. Dane od właściciela: średni koszyk brutto, stawka VAT, marża produktowa netto (%), koszty na zamówienie netto (opakowanie, część wysyłki pokrywana przez sklep), prowizja płatności (%), odsetek zwrotów.

Wzory (na kwotach netto, VAT 23% jako przykład):
- średni koszyk netto = koszyk brutto / 1,23
- **Max CPA** (ile najwyżej zapłacić za jedno zamówienie, żeby wyjść na zero) = koszyk netto × marża % − opakowanie − wysyłka po stronie sklepu − prowizja płatności (koszyk brutto × %) − koszt zwrotów (np. odsetek zwrotów × (marża utracona + koszty wysyłek zwrotnych))
- **BE ROAS** (próg rentowności na przychodzie netto) = koszyk netto / Max CPA
- **ROAS netto** z panelu = ROAS z panelu / 1,23 (panel liczy przychód z VAT)

Porównanie: ROAS netto = BE ROAS → na zero; wyżej → zarabiasz. Koszt zakupu z panelu poniżej Max CPA → zarabiasz.

**Oba wskaźniki razem:** ROAS pilnuje wartości koszyka (ważny przy produktach w różnych cenach), CPA pilnuje kosztu klienta (ważny przy skalowaniu). Niski ROAS przy tanim CPA (ktoś kupił tańszy produkt) nadal może być zyskiem. Gdy sklep ma bardzo różne produkty, licz próg dla średniej całego konta albo osobno dla głównych linii.

W BE ROAS nie ma kosztów stałych (pensje, agencja, narzędzia). Pełny obraz daje ROI.

## Strefy decyzji (przykład: BE ROAS 2,5, Max CPA 45 zł)

| Strefa | Warunek | Decyzja |
|---|---|---|
| **Wyłącz (KILL)** | ROAS netto poniżej progu **i** CPA powyżej Max CPA | wyłącz albo pilna naprawa; jeśli po naprawie nie wraca do normy, wyłącz |
| **Napraw (FIX)** | ROAS netto tuż pod progiem (np. 2,0–2,4) **lub** CPA lekko ponad limit (np. 45–55 zł) | nie wyłączaj, bo system zebrał już dane. Po zmianie daj wydać jeszcze ok. 3× CPA; brak poprawy → wyłącz. Niski CTR → nowy haczyk albo nagłówek. Wysoki CTR bez sprzedaży → oferta albo sklep (szybkość, koszyk, płatności, cena, koszt dostawy) |
| **Skaluj (SCALE)** | ROAS netto powyżej progu **lub** CPA poniżej Max CPA | zarabiasz; dopóki jeden z nich trzyma w strefie zysku, skaluj (`skalowanie.md`) |
| **Mocno skaluj** | ROAS netto wyraźnie powyżej progu **i** CPA wyraźnie poniżej (np. ROAS 4, CPA 30 zł) | duży zapas, zwiększaj budżet i dokładaj nowe reklamy |

**Zastrzeżenia, zawsze:**
- strefy stosuj na właściwym poziomie oceny i z wystarczającą próbą (`references/tryb-analiza.md`, Krok 2–3): pierwsze wnioski o reklamie po wydaniu ok. 2–3× Max CPA, o nowym zestawie ok. 5× Max CPA,
- nie wyłączaj części kampanii z budżetem Advantage+ tylko przez wyższy średni koszt (efekt podziału, `mechanizmy.md`),
- reklama „asystująca” może mieć mało zakupów, a pracować na sprzedaż (`piksel-i-atrybucja.md`).

## ROI całego konta Meta

1. Dostępna marża = przychód netto z Meta (wiersz podsumowania / 1,23) / BE ROAS.
2. Czysty zysk = dostępna marża − wszystkie wydatki na Meta (wszystkie kampanie) − koszt obsługi (agencja, freelancer; opcjonalnie pensje).
3. ROI = czysty zysk / (wydatki na Meta + koszt obsługi) × 100%.

Przykład: BE ROAS 4,83, przychód netto 150 000 zł, wydatki 21 000 zł, agencja 5 000 zł → marża 31 056 zł, zysk 5 056 zł, ROI ok. 19%. Zawsze patrz też na zysk w złotówkach: ROI 20% przy 100 000 zł wydatków to więcej pieniędzy niż ROI 100% przy 5 000 zł.

## Wskaźniki całego sklepu

- **MER:** dwie konwencje, zawsze napisz, której używasz:
  - przychód sklepu / wszystkie wydatki marketingowe (np. 7 = 7 zł przychodu z 1 zł),
  - wydatki marketingowe / przychód sklepu × 100% (przewodnik 2026 podaje jako zdrowy poziom ok. 12–15% przychodu; to orientacja, zależy od marży).
- **Blended CAC** = wszystkie wydatki marketingowe / liczba nowych klientów.
- **LTV / CAC:** wartość klienta (np. z 12 miesięcy) do kosztu pozyskania. Przy wysokim LTV można pozyskiwać klientów „na zero” na pierwszym zakupie, ale tylko z zapasem gotówki.
- ROAS z panelu jest wskaźnikiem pomocniczym (okna atrybucji się nakładają). Decyzje o budżecie całego sklepu: MER i Blended CAC.

## Gotówka i model sklepu

- **Własny magazyn:** wynik „na zero” to pułapka: odzyskujesz wkład, ale nie masz na kolejną dostawę. Potrzebna nadwyżka.
- **Dropshipping:** niskie marże, więc wysoki ROAS i tanie CPA są konieczne.
- **Produkty cyfrowe:** można świadomie pozyskiwać klientów na progu i zarabiać na kolejnych sprzedażach albo od razu celować w wysoki ROAS.
- **Płatność za pobraniem, odroczone płatności:** Meta pobiera opłaty od razu, pieniądze wracają po dniach. Zadbaj o płynność przed agresywnym skalowaniem.
- **Zwroty:** panel ich nie widzi. Przy 30% zwrotów (np. moda, obuwie) ROAS 5 w panelu to realnie ok. 3,5. Zwroty muszą być w BE ROAS.

## Efekt skali

Przy kosztach stałych nawet niski, ale dodatni wynik zarabia przy dużej liczbie sprzedaży, bo koszty stałe się rozmywają. Mały budżet (np. 10 zł dziennie) może nigdy nie pokryć kosztów stałych, nawet przy dobrej reklamie. Przy słabym wyniku są dwie racjonalne drogi: poprawić reklamy i ofertę albo, gdy wynik jest nad progiem, świadomie skalować. Zawsze w granicach BE ROAS i Max CPA.

## Hierarchia naprawy wyników (przewodnik 2026)

1. wyższy średni koszyk i marża, 2. dosprzedaż i powroty klientów, 3. różnorodność reklam, 4. dopiero ustawienia w Menedżerze reklam.
