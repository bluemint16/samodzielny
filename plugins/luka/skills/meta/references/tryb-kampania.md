# Kampania Meta: od celu do gotowej instrukcji

> Tryb umiejętności `meta`. Czytasz go, gdy przewodnik (`SKILL.md`) skierował tu właściciela. Wersja, `dane/` i spis kampanii są już przeczytane: nie powtarzaj tego i nie pytaj o zapisane fakty. Prowadź według zasad „za rękę” z `SKILL.md`: jeden krok naraz, potwierdzenie „zrobione?”, na końcu wróć do przewodnika (Krok 5 i Zakończenie).

Właściciel mówi „chcę więcej sprzedaży z Instagrama”. Nie musi wiedzieć, czym jest cel kampanii, zestaw reklam ani piksel, i nie wybiera ich sam. Opowiada o sklepie, a Ty robisz resztę i tłumaczysz ją jego słowami.

**Luka nie łączy się z kontem reklamowym.** Efektem jest plan i instrukcja „co kliknąć”, a kampanię tworzy i włącza właściciel. Wszystko zapisujesz w folderze kampanii `wyniki/meta-ads/kampanie/<nazwa>/` (pliki według `references/szablony.md`).

Pliki wiedzy:
- `references/plan-i-ustawienie.md`: słownik, za co płacimy, budżet, limity tekstu, plan, instrukcja do Menedżera reklam,
- `references/struktury.md`: struktury kampanii (dwie szkoły, dobór do budżetu),
- `references/kreacje.md`: budowa reklamy, komplet 5 typów wg poziomów świadomości, wariacja a nowy koncept, formaty, testy,
- `references/algorytm-2026.md`: jak Meta wybiera reklamy,
- `references/rentownosc.md` i `piksel-i-atrybucja.md`: progi rentowności i sprawdzenie piksela.

## Jak mówić

Mów o sklepie, nie o ustawieniach Meta. Słownik tłumaczeń jest w pliku referencyjnym. Trzy zasady:
- **Każda kampania to test**, nie „reklamy już działają”. Przed wydaniem pieniędzy powiedz, na jakie pytanie ten budżet odpowie, a na jakie nie.
- **Nie mów, że reklama działa, dopóki Meta jej nie zaakceptowała i właściciel jej nie włączył.**
- **Błędy Meta tłumacz** na to, co się stało i co dalej.

## Krok 0

Jeśli kampania jest już w toku, kontynuuj ją od jej etapu (`stan.md`), zamiast zaczynać od nowa. Mapa etapów: `wywiad`/`plan` → Etap 1–5 (plan), `reklamy` → Etap 5 pkt 2, `ustawienie` → Etap 5 pkt 3–4, `działa` → Etap 7.

## Etap 1. Cel

Zacznij od celu, nie od ustawień. Nigdy nie każ właścicielowi wybierać celu kampanii, typu budżetu ani struktury. Zapytaj (pomiń to, co już wiesz z plików):

1. **Cel:** co mają dać te pieniądze? Sprzedaż, zapisy do newslettera, ruch na stronie, rozpoznawalność, albo „chcę sprawdzić, czy to w ogóle działa”.
2. **Oferta:** co reklamujemy i co dokładnie dostaje klient? Które produkty?
3. **Odbiorcy:** dla kogo i gdzie (cała Polska, miasto, kraje)?
4. **Budżet i czas:** ile łącznie i jak długo (np. „1 500 zł przez 2 tygodnie”). Gdy ktoś poda kwotę dzienną, dopytaj o całość i czas.

W drugiej kolejce:

5. **Miara sukcesu:** jaki wynik uznamy za dobry? Policz progi: **Max CPA** i **BE ROAS** według `rentownosc.md` (albo kalkulator.blue-mint.pl). Potrzebne: średni koszyk, marża, koszty na zamówienie, prowizja płatności, odsetek zwrotów. Sprawdź najpierw `wyniki/meta-ads/README.md`, `wyniki/black-week/2_oferta.md` i `dane/`. Bez marży: `BRAK DANYCH` i plan jako test działania, bez celu kosztu zakupu.
6. **Strona docelowa:** dokąd ma trafić klient po kliknięciu?

Gdy czegoś brakuje, wyjaśnij jednym zdaniem, po co to potrzebne. Brak odpowiedzi to „nie”, a nie „tak”. Gdy właściciel nie wie, zapisz założenie w sekcji „Czego nie wiemy”.

**Ustal, co wolno powiedzieć w reklamie.** Co produkt robi naprawdę, jakie obietnice są dozwolone, czy jest prawdziwa opinia lub wynik do zacytowania (domyślnie: brak). Każdą liczbę i cenę sprawdź na stronie sklepu. Rabat podawaj tylko z najniższą ceną z 30 dni przed obniżką (zasady UOKiK obejmują też reklamy).

## Etap 2. Resztę ustal sam

Zapytaj właściciela o trzy rzeczy, które sprawdzi w Menedżerze reklam (albo przyjmij założenie):
- czy konto reklamowe już kiedyś wydawało pieniądze (nowe konto = większe wahania),
- czy na stronie sklepu działa piksel Meta i ile zakupów tygodniowo widzi (w Menedżerze zdarzeń; wiele platform sklepowych ma gotową integrację z Meta),
- czy sklep ma katalog produktów w Meta (potrzebny do reklam katalogowych).

Z tych odpowiedzi wybierz, za co płacimy (tabela w pliku referencyjnym):
- około 50 zakupów tygodniowo i więcej → płacimy za zakupy,
- mniej, ale piksel działa → płacimy za wyświetlenia strony docelowej („za osoby, które naprawdę weszły na stronę”), a po 2–3 tygodniach przechodzimy na zakupy, gdy będzie ich więcej,
- brak piksela → płacimy za kliknięcia i najpierw naprawiamy piksel.

**Uczciwie oceń budżet** (tabela w pliku referencyjnym) i powiedz to w Etapie 4. Mały budżet sprawdza, czy wszystko działa, a nie, ile kosztuje sprzedaż.

**Struktura wynika z budżetu.** Dobierz ją według tabeli „Dobór struktury” w `references/struktury.md`. Przy małym budżecie: jedna kampania Sprzedaż, jeden szeroki zestaw, kilka naprawdę różnych reklam. Dzielenie małego budżetu na wiele grup odbiorców głodzi każdą z nich. Remarketing katalogowy, gdy działają katalog i piksel, a ruch na stronie to uzasadnia. Minimum orientacyjne: ok. 30 zł dziennie na zestaw reklam.

**Zawsze wykluczaj ostatnich kupujących** (lista klientów albo kupujący z piksela z 30–180 dni) w kampaniach do nowych klientów: to jedyne twarde ustawienie, które realnie chroni budżet. Wiek, płeć i zainteresowania są dla Meta tylko podpowiedzią (`algorytm-2026.md`).

**Przy koncie z historią** sprawdź stare zestawy z wąskimi zainteresowaniami: część może być „Aktywna” z budżetem, ale bez wyświetleń.

## Etap 3. Sprawdzenie przed akceptacją

Najpierw **piksel**: jeśli kampania ma płacić za zakupy, przeprowadź z właścicielem Test 1 z `piksel-i-atrybucja.md` (testowanie zdarzeń: wartość, waluta PLN, deduplikacja). Zakupy zdublowane albo niewidoczne blokują start kampanii sprzedażowej.

Potem cztery sprawdzenia. Każdy problem opisz w tym samym układzie (szablon „Problem” w pliku referencyjnym): co jest nie tak, dlaczego to ważne, czy blokuje start, co zrobi Luka, co musi zrobić właściciel. Nie łącz dwóch ostatnich punktów.

1. **Strona docelowa.** Otwórz ją i obejrzyj: czy działa, czy przekierowania prowadzą tam, gdzie trzeba, czy kontynuuje obietnicę reklamy, czy jest jedno oczywiste działanie (np. „Do koszyka”), czy cena i dostawa są jasne. Nie wysyłaj płatnego ruchu na ogólną stronę główną, gdy jest lepsza strona produktu lub kategorii.
2. **Konto i płatność.** Właściciel potwierdza, że konto reklamowe jest aktywne i ma podpiętą kartę. Bez karty reklamy się nie wyświetlą, choć wyglądają na gotowe.
3. **Pod jakim profilem.** Strona na Facebooku i połączony Instagram sklepu, a nie prywatny czy porzucony profil. Klienci sprawdzają profil przed zakupem: profil bez aktywności od miesięcy obniża sprzedaż nawet przy dobrej reklamie.
4. **Reklamy.** Każda obietnica ma pokrycie, tekst mieści się w limitach (tabela w pliku referencyjnym), nic nie łamie zasad Meta. Sprawdź każdą reklamę przed akceptacją według `references/tryb-zasady.md`.

Gdy wszystko jest dobrze, powiedz to jednym zdaniem. Nie wymyślaj problemów.

## Etap 4. Projekt testu

Przed wydaniem pieniędzy powiedz prosto:
1. **Co sprawdzamy** (pytanie, np. „czy klientki bardziej przekonuje ręczne wykonanie, czy gotowy prezent?”). „Uruchamiamy kampanię” to nie test.
2. **Dlaczego warto** (co zmieni się zależnie od wyniku).
3. **Jedna różnica między reklamami.** Tylko jedna, inaczej nie wiadomo, co zadziałało.
4. **Podział budżetu** (zwykle wszystkie reklamy w jednej grupie, Meta sama przesuwa wyświetlenia).
5. **Która liczba wyłoni zwycięzcę** (ustalona z góry).
6. **Ile danych potrzeba** (np. „każda reklama co najmniej 1 000 wyświetleń i 30 wejść na stronę, przy tym budżecie około 6 dni”).

I powiedz wprost: „Nie ogłoszę zwycięzcy za wcześnie. Po dwóch dniach prowadząca reklama zwykle prowadzi przypadkiem.”

Przed startem oceń każdą reklamę oczami odbiorcy: czy zatrzyma kciuk, czy mówi do celu, czy strona dotrzymuje obietnicy. Poprawiaj, aż będzie warta pieniędzy. Nie zakładaj testu A/B Meta: przy małym budżecie potrzebuje zbyt dużo pieniędzy.

## Etap 5. Plan i dwie zgody

Pokaż krótki plan w 9 częściach (szablon w pliku referencyjnym): cel, odbiorcy, budżet, terminy, strona docelowa, co liczymy, reklamy, plan testu, **czego nie wiemy** (ta sekcja nigdy nie jest pusta tylko dlatego, że lepiej wygląda).

1. **Zgoda na plan.** Właściciel akceptuje plan. Zmiana planu = ponowna akceptacja. Zapisz `plan.md`, wpis w `decyzje.md`, etap `reklamy` albo `ustawienie`.
2. **Reklamy.** Według `references/kreacje.md`: komplet naprawdę różnych konceptów (5 typów wg poziomów świadomości, ile ich zależy od budżetu), każdy zbudowany jako haczyk → kąt → mechanizm → dowód → efekt → wezwanie, w formatach 4:5 i 9:16. Teksty w tonie z `dane/marka.md`, z UVP z `dane/uvp.md`. Dla każdej reklamy brief (szablon na końcu `kreacje.md`), także instrukcja nagrania wideo telefonem, jeśli właściciel nagrywa sam. Po sprawdzeniu zasad (`references/tryb-zasady.md`) i akceptacji właściciela etap `ustawienie`.
3. **Instrukcja ustawienia.** Krok po kroku do Menedżera reklam według listy w pliku referencyjnym. Kampania powstaje **wyłączona** albo z datą startu w przyszłości, żeby Meta mogła sprawdzić reklamy, zanim cokolwiek wyda.
4. **Zgoda na start.** Osobna, wyraźna decyzja właściciela: włącza kampanię sam. Przypomnij: „Od tej chwili kampania wydaje prawdziwe pieniądze, najwyżej [kwota], i sama się zatrzyma [data]. Wstrzymasz ją jednym przełącznikiem w każdej chwili.”
5. Gdy właściciel potwierdzi, że reklamy są zaakceptowane i włączone: etap `działa`. Gdy któraś jest odrzucona: tryb Zasady (`references/tryb-zasady.md`) z treścią odrzucenia.

## Etap 6. Zatrzymanie jest zawsze proste

„Wstrzymaj reklamę” albo „zatrzymaj kampanię” działa zawsze, bez planu i zgody. Daj instrukcję (przełącznik przy kampanii lub reklamie w Menedżerze reklam) i zapisz decyzję.

## Etap 7. Uczciwe wnioski

Pierwsze wyniki oceniaj tym, na co budżet mógł odpowiedzieć: czy reklamy przeszły weryfikację, czy wejścia na stronę idą w parze z kliknięciami (duża różnica = problem ze stroną albo pikselem), czy współczynnik kliknięć jest wiarygodny. **Nie podawaj kosztu sprzedaży z budżetu, który nie mógł go zmierzyć.** Do pełnej analizy przejdź do trybu Analiza (`references/tryb-analiza.md`).

Na końcu: co się zmieniło, co działa, co marnuje pieniądze, jeden następny krok do akceptacji. Zakończ według `SKILL.md` (zapis zmian i jeden następny krok).

---
Na podstawie umiejętności `launch-meta-ad-campaign` (goose-skills) i `meta-ads-campaign-builder` (gooseworks-skills) z projektu GooseWorks, licencja MIT. Przepisane po polsku, bez łączenia z kontem reklamowym. Szczegóły: `THIRD-PARTY-NOTICES.md` w katalogu pluginu.
Wiedza o Meta Ads 2026: materiały Blue Mint (przewodnik Meta Ads 2026 oraz e-book Patryka Kamelskiego), streszczone w plikach `references/`.
