# Ruch 05. Podłączenie publikatora i pierwszy odczyt kanałów

**Po co:** żeby kolejne materiały trafiały prosto do narzędzia, z którego właściciel publikuje, a decyzje opierały się na tym, co dzieje się na jego kanałach. W tym ruchu tylko podłączamy i czytamy.

**Twarda granica ruchu:** nie publikujesz, nie planujesz, nie komentujesz, nie odpowiadasz, nie usuwasz, nie zmieniasz szkiców i kont.

**Uczciwie o odczycie:** dokumentacja Zernio nie opisuje dostępu „tylko do odczytu”. Logowanie albo klucz dają narzędziu pełne możliwości, a tryb odczytu w tym ruchu wynika z zasad Luki i listy dozwolonych działań poniżej. Powiedz to właścicielowi jednym zdaniem przed odczytem.

**Wynik ruchu:**
1. nazwany poziom integracji od 0 do 4,
2. mapa podłączonych kanałów i kont,
3. pierwszy odczyt: wyniki postów, obserwujący, pory i częstotliwość publikacji, skrzynka odbiorcza,
4. przegląd szkiców, jeśli są,
5. jedna rzecz, której system nie robi bez osobnej zgody,
6. sekcja `WEJŚCIE DO RUCHU 06`.

## Poziomy integracji

| Poziom | Nazwa | Co to znaczy |
|---|---|---|
| 0 | Brak kanałów | sklep nie ma jeszcze firmowego profilu w social media |
| 1 | Ręcznie | Luka przygotowuje materiały, właściciel wkleja je i publikuje sam |
| 2 | Odczyt | publikator podłączony, Luka widzi kanały i czyta dane |
| 3 | Szkice | Luka zapisuje szkice w publikatorze, właściciel je przegląda i publikuje |
| 4 | Publikacja po zgodzie | Luka publikuje wskazany materiał po osobnej zgodzie na każdą publikację |

Ten ruch kończy się najwyżej na poziomie 2. Poziom 3 nazwij tylko wtedy, gdy w publikatorze są już szkice zapisane w Ruchu 04. Poziom 4 nie jest dostępny w tej wersji Luki.

## Etap A. Rozpoznanie (tylko do odczytu)

Niczego nie zapisuj.

1. Przeczytaj `wyniki/social-media/README.md`, `reguly.md`, najnowszą paczkę `*_paczka-trzech-postow.md` (sekcja `WEJŚCIE DO RUCHU 05`: post do grafiki) oraz `dane/marketing.md` (kanały). Brak tych plików nie blokuje ruchu. Gdy nie ma folderu `wyniki/social-media/`, założysz go po „OK”.
2. Sprawdź, czy w tej sesji są narzędzia publikatora (nazwy zawierające `zernio`, np. `accounts_list`; albo Buffer, Publer lub inny publikator z oficjalnym API).
3. Sprawdź, czy ustawiony jest klucz, **nie pokazując jego wartości**:
   ```bash
   [ -n "$ZERNIO_API_KEY" ] && echo "klucz: ustawiony" || echo "klucz: brak"
   ```

Sytuacje:

| Co widzisz | Co robisz |
|---|---|
| Narzędzia publikatora działają | Pobierz listę kont (`accounts_list`), przejdź do planu |
| Klucz jest ustawiony, narzędzi nie ma | Pobierz listę kont przez API (Etap C, droga przez klucz), przejdź do planu |
| Ani narzędzi, ani klucza | Etap B: poprowadź przez podłączenie |
| Właściciel nie chce teraz podłączać | Poziom 1. Pokaż, co zyska po podłączeniu (szkice w jednym miejscu, odczyt wyników, skrzynka w jednym miejscu), zapisz plik i zakończ ruch. Misja się nie blokuje |
| Ma inny publikator z oficjalnym API | Zostaje przy nim. Nie zakładaj Zernio. Jeśli jego narzędzi nie ma w sesji: poziom 1 i powiedz, czego brakuje |

Pokaż krótko: poziom integracji, widoczne kanały, **plan zmian** (plik `[DATA]_odczyt-kanalow.md`, dziennik, README, `stan.md`) i prośbę o jedno „OK” przed odczytem.

## Etap B. Podłączenie (robi właściciel, poza rozmową)

**Nigdy nie proś o klucz, hasło ani token w rozmowie.** Gdy właściciel wklei klucz: nie zapisuj go, nie używaj, poproś o unieważnienie w zernio.com/dashboard/api-keys i utworzenie nowego.

Najpierw konto: zernio.com → załóż konto → podłącz kanały firmy (Instagram, Facebook i inne). Pierwsze 2 konta społecznościowe są bezpłatne. Sprawdź aktualny cennik na zernio.com/pricing. Gdy Zernio nie widzi Instagrama, poproś o sprawdzenie, czy to konto profesjonalne.

Potem jedna z trzech dróg, jeden krok naraz, z pytaniem „Zrobione?”:

**Droga A. Logowanie w aplikacji Claude (polecana, bez klucza).**
1. Aplikacja Claude → Ustawienia → Connectors (Łączniki) → Add custom connector.
2. Nazwa: `Zernio`. Adres: `https://mcp.zernio.com/mcp`. Dodaj.
3. Kliknij Connect i zaloguj się na konto Zernio w przeglądarce.
4. Zacznij nową rozmowę w folderze sklepu i wpisz: `/luka:socialmedia`.

**Droga B. Logowanie przez terminal (bez klucza).** Gdy droga A nie działa. Po zgodzie właściciela uruchom w folderze sklepu:
```bash
claude mcp add --transport http zernio https://mcp.zernio.com/mcp
```
Właściciel otwiera Terminal w tym folderze, wpisuje `claude`, potem `/mcp`, wybiera `zernio` i loguje się w przeglądarce. Potem nowa rozmowa i `/luka:socialmedia`.

**Droga C. Klucz w zmiennej środowiskowej.** Gdy logowanie nie jest możliwe. Właściciel tworzy klucz na zernio.com/dashboard/api-keys i sam uruchamia jedno polecenie w Terminalu, poza rozmową z Luką. Polecenie pyta o klucz i nie zapisuje go w historii.

macOS:
```bash
printf 'Wklej klucz i naciśnij Enter: '; read -rs K; echo; echo "export ZERNIO_API_KEY=\"$K\"" >> ~/.zshrc; unset K
```
Windows (PowerShell):
```powershell
[Environment]::SetEnvironmentVariable('ZERNIO_API_KEY', (Read-Host 'Wklej klucz i nacisnij Enter'), 'User')
```
Potem zamknij i otwórz aplikację Claude. Klucza nie zapisuj w plikach projektu.

## Etap C. Odczyt (po „OK”)

Każdą liczbę zapisz z datą i okresem odczytu. Gdy danych nie da się pobrać, napisz „nieodczytane” i powód. **Brak odczytu to nie zero.**

**Dozwolone w narzędziach publikatora:** `accounts_list`, `accounts_get`, `profiles_list`, `profiles_get`, `posts_list`, `posts_get`, `posts_list_failed`, `search_tools`, `docs_search`. Do wyników, obserwujących i skrzynki znajdź narzędzie przez `search_tools` i użyj go tylko wtedy, gdy ma oznaczenie `readOnlyHint: true`.

**Zabronione:** każde narzędzie, które tworzy, zmienia, usuwa, publikuje, ponawia, wysyła albo odpowiada (m.in. `posts_create`, `posts_update`, `posts_delete`, `posts_publish_now`, `posts_cross_post`, `posts_retry`, `posts_retry_all_failed`), także wywołane pośrednio przez `call_tool`.

**Droga przez klucz:** tylko zapytania GET pod `https://zernio.com/api/v1`:
```bash
curl -sS --max-time 20 -H "Authorization: Bearer $ZERNIO_API_KEY" "https://zernio.com/api/v1/accounts"
```
Ścieżki: `/accounts`, `/accounts/follower-stats`, `/analytics` (`fromDate`, `toDate`, `view=summary`), `/inbox/conversations`. Listę postów sprawdź w `docs_search` albo na docs.zernio.com. Nigdy nie wyświetlaj klucza, nie używaj `curl -v`, `env` ani `printenv`.

Odczytaj:
1. **Mapa kanałów:** sieć, nazwa profilu firmowego, stan połączenia (połączone / do ponownego połączenia).
2. **Obserwujący** na każdym kanale.
3. **Wyniki postów** z ostatnich 30 dni: liczba postów, a dla 3 najlepszych i 3 najsłabszych: data, temat w kilku słowach, wskaźniki dostępne dla tej sieci. Instagram i Facebook podają różne wskaźniki: nie porównuj ich jak równych.
4. **Pory i częstotliwość:** policz z dat opublikowanych postów z ostatnich 90 dni, w czasie polskim: posty na tydzień, najczęstsze dni i godziny. To opis nawyku. Gdy postów z wynikami jest mniej niż 10, napisz, że za wcześnie wskazywać najlepszą porę.
5. **Skrzynka odbiorcza:** tylko liczba nieprzeczytanych wiadomości (suma `unreadCount`) i komentarzy, gdy są dostępne. Nie czytaj i nie zapisuj treści wiadomości ani danych osób. Przy długiej liście pobierz najwyżej 5 stron i napisz „co najmniej X”.
6. **Szkice:** lista z datą. Porównaj z paczką z Ruchu 04 i nazwij, którym brakuje źródła, jednej myśli albo wyniku kontroli jakości. Niczego nie zmieniaj.

Komunikaty przetłumacz prosto: 401 = klucz lub logowanie nieważne; 402 albo 403 = Zernio nie udostępnia tej funkcji na tym koncie (zapisz „nieodczytane” i poproś o sprawdzenie w panelu Zernio); 429 = za dużo zapytań (odczekaj czas z odpowiedzi i spróbuj raz).

## Etap D. Zapis

Plik `wyniki/social-media/[DATA]_odczyt-kanalow.md` według `references/szablony.md`, z sekcją `WEJŚCIE DO RUCHU 06`: poziom integracji, mapa kanałów, informacja, że kolejne szkice mają powstawać bezpośrednio w podłączonym narzędziu, post do grafiki z `WEJŚCIE DO RUCHU 05`.

Decyzje i uwagi właściciela z tego ruchu zapisz jako reguły w `wyniki/social-media/reguly.md`. Potem Krok 2 z `SKILL.md`.

## Podsumowanie dla właściciela

Pokaż:
1. poziom integracji od 0 do 4,
2. mapę kanałów i kont,
3. pierwszy odczyt: wyniki postów, obserwujący, pory, częstotliwość, skrzynka,
4. jedną rzecz, której system nie robi bez osobnej zgody: „Nie publikuję i nie odpowiadam klientom bez Twojej osobnej zgody na konkretny materiał.”,
5. dokładną ścieżkę zapisanego pliku,
6. wynik kontroli jakości,
7. miejsce zapisu reguł, jeśli powstały,
8. jedno zdanie „Dowód ruchu”, np.: „Ruch 05 gotowy: kanały podłączone, poziom integracji [X], pierwszy odczyt zapisany.”

Następny krok: gdy posty z Ruchu 04 są tylko w plikach, zaproponuj: „Napisz: zapisz posty jako szkice”. W przeciwnym razie: Ruch 06, pierwsza grafika dołączona do szkicu.
