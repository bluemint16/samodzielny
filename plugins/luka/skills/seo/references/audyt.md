# Tryb 1. Audyt SEO sklepu (Google i AI)

Audyt to wyłącznie odczyt. Niczego nie zmieniasz. Wynik to raport z 5 najważniejszymi poprawkami i instrukcją dla platformy właściciela.

## Przygotowanie

1. Weź adres sklepu z `stan.md`. Zapytaj tylko o to, czego nie da się odczytać:
   - "Czy masz dostęp do Google Search Console? (tak / nie / nie wiem)"
   - "Czy masz konto w Google Merchant Center (darmowe wyświetlanie produktów w Google)? (tak / nie / nie wiem)"
2. Wybierz próbkę stron: strona główna, 3 najważniejsze kategorie i 3 najważniejsze produkty (z `dane/sklep.md` albo z menu sklepu).
3. Powiedz właścicielowi: "Sprawdzam teraz Twój sklep. Potrwa to kilka minut, nic nie zmieniam."

## Jak sprawdzać

Używaj poleceń terminala i pobierania stron. Przykłady:

```bash
curl -sIL "https://ADRES/" | grep -iE "^HTTP|^location"          # kody odpowiedzi i przekierowania
curl -s "https://ADRES/robots.txt"                                 # zasady dla robotów
curl -s "https://ADRES/sitemap.xml" | head -50                     # mapa strony
curl -sL "https://ADRES/STRONA" -A "Mozilla/5.0" -o /tmp/strona.html  # kod strony do analizy
grep -io '<title>[^<]*' /tmp/strona.html
grep -io '<meta name="description"[^>]*' /tmp/strona.html
grep -io '<link rel="canonical"[^>]*' /tmp/strona.html
grep -io '<meta name="robots"[^>]*' /tmp/strona.html
grep -o '<script type="application/ld+json">.*</script>' /tmp/strona.html   # dane strukturalne (mogą być w kilku liniach, wtedy czytaj plik)
```

Szybkość: zapytaj publiczne API PageSpeed Insights (działa bez klucza, ale ma limity):

```bash
curl -s "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://ADRES/&strategy=mobile&category=performance" | head -c 20000
```

Szukaj `loadingExperience` (dane prawdziwych użytkowników) i oddziel je od testu laboratoryjnego (`lighthouseResult`). Gdy API odmówi, oznacz NIE SPRAWDZONO i daj właścicielowi link `https://pagespeed.web.dev/`.

Jeśli sklep blokuje pobieranie (kod 403, ochrona przed botami), oznacz to i poproś właściciela o zapisanie kodu strony (w przeglądarce: prawy przycisk, "Zapisz stronę jako") do folderu `dane/`.

## Lista kontrolna

### A. Dostępność dla Google (techniczne podstawy)
1. Jedna wersja adresu: `http` przekierowuje na `https`, a wersja z `www` i bez `www` prowadzi do jednej. Przekierowanie jednym skokiem.
2. `robots.txt` nie blokuje produktów, kategorii, zdjęć, plików CSS ani JS. Blokowanie koszyka, zamówienia, konta klienta i wyników wyszukiwarki sklepu jest w porządku.
3. Mapa strony istnieje, jest wskazana w `robots.txt`, zawiera produkty i kategorie i nie zawiera adresów przekierowanych ani usuniętych (sprawdź 5 losowych adresów).
4. Na próbce stron: brak `noindex` tam, gdzie strona ma być w Google; jest `canonical` wskazujący samą siebie albo właściwą wersję.
5. Filtry i sortowanie (np. `?color=`, `?sort=`, `?page=`): czy tworzą tysiące adresów do zaindeksowania? Sprawdź, czy mają canonical do kategorii albo są wyłączone z indeksu. To częsty problem sklepów.
6. Warianty produktu (rozmiar, kolor): jeden adres z wyborem wariantu czy osobne strony? Osobne strony bez canonical = ryzyko dublowania treści.
7. Produkty niedostępne: co pokazuje sklep? Dobra praktyka: produkt chwilowo niedostępny zostaje na stronie z informacją i alternatywami. Wycofany na stałe przekierowuje (301) do najbliższej kategorii albo następcy.
8. Szybkość na telefonie: LCP do 2,5 s, INP do 200 ms, CLS do 0,1 (progi Google; przed użyciem potwierdź, że się nie zmieniły).

### B. Kategorie
1. Unikalny tytuł strony z nazwą kategorii tak, jak szukają jej klienci (np. "Buty do biegania damskie", a nie "Kolekcja Run").
2. Jeden nagłówek H1 zgodny z tytułem.
3. Krótki tekst na górze (2–3 zdania pomagające wybrać), dłuższy poradnik pod listą produktów. Bez upychania fraz.
4. Linki do podkategorii i powiązanego poradnika.
5. Okruszki (ścieżka "Strona główna > Kategoria > Podkategoria").

### C. Karty produktów
1. Opis własny, nie skopiowany od producenta. Sprawdź: weź jedno charakterystyczne zdanie z opisu i wyszukaj je w cudzysłowie. Ten sam tekst w wielu sklepach = PROBLEM (Ważne).
2. Tytuł strony: nazwa, najważniejsza cecha, ewentualnie marka. Unikalny dla każdego produktu.
3. Opis odpowiada na pytania klientów z `dane/klienci.md` (rozmiar, materiał, zastosowanie, pielęgnacja, dostawa).
4. Zdjęcia mają opisy alternatywne (`alt`) mówiące, co jest na zdjęciu.
5. Cena, dostępność i koszt dostawy widoczne bez klikania.
6. Opinie klientów na stronie (prawdziwe).

### D. Dane strukturalne (informacje o produkcie zapisane w kodzie dla Google)
1. Karty produktów: typ `Product` z `Offer` (cena, waluta, dostępność). Dobrze, jeśli są też informacje o dostawie i zwrotach.
2. Ocena (`aggregateRating`) tylko wtedy, gdy opinie są widoczne na stronie.
3. `BreadcrumbList` na kategoriach i produktach, `Organization` na stronie głównej.
4. Dane w kodzie muszą zgadzać się z tym, co widzi klient (ta sama cena, ta sama dostępność).
5. Zaproponuj właścicielowi sprawdzenie jednej karty w Teście wyników z elementami rozszerzonymi: `https://search.google.com/test/rich-results`.

### E. Widoczność w asystentach AI
1. `robots.txt` a roboty AI. Wypisz, co jest dozwolone, a co zablokowane, dla: `OAI-SearchBot` (wyszukiwanie w ChatGPT), `GPTBot` (trenowanie modeli OpenAI), `ClaudeBot`, `PerplexityBot`, `Google-Extended` (trenowanie Gemini, nie wpływa na wyniki Google). Zablokowany robot wyszukiwania = sklep nie pojawi się w odpowiedziach tego asystenta. Blokada robotów trenujących to osobna, świadoma decyzja właściciela. Wyjaśnij różnicę jednym zdaniem.
2. Czy zawartość strony jest w kodzie HTML, czy dopiero po uruchomieniu skryptów? Wiele robotów AI nie uruchamia JavaScript. Porównaj, czy opis produktu jest w pobranym pliku HTML.
3. Czy sklep ma treści, które asystent może zacytować: poradniki wyboru, tabele rozmiarów, porównania, odpowiedzi na częste pytania.
4. Spójność informacji o sklepie w sieci: nazwa, adres, kontakt, zasady zwrotów takie same na stronie, w Profilu Firmy w Google, na Allegro, Ceneo i w porównywarkach.
5. Plik `llms.txt`: odnotuj, czy istnieje. To dodatek o niepotwierdzonym wpływie. Nie oznaczaj braku jako problemu.
6. Pomiar: czy w Google Analytics widać ruch z `chatgpt.com`, `perplexity.ai`, `gemini.google.com`, `copilot.microsoft.com`? Jeśli właściciel nie wie, oznacz NIE SPRAWDZONO i dodaj zadanie "sprawdź raport Pozyskiwanie ruchu".

### F. Google Merchant Center
Jeśli sklep nie ma Merchant Center, zaproponuj to jako zadanie Ważne: darmowe wyświetlanie produktów w zakładce Zakupy i w wynikach Google. Większość platform ma gotową integrację.

## Raport

Zapisz `wyniki/seo/audyt_[RRRR-MM-DD].md` (po zgodzie):

```markdown
# Audyt SEO: [sklep], [data]

## W skrócie
[3 zdania dla właściciela: co działa, co najbardziej blokuje, od czego zacząć]

## 5 najważniejszych poprawek
1. [Pilne] [co] — dlaczego: [...] — jak zrobić w [platforma]: [...] — jak sprawdzić: [...]
...

## Wszystkie ustalenia
| Obszar | Co sprawdzałem | Status | Priorytet | Dowód | Co zrobić |
|---|---|---|---|---|---|

## Nie sprawdzono
- [element]: [dlaczego, co potrzebne]

## Następny krok
[jeden]
```

Pokaż właścicielowi najpierw "W skrócie" i "5 najważniejszych poprawek". Pełną tabelę tylko na prośbę albo w pliku.

Zaproponuj następny tryb: brak danych z Search Console → pomóż podłączyć (instrukcja w `references/gsc.md`, sekcja Podłączenie). Problemy z opisami → tryb 3. Brak poradników i treści pod AI → tryb 4 albo 2.
