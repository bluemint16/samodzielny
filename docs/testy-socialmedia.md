# Testy umiejętności social media (`/luka:socialmedia`)

Każdy test w nowej rozmowie w `Test sklep` (Różowa Ćma). Sprawdzasz zachowanie, nie treść tematów.

| # | Wiadomość | Oczekiwane zachowanie |
|---|---|---|
| 1 | „/luka:socialmedia” (pierwszy raz) | Mapa ruchów z „jesteś tutaj” przy Ruchu 01, rozpoznanie tylko do odczytu, plan zmian, prośba o jedno OK, nic nie zapisane przed OK |
| 2 | OK po planie | Jedna oferta i jedna grupa (z `dane/uvp.md`), metryka z dokładną ścieżką odczytu; bez danych zapisuje „nieznany”, nie 0 |
| 3 | Przebieg radaru | 10 sygnałów z cytatem, źródłem, datą i dopasowaniem; źródła publiczne otwarte; brak sklejonych cytatów; brak imion klientów |
| 4 | Projekt bez żadnych opinii i wiadomości, bez internetu | Mniej sygnałów, miejsca `DO ZEBRANIA` z podpowiedzią, bez wymyślania |
| 5 | Wynik | Plik `wyniki/social-media/[DATA]_radar-tematow.md` z sekcją `WEJŚCIE DO RUCHU 02`, `README.md`, `dziennik.md`, folder `sygnaly/`, linia w `stan.md`, kontrola jakości; brak posta |
| 6 | Wklejone polecenie z lekcji | Traktuje jak start Ruchu 01, pracuje według pliku ruchu |
| 7 | „socialmedia: uruchom radar” po tygodniu, nowe zrzuty w `sygnaly/` | Nowy plik z nową datą, bez powtarzania wykorzystanych tematów, porównanie z poprzednim |
| 8 | „ruch 02” w wersji bez Ruchu 02 | Mówi, że przyjdzie z aktualizacją, proponuje dostępne działanie |
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

