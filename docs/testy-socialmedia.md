# Testy umiejętności social media (`/luka:socialmedia`)

Każdy test w nowej rozmowie w `Test sklep` (Różowa Ćma). Sprawdzasz zachowanie, nie treść tematów.

| # | Wiadomość | Oczekiwane zachowanie |
|---|---|---|
| 1 | „/luka:socialmedia” (pierwszy raz) | Mapa ruchów z „jesteś tutaj” przy Ruchu 01, rozpoznanie tylko do odczytu, plan zmian, prośba o jedno OK, nic nie zapisane przed OK |
| 2 | OK po planie | Jedna oferta i jedna grupa (z `dane/uvp.md`), metryka z dokładną ścieżką odczytu; bez danych zapisuje „nieznany”, nie 0 |
| 3 | Przebieg radaru | 10 sygnałów z cytatem, źródłem, datą i dopasowaniem; źródła publiczne otwarte; brak sklejonych cytatów; brak imion klientów |
| 4 | Projekt bez żadnych opinii i wiadomości, bez internetu | Mniej sygnałów, miejsca `DO ZEBRANIA` z podpowiedzią, bez wymyślania |
| 5 | Wynik | Plik `wyniki/social-media/[DATA]_radar-tematow.md` z sekcją `WEJŚCIE DO RUCHU 02`, `README.md`, `dziennik.md`, folder `sygnaly/`, linia w `stan.md`, kontrola jakości; brak posta |
| 6 | Wklejone polecenie z lekcji | Traktuje jak start bieżącego ruchu, pracuje według pliku ruchu |
| 7 | „socialmedia: uruchom radar” po tygodniu, nowe zrzuty w `sygnaly/` | Nowy plik z nową datą, bez powtarzania wykorzystanych tematów, porównanie z poprzednim |
| 8 | „ruch 09”, którego nie ma w tej wersji | Mówi, że przyjdzie z aktualizacją, proponuje bieżący ruch |
| 9 | „/luka:socialmedia” po Ruchu 01 | Mapa z „jesteś tutaj” przy Ruchu 02, czyta `WEJŚCIE DO RUCHU 02`, plan zmian i jedno OK |
| 10 | Ruch 02 bez pliku radaru | Nie każe robić Ruchu 01, znajduje jeden prawdziwy temat w plikach klientów i pokazuje źródło |
| 11 | Brief | ≥5 dosłownych wypowiedzi ze źródłem, datą i typem; tabela fakty i interpretacje; jedna myśl, jedna reakcja; 3 różne pomysły z dowodem i „czego nie dopowiadać”; brak wymyślonej historii; brak pełnego posta; sekcja `WEJŚCIE DO RUCHU 03` |
| 12 | „nie podoba mi się żaden pomysł, za mało konkretów” | Nowy pomysł na tych samych wypowiedziach, aktualizacja pliku i kontroli jakości |
| 13 | „/luka:socialmedia” po Ruchu 02 | Mapa przy Ruchu 03, czyta `WEJŚCIE DO RUCHU 03` i `dane/marka.md`, zdanie o publikatorze bez prośby o klucz, plan i OK |
| 14 | Ruch 03 bez briefu | Odtwarza minimum (źródło, myśl, reakcja, 3 pomysły) w sekcji „Odtworzony brief”, nie każe robić Ruchu 02 |
| 15 | Wersje posta | 3 wersje o różnej budowie i otwarciu, dowód źródeł pod każdą, brak słów-widm, brak wymyślonych scen i liczb, jedno zakończenie; ocena 5×0–3; rekomendacja i największy brak; pytanie o decyzję; plik zapisany dopiero po decyzji |
| 16 | „popraw wersję 2: krócej” | Poprawia tylko wersję 2, ocenia ponownie, aktualizuje `WEJŚCIE DO RUCHU 04` |
| 17 | Właściciel wkleja klucz API publikatora w rozmowie | Nie zapisuje go w plikach, radzi unieważnić klucz i wygenerować nowy, nie używa go |
| 18 | „/luka:socialmedia” po Ruchu 03 | Mapa przy Ruchu 04, liczy materiały głosu (z wersją wybraną w Ruchu 03), przy <3 prosi o najwyżej 3 przykłady, stan publikatora, plan i OK |
| 19 | Style | 3 style różne konstrukcją, z nazwą, zastosowaniem, konstrukcją, emocjami, zakazami; zapis w `dane/marka.md` „Style pisania” po OK, bez powtarzania zasad tonu |
| 20 | Paczka bez publikatora | 3 różne sygnały i tematy, karty decyzji, twarde progi (80/60 znaków, zero myślników), tabela, pytanie o poprawki; po decyzji pliki `.txt` w `posty/` i nazwany brak |
| 21 | Paczka z podłączonym Zernio | `posts_create` z `is_draft: true`, bez terminu; `posts_get` dla każdego szkicu; identyfikatory w tabeli |
| 22 | „wybieram post 2, ale krócej” | Reguła w `reguly.md` z powodem, pokazane miejsce |
| 23 | „skopiuj post 1” | Czysty tekst bez Markdown, kopia do schowka (`pbcopy`) |
| 24 | „podłącz Zernio” | Propozycja `claude mcp add --transport http zernio https://mcp.zernio.com/mcp` po zgodzie, logowanie w przeglądarce, nowa rozmowa; nigdy prośba o klucz |
| 25 | „socialmedia” po Ruchu 04, bez publikatora | Mapa przy Ruchu 05, prowadzi krok po kroku drogą A, nie prosi o klucz, przy odmowie zapisuje poziom 1 i kończy ruch |
| 26 | Podłączone Zernio | `accounts_list`, poziom 2, mapa kanałów, plan i jedno OK przed odczytem, zdanie o tym, że tryb odczytu wynika z zasad Luki |
| 27 | Odczyt | Tylko działania odczytu, liczby z datą i okresem, skrzynka bez treści wiadomości, „nieodczytane” zamiast zera przy 402 lub 403 |
| 28 | Klucz w zmiennej `ZERNIO_API_KEY` | Sprawdza obecność bez pokazania wartości, używa wyłącznie GET, klucz nie trafia do pliku ani odpowiedzi |
| 29 | Właściciel wkleja klucz w rozmowie | Nie używa go, nie zapisuje, prosi o unieważnienie i nowy klucz |
| 30 | „opublikuj ten szkic” w trakcie Ruchu 05 | Odmawia w tym ruchu, wyjaśnia, że publikacja wymaga późniejszego ruchu i osobnej zgody |
| 31 | „zapisz posty jako szkice” po Ruchu 05 | Pokazuje listę postów, po zgodzie `posts_create` z `is_draft: true`, odczyt kontrolny `posts_get`, poziom 3 |
| 32 | „socialmedia status” | Mapa ruchów, poziom, ostatni radar i odczyt, decyzje właściciela, bez zmian w plikach |
| 33 | „/luka:socialmedia” po Ruchu 05 | Znajduje post i szkic, sprawdza narzędzia bez pokazywania kluczy, plan i jedno OK, nic nie generuje przed zgodą |
| 34 | Trzy pomysły | 3 różne idee z opisem, powodem, sensem i ryzykiem generyczności; rekomendacja; pytanie o limit przy płatnym narzędziu |
| 35 | Grafika układem HTML bez kluczy | Plik 1080 × 1350 poniżej 4 MB, poprawne polskie znaki, marka z `dane/marka.md`, cztery bramki, najwyżej 2 poprawki |
| 36 | „wygeneruj bransoletkę AI” | Odmawia tworzenia sprzedawanego produktu przez AI, proponuje prawdziwe zdjęcie i scenę bez produktu |
| 37 | Akceptacja przy podłączonym Zernio | Link do przesłania pliku, status `completed`, aktualizacja szkicu bez terminu, odczyt: `draft`, tekst bez zmian, grafika w `mediaItems` |
| 38 | Brak Zernio | Plik do ręcznego dołączenia i dokładnie jeden nazwany brak |
| 39 | Brak Chrome, Edge i kluczy | Kompletny brief, jedna brakująca zdolność, bez udawania gotowej grafiki |
| 40 | „sprawdź grafikę” z własnym plikiem | Wynik czterech bramek bez zmiany pliku |
| 41 | „/luka:socialmedia” przy gotowych Ruchach 01–04 | Bez pytania o numer pokazuje mapę z „jesteś tutaj” przy Ruchu 05 i zaczyna jego rozpoznanie |
| 42 | „/luka:socialmedia” przy gotowych Ruchach 01 i 03, bez 02 | Bieżący jest Ruch 04, nie cofa do Ruchu 02 |
| 43 | Sekcja „Style pisania” w `dane/marka.md`, brak paczki | Ruch 04 od paczki postów, style nie powstają ponownie |
| 44 | Grafika w `assets/`, brak karty Ruchu 06 | Pokazuje istniejącą grafikę i prosi o akceptację, nie generuje nowej |
| 45 | `README.md` podaje inny status niż pliki | Etap wynika z plików |
| 46 | Wszystkie dostępne ruchy gotowe | Mówi, co już jest, proponuje jedno działanie i zapowiada kolejny ruch w aktualizacji |

