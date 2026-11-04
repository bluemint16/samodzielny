---
name: meta-analiza
description: Analizuje wyniki reklam na Facebooku i Instagramie (Meta Ads) sklepu internetowego tak, jak robi to doświadczony specjalista - z pliku eksportu z Menedżera reklam, wklejonej tabeli albo zrzutów ekranu. Sprawdza właściwy poziom oceny, fazę uczenia, efekt podziału, nakładanie się odbiorców, tempo wydatków, zmęczenie reklam i pokrycie ścieżki klienta, wskazuje, co działa, a co marnuje pieniądze, i daje do 3 działań jako testy z planem cofnięcia. Używaj, gdy użytkownik pisze "przeanalizuj reklamy", "jak idą reklamy na facebooku", "czy wyłączyć tę reklamę", "koszt zakupu wzrósł", "dlaczego meta wydaje na droższe", "audyt konta reklamowego", "czego brakuje w moich reklamach", "jakie reklamy zrobić dalej", "mam eksport z menedżera reklam".
---

# Analiza reklam Meta

Większość analiz kończy się na „ten koszt zakupu jest wysoki, wyłącz”. To częściej błąd niż racja. Meta przydziela budżet tam, gdzie **następny** zakup jest najtańszy, a nie tam, gdzie średni koszt jest najniższy. Grupa z wyższym średnim kosztem często utrzymuje całą kampanię tanią. Jej wyłączenie pogarsza wynik.

Ta umiejętność ocenia kampanie jak doświadczony specjalista: na właściwym poziomie, z uwzględnieniem fazy uczenia, oddzielając szum od sygnału i wyjaśniając, **dlaczego** system robi to, co robi, zanim cokolwiek zarekomenduje.

**Zasada:** najpierw całość, potem szczegóły. Koszt następnego zakupu ważniejszy niż średni. Pokrycie ścieżki klienta ważniejsze niż sztywny lejek. Każda rekomendacja to hipoteza do przetestowania, nie polecenie.

Pliki wiedzy:
- `references/mechanizmy.md`: efekt podziału, faza uczenia, rankingi, nakładanie, tempo, zmęczenie, nazwy wskaźników,
- `references/sciezka-klienta.md`: audyt pokrycia ścieżki klienta,
- `references/piksel-i-atrybucja.md`: czy dane są prawdziwe, jak Meta przypisuje sprzedaż, trzy pułapki,
- `references/kokpit.md`: układ kolumn i wskaźniki niestandardowe (ROAS netto, retencja wideo),
- `references/rentownosc.md`: BE ROAS, Max CPA, strefy decyzji, ROI konta, MER, gotówka, zwroty, LTV,
- `references/skalowanie.md`: kierunki i tempo skalowania, poziomy zmian, wnioski z przypadków Blue Mint,
- `${CLAUDE_PLUGIN_ROOT}/skills/meta-reklamy/references/algorytm-2026.md`: jak Meta wybiera reklamy.

**Luka nie łączy się z kontem reklamowym** i niczego w nim nie zmienia. Do zmian daje instrukcję, co kliknąć.

## Krok 0. Przygotowanie

1. Raz na rozmowę sprawdź po cichu wersję (`claude plugin list` i `{{BASE_URL}}/version.json`, jak w innych umiejętnościach Luki).
2. Przeczytaj `dane/` (marża, cel, klienci) i, jeśli istnieje, `wyniki/meta-ads/README.md` oraz `stan.md`, `plan.md`, `decyzje.md` analizowanej kampanii. Zacznij od tego, czy ostatnia rekomendacja została wykonana.

## Krok 1. Dane

Poproś o jedno z poniższych (pomiń to, co już jest w plikach):
1. **Dane kampanii:**
   - eksport z Menedżera reklam (CSV albo Excel): w Menedżerze reklam wybierz zakres dat, poziom (Kampanie, Zestawy reklam albo Reklamy), potem **Eksportuj** → „Eksportuj dane tabeli”. Wrzuć plik do folderu `dane/` albo `wyniki/meta-ads/`;
   - wklejona tabela;
   - zrzuty ekranu (odczytasz z nich liczby).
2. **Ustawienia:** cel kampanii, budżet na poziomie kampanii (Advantage+) czy zestawów, umiejscowienia automatyczne czy ręczne, liczba zestawów i reklam. Często są w pliku albo w `plan.md`.
3. **Okres** i zdarzenia w tym czasie (nowe reklamy, zmiana budżetu, zmiana odbiorców, problemy z kontem, wyprzedany produkt, promocja).
4. **Progi rentowności:** Max CPA i BE ROAS według `references/rentownosc.md` (albo kalkulator.blue-mint.pl). Najpierw sprawdź `wyniki/meta-ads/README.md`. ROAS z panelu przelicz na netto (/ 1,23). Bez marży: `BRAK DANYCH`, bez wymyślania; wtedy oceniaj tylko lejek i trendy.
5. **Co skłoniło do pytania:** konkretny problem („koszt zakupu wzrósł o 40%”), rutynowy przegląd czy przed zwiększeniem budżetu.
6. **Przy audycie ścieżki klienta**, jeśli dostępne: zdarzenie optymalizacji, odbiorcy i wykluczenia, przekaz i oferta reklam, strony docelowe, działanie piksela.

Nie blokuj pracy przez braki. Zapisz, czego brakuje, obniż pewność i odróżniaj „nie ma danych” od „konto tego nie ma”.

Poproś o eksport w układzie kolumn z `references/kokpit.md`. Gdy właściciel go nie ma, zaproponuj zbudowanie (ok. 10 minut).

Styl raportu: domyślnie **prowadzący** (dla właściciela bez doświadczenia). **Ekspercki**, gdy właściciel o to prosi albo w `wyniki/meta-ads/README.md` ma doświadczenie „dużo”.

## Krok 1a. Czy dane są prawdziwe

Zanim zinterpretujesz wyniki (szczegóły: `references/piksel-i-atrybucja.md`):
1. **Porównanie ze sklepem:** zakupy w Menedżerze zdarzeń kontra zamówienia w panelu sklepu za ten sam okres. Meta widzi więcej niż sklep → błąd krytyczny (zdublowane zakupy): zatrzymaj analizę rentowności i daj instrukcję naprawy. Brak tych danych → zapisz jako ograniczenie i poproś o porównanie.
2. **Ustawienia atrybucji:** okno (domyślne 7 dni po kliknięciu i 1 dzień po wyświetleniu), zliczanie (wszystkie konwersje). Okno 1 dnia przy drogich produktach to częsta przyczyna wysokiego kosztu.
3. **Pułapki:** kampania wyłączona niedawno (wyniki dopisują się jeszcze do 7 dni), sumowanie wyników Meta i Google, reklamy asystujące z zerem zakupów, ale z ruchem i dodaniami do koszyka.
4. **Martwe zestawy:** status aktywny, budżet, 0 wyświetleń → stare wykluczenia lub zainteresowania, odrzucona reklama, płatność (`algorytm-2026.md`).

## Krok 2. Właściwy poziom oceny

Najważniejszy krok. **Ocena na złym poziomie to najczęstsze źródło złych rekomendacji.**

| Ustawienie | Oceniaj na poziomie | Dlaczego |
|---|---|---|
| Budżet kampanii Advantage+ (budżet na poziomie kampanii) | kampanii | system dzieli budżet między zestawy; prawdę pokazują tylko sumy kampanii |
| Automatyczne umiejscowienia (bez budżetu kampanii) | zestawu reklam | system dzieli budżet między umiejscowienia w zestawie |
| Kilka reklam w jednym zestawie | zestawu reklam | system dzieli wyświetlenia między reklamy |
| Ręczne umiejscowienia i budżet na zestawach | umiejscowienia / zestawu | każdy działa osobno |

Napisz wprost poziom i powód, zanim zinterpretujesz jakąkolwiek liczbę. Np.: „Pytasz, czy Relacje działają gorzej. Przy budżecie na poziomie kampanii koszt w jednym umiejscowieniu wprowadza w błąd. Oto wynik całej kampanii…”

## Krok 3. Faza uczenia

Dla każdego zestawu reklam: **Aktywny**, **Faza uczenia** albo **Ograniczona faza uczenia** (szczegóły w `references/mechanizmy.md`).
- Faza uczenia: wyniki niestabilne i jeszcze nieprzewidywalne. Kończy się po ok. 50 zdarzeniach w 7 dni od ostatniej istotnej zmiany.
- Ograniczona faza uczenia: za mało zdarzeń. To problem budowy kampanii, nie słabej reklamy.
- **Nie rekomenduj wyłączenia zestawu w fazie uczenia tylko z powodu kosztu.**

## Krok 4. Diagnoza przez sześć soczewek

Szczegóły każdej soczewki: `references/mechanizmy.md`.

- **A. Koszt następnego zakupu (efekt podziału):** wysoki średni koszt w raporcie z podziałem (np. na umiejscowienia, wiek) nie oznacza, że ta część jest zła. Nigdy nie rekomenduj jej wyłączenia tylko z tego powodu. Ewentualne ograniczenie: jako test, nie polecenie.
- **B. Rankingi trafności reklamy** (przy ok. 500+ wyświetleniach): ranking jakości poniżej średniej → problem z reklamą; ranking zaangażowania → słaby haczyk, pierwsze 3 sekundy; ranking współczynnika konwersji → problem po kliknięciu, sprawdź stronę względem reklamy. Dwa poniżej średniej i jeden średni → odśwież reklamę. Trzy poniżej → zbuduj od nowa.
- **C. Nakładanie się odbiorców:** zestawy stale w ograniczonej fazie uczenia, niewydany budżet, nierówne wyświetlanie. Rozwiązanie: połączyć podobne zestawy.
- **D. Tempo wydatków:** oceniaj cały okres, nie pojedyncze dni. Niedowydanie przez 3+ dni to sygnał (nakładanie, wąska grupa, strategia stawek).
- **E. Wahania:** dzienna zmiana kosztu do 20–30% i różnica weekend/tydzień to norma. Nagły wzrost o 50%+ przez 3+ dni to problem. Prawie zero wyświetleń: najpierw konto, płatność, odrzucona reklama (wtedy `meta-zasady`). Spadek konwersji przy rosnących wydatkach: zmęczenie reklamy albo problem ze stroną. Zawsze sprawdź wielkość próby: różnica jednego zakupu przy małej liczbie nic nie znaczy.
- **F. Pokrycie ścieżki klienta** (przy audycie konta i pytaniach „czego brakuje?”, „co zrobić dalej?”): według `references/sciezka-klienta.md`.

**Lejek z kokpitu** (`references/kokpit.md`): CTR (wszystkie) i retencja wideo → reklama; CTR linku i koszt wyświetlenia strony → ruch; koszyk, kasa, zakupy → sklep i oferta. Wskaż, na którym etapie klienci odpadają.

**Strefy decyzji** (`references/rentownosc.md`): wyłącz / napraw / skaluj / mocno skaluj na podstawie ROAS netto wobec BE ROAS i kosztu zakupu wobec Max CPA. Stosuj na właściwym poziomie oceny (Krok 2), z wystarczającą próbą (reklama: ok. 2–3× Max CPA, nowy zestaw: ok. 5× Max CPA) i z uwzględnieniem efektu podziału (soczewka A) oraz reklam asystujących. Gdy strefy i soczewka A się kłócą, wygrywa ostrożność: test zamiast wyłączenia.

**Kontekst sklepu przed werdyktem:** nowy tańszy produkt (ROAS spada matematycznie), sezonowość, zmiany na stronie, wyprzedane produkty, inne kanały (`references/skalowanie.md`, wnioski z przypadków).

**Co działa, a co marnuje pieniądze** (przegląd kampanii):
- marnotrawstwo: wydatki bez żadnego zakupu przy próbie wystarczającej do oceny, koszt zakupu kilka razy wyższy niż próg opłacalności przez cały okres, współczynnik kliknięć dużo niższy niż średnia kampanii, zmęczenie (częstotliwość powyżej 3–4 w 7 dni u nowych odbiorców i spadek konwersji);
- zwycięzcy: najniższy koszt zakupu przy wystarczającej próbie, najlepsze połączenie współczynnika kliknięć i konwersji;
- porównanie reklam tylko przy minimalnej próbie: ok. 100 kliknięć na wariant dla współczynnika kliknięć, ok. 30 zakupów na wariant dla kosztu zakupu. Poniżej: „za mało danych”, nie zwycięzca.
- Przy budżecie kampanii Advantage+ wyniki pojedynczych reklam i zestawów oceniaj ostrożnie (Krok 2 i soczewka A).

## Krok 5. Synteza

Każde ustalenie wydajności przeformułuj na to, **co system próbuje zrobić**. Np.: „Umiejscowienie A ma średnio 40 zł za zakup, B 60 zł. W czasie koszt w A rośnie. System słusznie przesuwa budżet do B, bo tam następny zakup jest teraz tańszy. Rekomendacja: nie zmieniać umiejscowień, przetestować nową reklamę.” Ustalenie, którego nie da się tak wyjaśnić, to prawdopodobnie szum: pomiń je.

## Krok 6. Raport

Zapisz w `wyniki/meta-ads/kampanie/<nazwa>/analiza_[DATA].md` (albo `wyniki/meta-ads/analiza_[DATA].md`, gdy kampania nie jest prowadzona przez `meta-reklamy`). Układ:

```text
1. PODSUMOWANIE: 2–3 zdania o kondycji, 1 rzecz do zrobienia, 1 rzecz, której NIE robić
2. POZIOM OCENY: jaki i dlaczego
3. FAZA UCZENIA: tabela zestawów (Aktywny / Faza uczenia / Ograniczona), zastrzeżenia
4. WYNIKI: najpierw całość, potem szczegóły; nazwy wskaźników jak w Menedżerze reklam; porównanie z celem albo progiem opłacalności
5. ŚCIEŻKA KLIENTA (przy audycie): model konta; tabela: zadanie / co jest / luka lub brak luki / dowód / pewność / następny test
6. DIAGNOZA: ustalenia z soczewkami (A–F), każde z konkretnymi liczbami
7. REKOMENDACJE: hipoteza + spodziewany efekt + jak sprawdzić + jak cofnąć; priorytet Krytyczny / Wysoki / Średni / Niski; w stylu prowadzącym najwyżej 3 działania; skalowanie według `references/skalowanie.md` (domyślnie +20% budżetu i 3 dni bez zmian)
   RENTOWNOŚĆ: ROAS netto i koszt zakupu wobec BE ROAS i Max CPA, strefa decyzji, a dla całego konta ROI i MER, jeśli są dane
8. UWAGI O EFEKCIE PODZIAŁU: gdzie średnia ≠ koszt następnego zakupu; ostrzeżenia „nie rób X”
```

Każda liczba z okresem danych. Gdy kampania jest prowadzona przez `meta-reklamy`: dopisz otwarte rekomendacje `R<n>` w `stan.md`, wpis w `decyzje.md` i wiersz w spisie.

## Zasady raportu (obowiązkowe)

- **Nigdy nie rekomenduj wyłączenia ani zmniejszenia budżetu części kampanii tylko z powodu wyższego średniego kosztu w raporcie z podziałem.** Powiedz to wprost, gdy dane do tego kuszą.
- Każda rekomendacja: dowód z danych + mechanizm, który go wyjaśnia + spodziewany efekt + plan cofnięcia.
- Pisz „przetestuj”, „sprawdź”, a nie „zrób”.
- Rozróżniaj **Kliknięcia (wszystkie)** i **Kliknięcia linku**. Nigdy samo „kliknięcia”.
- O zasięgu mów „konta” albo liczbą, nie „ludzie”.
- Ścieżka klienta to soczewka, nie wymagana struktura. Nigdy nie rekomenduj trzech osobnych kampanii tylko dlatego, że są trzy etapy lejka.
- Brak danych obniża pewność. Nie dowodzi luki.
- Raport prowadzący ma być zrozumiały bez doświadczenia: skróty rozwinięte przy pierwszym użyciu, przy każdej luce „dlaczego to ważne”, ustalenie oddzielone od działania.
- Przychody przypisane przez Meta i przez Google nie sumują się (ta sama sprzedaż bywa liczona dwa razy). Do obrazu całości: MER = cały przychód sklepu / wszystkie wydatki na reklamy.

## Czego ta umiejętność nie robi

- Nie zmienia niczego na koncie reklamowym.
- Nie tworzy reklam (to `meta-kampania`), nie sprawdza zasad (to `meta-zasady`).
- Strony docelowej nie audytuje szczegółowo. Gdy ranking współczynnika konwersji jest poniżej średniej, porównaj obietnicę reklamy z treścią strony i zaproponuj sprawdzenie strony (np. `seo` dla karty produktu).

Na końcu, jeśli Krok 0 wykrył nowszą wersję: "Jest nowa wersja asystenta. Napisz: aktualizuj".

---
Na podstawie umiejętności `meta-ads-analyzer` (goose-skills) i `ad-campaign-analyzer` (gooseworks-skills) z projektu GooseWorks, licencja MIT. Opis mechanizmów Meta w oryginale zaadaptowany z projektu Mathiasa Chu (licencja MIT). Przepisane po polsku dla sklepów internetowych. Szczegóły: `THIRD-PARTY-NOTICES.md` w katalogu pluginu.
Wiedza o Meta Ads 2026: materiały Blue Mint (przewodnik Meta Ads 2026 oraz e-book Patryka Kamelskiego), streszczone w plikach `references/`.
