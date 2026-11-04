# Testy umiejętności Meta Ads

Każdy test w nowej rozmowie w `Test sklep`. Sprawdzasz zachowanie, nie liczby.

| # | Wiadomość | Oczekiwane zachowanie |
|---|---|---|
| 1 | „meta reklamy” (pierwszy raz) | Pyta o doświadczenie z reklamami Meta, zakłada `wyniki/meta-ads/README.md`, przechodzi do nowej kampanii, nie pyta o fakty z `dane/` |
| 2 | „Chcę reklamę bransoletek na Instagramie, 600 zł na 2 tygodnie” | Sam dobiera cel kampanii, mówi uczciwie, że ok. 43 zł dziennie to test działania, a nie kosztu sprzedaży, 1 grupa odbiorców i 2–3 reklamy, sprawdza stronę docelową |
| 3 | Akceptacja planu, potem „jak to ustawić?” | Instrukcja krok po kroku do Menedżera reklam, kampania wyłączona albo z przyszłą datą startu, osobna zgoda na start |
| 4 | „meta zasady: Masz problemy z cerą? Nasz krem usunie trądzik w 7 dni! -50%” | Pobiera aktualne zasady Meta, oznacza cechy osobowe i obietnicę zdrowotną, pyta o najniższą cenę z 30 dni, daje 3 bezpieczniejsze wersje |
| 5 | Eksport CSV z Menedżera reklam (kampania z budżetem Advantage+) + „wyłączyć Relacje, bo mają wyższy koszt zakupu?” | Ocena na poziomie kampanii, wyjaśnia efekt podziału, nie rekomenduje wyłączenia, najwyżej 3 działania jako testy z planem cofnięcia |
| 6 | „Zestaw jest w fazie uczenia od 3 dni, koszt zakupu 2× wyższy, zmienić budżet?” | Wyjaśnia fazę uczenia, odradza zmiany teraz, mówi, kiedy ocenić |
| 7 | „Audyt konta: czego brakuje w moich reklamach?” (kilka zrzutów) | Model konta, mapa trzech zadań (budzić zainteresowanie, budować rozważanie, domykać zakup), pewność niska przy zrzutach, bez zalecenia trzech kampanii |
| 8 | „wstrzymaj kampanię kolekcja-jesien” | Instrukcja wstrzymania bez dopytywania o zgodę, wpis w `decyzje.md`, etap `wstrzymana` w spisie i `stan.md` |

## Testy wiedzy Blue Mint (dodane 2026-11-04)

| # | Wiadomość | Oczekiwane zachowanie |
|---|---|---|
| 9 | „meta reklamy” przy pierwszej kampanii | Sprawdza fundamenty: piksel i CAPI, Max CPA i BE ROAS (kalkulator.blue-mint.pl albo wzór), profil IG, wykluczenie kupujących; zapisuje w README |
| 10 | „Koszyk 200 zł brutto, marża 40%, pakowanie 3 zł, wysyłka 8 zł, płatności 1,5%, zwroty 5%” | Liczy Max CPA i BE ROAS na netto, pokazuje wzór, przelicza ROAS z panelu na netto (/1,23) |
| 11 | Eksport: ROAS 3,1 w panelu, koszt zakupu 38 zł, Max CPA 45 zł, BE ROAS 2,8 | ROAS netto 2,52 poniżej progu, ale CPA pod Max CPA → strefa skaluj (sytuacja „niski koszyk”), nie wyłącza |
| 12 | „W Meta widzę 120 zakupów, w sklepie 95” | Błąd krytyczny (zdublowane zakupy), zatrzymuje ocenę rentowności, instrukcja testowania zdarzeń i deduplikacji |
| 13 | „Przygotuj reklamy do kampanii na bransoletki, 100 zł dziennie” | Komplet różnych konceptów (5 typów wg świadomości), formaty 4:5 i 9:16, brief z haczykiem, nie 10 wariacji jednej grafiki |
| 14 | „ROAS spadł z 9 na 4, odkąd dodałam tańszy produkt” | Wyjaśnia matematykę ceny, każe policzyć nowy BE ROAS i patrzeć na zysk w złotówkach, nie wyłącza |
