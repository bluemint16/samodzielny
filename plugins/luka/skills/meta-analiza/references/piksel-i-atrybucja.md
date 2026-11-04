# Piksel i atrybucja: czy liczbom w panelu można ufać

Źródło: praktyka Blue Mint (e-book Patryka Kamelskiego, 2026, rozdz. 1–2). Nazwy w Menedżerze zdarzeń i Menedżerze reklam mogą się zmieniać: gdy właściciel nie widzi opisanego miejsca, poproś o zrzut ekranu.

**Zasada:** zanim ocenisz wyniki, sprawdź dane. Gdy sklep wysyła dwa zakupy zamiast jednego, wyniki są zawyżone i sklep „zarabia” tylko w panelu. Gdy piksel gubi połowę zakupów, łatwo wyłączyć dochodowe reklamy.

## Test 1. Testowanie zdarzeń (najbardziej wiarygodny)

Menedżer zdarzeń (Wszystkie narzędzia) → piksel (zestaw danych) → **Testowanie zdarzeń** → Witryna internetowa → adres sklepu → otwórz stronę i zachowuj się jak klient:
1. strona główna → zdarzenie **PageView**,
2. karta produktu → **ViewContent**,
3. dodanie do koszyka → **AddToCart**,
4. przejście do kasy → **InitiateCheckout**,
5. zakup (produkt testowy za 1 zł albo kod -100%) → **Purchase**.

W zdarzeniu Purchase sprawdź:
- **wartość:** zgadza się z koszykiem? Najlepiej sama wartość towaru, bez dostawy;
- **walutę:** PLN, a nie USD czy EUR (częsty błąd: sklep wysyła „100”, a Meta przyjmuje inną walutę);
- **deduplikację:** przy pikselu i Conversions API (CAPI) widać dwa zdarzenia, ale jedno oznaczone „Zdeduplikowano”. Dwa aktywne zakupy o tej samej godzinie = podwójnie liczony ROAS.

Deduplikację można też sprawdzić w szczegółach zdarzenia (zakładka deduplikacji: procent pokrycia piksel kontra CAPI). Testowanie zdarzeń po stronie serwera wymaga kodu testowego (np. we wtyczce PixelYourSite w WooCommerce): **po teście kod trzeba usunąć i wyczyścić pamięć podręczną strony**, inaczej dane prawdziwych klientów mogą nie trafiać do raportów. Przy problemach technicznych właściciel potrzebuje programisty albo wsparcia platformy.

## Test 2. Meta Pixel Helper

Darmowa wtyczka do Chrome: pokazuje piksele na stronie i zdarzenia podczas klikania po sklepie. Szybki podgląd, mniej dokładny niż Test 1.

## Test 3. Porównanie ze sklepem (regularnie)

Menedżer zdarzeń pokazuje **wszystkie** zakupy zarejestrowane przez piksel i CAPI, niezależnie od źródła ruchu. Menedżer reklam pokazuje tylko zakupy przypisane reklamom. Do testu: Menedżer zdarzeń → piksel → Zakup → szczegółowe informacje → przegląd zdarzenia (osobno piksel i serwer). Porównaj z liczbą zamówień w panelu sklepu za ten sam okres.

| Wynik | Ocena |
|---|---|
| **Meta widzi więcej zakupów niż sklep** | błąd krytyczny: zdublowane zakupy (np. odświeżanie strony podziękowania). Najpierw naprawa, potem jakakolwiek analiza. |
| Meta widzi mniej, sklep ma też inne źródła (Google, SEO, newsletter) | normalne |
| Meta widzi dużo mniej (np. 20%), a Meta to jedyne źródło ruchu | możliwy problem: piksel na telefonach, CAPI, tryb zgody (consent mode); albo bardzo silna marka |

Naturalna utrata danych to ok. 10–25%: ludzie odrzucają pliki cookies (RODO), iOS, blokery. To powód, by nie oczekiwać idealnej zgodności.

## Atrybucja: jak Meta przypisuje sprzedaż

- **Ostatnie kliknięcie:** zakup dostaje reklama ostatniej interakcji. Reklamy „asystujące” (np. wideo z opinią, karuzela) mogą mieć 0 zakupów, choć zrobiły dużą pracę. **Zanim uznasz reklamę za słabą,** sprawdź CTR linku, koszt kliknięcia i dodania do koszyka. Gdy reklama sprowadza ruch i dodania do koszyka, zostaw ją.
- **Domyślne okno:** 7 dni po kliknięciu, 1 dzień po wyświetleniu, 1 dzień po aktywności (np. polubienie, 5 sekund wideo).
- **Okno to także wskazówka dla systemu**, kogo szukać. 1 dzień po kliknięciu = klienci impulsywni (tanie produkty, np. etui za 40 zł). 7 dni = klienci, którzy potrzebują czasu (rekomendowane dla większości sklepów). 1 dzień przy drogich produktach (np. wózki) drastycznie podnosi koszt zakupu.
- **Zliczanie:** „Wszystkie konwersje” (każde zamówienie) prawie zawsze; „Pierwsza konwersja” pokazuje tylko nowych klientów i rzadko ma sens.
- **Porównanie okien:** Kolumny → Porównaj ustawienia atrybucji (1 dzień po kliknięciu, 7 dni po kliknięciu, 1 dzień po wyświetleniu, 28 dni po kliknięciu tylko do porównania). Różnica 7 dni − 1 dzień = klienci, którzy potrzebowali czasu. Zakupy po wyświetleniu = osoby, które zobaczyły reklamę i same weszły do sklepu. Pomaga zdecydować, czy skrócenie okna ma sens (zwykle nie).
- **Model przyrostowy** (Meta szacuje zakupy, które nastąpiły tylko dzięki reklamie, na podstawie grupy kontrolnej) ujawnia, ile sprzedaży z remarketingu wydarzyłoby się i tak. Mało przejrzysty, traktuj jako uzupełnienie. Przykład: znany sklep z silnym remarketingiem: w panelu ROAS 20, przyrostowo 4; nowa marka: prawie bez różnicy.

## Trzy pułapki

1. **Za wczesny raport.** Przy oknie 7 dni zakupy dopisują się do kampanii jeszcze do 7 dni po jej wyłączeniu. Końcową ocenę rób po tygodniu.
2. **Sumowanie platform (1 + 1 = 1).** Meta, Google i newsletter przypisują sobie ten sam zakup. Prawdę mówią zamówienia w sklepie (Menedżer reklam nie widzi też zwrotów). Całość: MER (`rentownosc.md`).
3. **Wyłączanie zimnego ruchu.** Kampanie do nowych klientów mają w panelu gorszy wynik niż remarketing, bo droga do zakupu jest długa. Wyłączenie ich po kilku tygodniach „zagłodzi” remarketing i obniży sprzedaż całego sklepu. Oceniaj je po wskaźnikach pomocniczych i całym wyniku sklepu.
