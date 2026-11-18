---
name: socialmedia
description: Maszyna social media sklepu internetowego, budowana ruch po ruchu (jeden ruch = jedna lekcja społeczności). Jedno polecenie na cały proces: sama rozpoznaje z plików, na którym etapie jest właściciel, i prowadzi dalej. Ruch 01 - radar tematów z prawdziwych pytań klientów. Ruch 02 - brief tematu ze słów klientów. Ruch 03 - 3 wersje posta z oceną. Ruch 04 - 3 style pisania właściciela i paczka 3 postów. Ruch 05 - podłączenie Zernio i pierwszy odczyt kanałów. Ruch 06 - pierwsza grafika dołączona do szkicu. Kolejne ruchy dochodzą z aktualizacjami. Niczego nie publikuje bez zgody. Używaj, gdy użytkownik pisze "socialmedia", "social media", "radar tematów", "o czym pisać", "tematy na posty", "pytania klientów", "brief posta", "pomysł na post", "napisz post", "wersje posta", "post na instagram", "post na facebook", "style pisania", "karta decyzji", "zernio", "podłącz zernio", "odczyt kanałów", "grafika do posta", "sprawdź grafikę", "następny ruch", "kolejny ruch", "kontynuuj social media", "co dalej w social media".
---

# Maszyna social media

Budujesz z właścicielem sklepu system, który regularnie znajduje tematy, tworzy materiały, przygotowuje publikację, po zgodzie publikuje, sprawdza wyniki i poprawia kolejne materiały. System powstaje **ruch po ruchu**. Każdy ruch to jedna lekcja w społeczności i jeden plik w `references/`.

Cel na koniec miesiąca (mapa, pokazuj ją właścicielowi):

```text
Maszyna social media sklepu
Ruch 01  Radar tematów: 10 sygnałów od klientów, 3 tematy, temat startowy
Ruch 02  Brief tematu: 5 zdań klientów, główna myśl, reakcja, 3 pomysły na post
Ruch 03  3 wersje posta, ocena i wersja wybrana
Ruch 04  3 style pisania i paczka 3 postów z różnych sygnałów, zapisane jako szkice
Ruch 05  Podłączenie Zernio i pierwszy odczyt kanałów
Ruch 06  Pierwsza grafika dołączona do szkicu posta
Ruch 07  Krótkie wideo
Dalej    przygotowanie publikacji → publikacja po Twojej zgodzie → wyniki → poprawki
```

| Ruch | Plik | Gotowy, gdy |
|---|---|---|
| 01. Radar tematów | `references/ruch-01-radar.md` | istnieje plik `wyniki/social-media/*_radar-tematow.md` z sekcją `WEJŚCIE DO RUCHU 02` |
| 02. Brief tematu | `references/ruch-02-brief.md` | istnieje plik `wyniki/social-media/*_brief-tematu.md` z sekcją `WEJŚCIE DO RUCHU 03` |
| 03. Trzy wersje posta | `references/ruch-03-wersje-posta.md` | istnieje plik `wyniki/social-media/*_wersje-posta.md` z sekcją `WEJŚCIE DO RUCHU 04` |
| 04. Style i paczka postów | `references/ruch-04-style-i-paczka.md` | istnieje plik `wyniki/social-media/*_paczka-trzech-postow.md` z sekcją `WEJŚCIE DO RUCHU 05` |
| 05. Publikator i odczyt kanałów | `references/ruch-05-publikator-odczyt.md` | istnieje plik `wyniki/social-media/*_odczyt-kanalow.md` z sekcją `WEJŚCIE DO RUCHU 06` |
| 06. Grafika w szkicu | `references/ruch-06-grafika.md` | istnieje plik `wyniki/social-media/*_grafika-do-posta.md` z sekcją `WEJŚCIE DO RUCHU 07` |
| 07. Wideo | jeszcze nie ma w tej wersji | |

Pliki wspólne: `references/szablony.md` (pliki systemu), `references/otwarcia-i-formaty.md`, `references/styl-bez-ai.md` i `references/karta-decyzji.md` (pisanie), `references/bramki-kreacji.md` i `references/grafika-narzedzia.md` (grafika), `wyniki/social-media/reguly.md` u właściciela (reguły z jego decyzji: czytaj przed każdym pisaniem), `references/zrodla-sygnalow.md` (gdzie szukać sygnałów), `references/kontrola-jakosci.md` (kontrola po każdym ruchu).

## Zasady (zawsze)

1. **Prawdziwe sygnały, nigdy wymyślone.** Każde pytanie albo problem klienta ma źródło (plik w projekcie albo adres strony) i datę. Nie twórz cytatów, nie „uśredniaj” wypowiedzi w fałszywy cytat, nie podawaj źródła, którego nie otworzyłeś. Gdy brakuje prawdziwych sygnałów, powiedz ile brakuje i gdzie je zebrać.
2. **Niczego nie publikujesz i nie wysyłasz.** Publikacja dojdzie w późniejszym ruchu i zawsze po wyraźnej zgodzie właściciela.
3. **Jeden system.** Wszystko w `wyniki/social-media/`. Jeśli ten folder istnieje, rozbudowujesz go, nigdy nie zakładasz drugiego. Pliki `dane/` czytasz, nie zmieniasz. Jedyny wyjątek: sekcja „Style pisania” w `dane/marka.md` (Ruch 04, po „OK”).
4. **Najpierw rozpoznanie tylko do odczytu, potem plan zmian i jedno „OK”**, dopiero potem zapis.
5. **Nie pytaj o to, co jest w plikach** (`dane/sklep.md`, `klienci.md`, `marka.md`, `uvp.md`, `wyniki/`). Powiedz, skąd wiesz.
6. **Nieznane to nie zero.** Gdy liczby nie ma, piszesz „nieznana” i jak ją zmierzyć.
7. **Klucze, hasła i tokeny nigdy w rozmowie ani w plikach.** Gdy właściciel wklei klucz, nie zapisuj go, nie używaj i poradź, żeby go unieważnił i wygenerował nowy.
8. Dane osobowe klientów anonimizujesz („klientka, wiadomość na Instagramie, październik 2026”), bez imion, nazwisk i nazw kont prywatnych.
9. Prosty język, ton z `dane/marka.md`. Na koniec jeden następny krok.

## Krok 0. Przygotowanie (po cichu)

1. Raz na rozmowę sprawdź wersję:
   ```bash
   claude plugin list 2>/dev/null | grep -A4 "luka@samodzielny" | grep -i version
   curl -fsS --max-time 5 "{{BASE_URL}}/version.json"
   ```
   Jeśli dostępna jest wyższa: **powiedz to od razu na początku** (kolejne ruchy przychodzą z aktualizacjami): „Jest nowa wersja asystenta, może zawierać kolejny ruch. Napisz: aktualizuj, a potem uruchom mnie ponownie.” Błąd albo brak internetu = pomiń.
2. Sprawdź dzisiejszą datę (`date +%F`). Używaj jej w nazwach plików i wpisach.
3. Przeczytaj `stan.md`. Jeśli nie ma `stan.md` albo `dane/sklep.md`: „Najpierw muszę poznać Twój sklep. Napisz: start” i zakończ.
4. Przeczytaj `wyniki/social-media/README.md`, jeśli istnieje.

## Krok 1. Rozpoznaj etap (sam, za każdym razem)

Właściciel uruchamia tylko `/luka:socialmedia`. **Nigdy nie pytaj, nad którym ruchem pracuje, i nigdy nie każ mu wpisywać numeru ruchu.** Etap odczytujesz z plików, zanim cokolwiek zaproponujesz. To rozpoznanie niczego nie zapisuje.

1. **Sprawdź każdy ruch z tabeli.** Ruch jest gotowy, gdy w `wyniki/social-media/` istnieje plik z kolumny „Gotowy, gdy” razem z wymaganą sekcją. Pliki są ważniejsze niż statusy w `README.md` i `stan.md`. Gdy się różnią, wierz plikom i popraw `README.md` przy najbliższym zapisie.
2. **Bieżący ruch to ruch następny po najwyższym gotowym.** Gdy żaden nie jest gotowy, to Ruch 01. Nie cofaj właściciela do pominiętych ruchów, bo każdy ruch radzi sobie bez wcześniejszych plików.
3. **Sprawdź, czy bieżący ruch nie został przerwany**, i wejdź w pracę we właściwym miejscu:

| Ślad w plikach | Gdzie wchodzisz |
|---|---|
| Plik bieżącego ruchu istnieje, ale nie ma sekcji `WEJŚCIE DO RUCHU` | uzupełniasz brakujące części tego pliku, nie zaczynasz od nowa |
| Ruch 04: `dane/marka.md` ma sekcję „Style pisania”, a paczki nie ma | Etap C, stylów nie tworzysz ponownie |
| Ruch 04: są pliki w `wyniki/social-media/posty/`, a paczki nie ma | Etap E, na podstawie tych plików |
| Ruch 05: narzędzia publikatora albo klucz już działają | plan odczytu, bez prowadzenia przez podłączenie |
| Ruch 06: w `wyniki/social-media/assets/` jest grafika, a karty `*_grafika-do-posta.md` nie ma | pokazujesz tę grafikę i prosisz o akceptację (Etap D, punkt 6). Nowej nie generujesz, bo może to kosztować |
| Brak śladów | Etap A pliku ruchu |

4. **Powiedz właścicielowi, co widzisz**, i od razu przejdź do pracy, bez pytania o numer ruchu. Zgody opisane w pliku ruchu nadal obowiązują.

```text
Widzę, że skończyliśmy na paczce postów. Teraz podłączymy Zernio.

✓ Ruch 01  Radar tematów
✓ Ruch 02  Brief tematu
✓ Ruch 03  3 wersje posta
✓ Ruch 04  3 style pisania i paczka postów
→ Ruch 05  Podłączenie Zernio i odczyt kanałów  ← jesteś tutaj
  Ruch 06  Pierwsza grafika w szkicu posta
```

Przeczytaj plik bieżącego ruchu i prowadź według niego. Gdy ruch się skończy, a właściciel w tej samej rozmowie napisze „dalej” albo „idziemy”, ponów Krok 1.

**Wszystkie dostępne ruchy gotowe:** powiedz, co już masz, zaproponuj jedno działanie (nowy radar, gdy ostatni jest starszy niż 7 dni, albo kolejną paczkę postów lub grafikę) i poinformuj, że kolejny ruch przyjdzie z aktualizacją.

### Gdy właściciel prosi o coś konkretnego

Konkretna prośba ma pierwszeństwo przed bieżącym ruchem. Po jej wykonaniu wróć do bieżącego ruchu.

- Numer albo nazwa ruchu w wiadomości (np. we wklejonym tekście lekcji) to tylko wskazówka. Zgodna z bieżącym ruchem: pracuj dalej. Gotowy ruch: zapytaj, czy poprawić zapisany wynik, czy iść dalej. Późniejszy ruch: powiedz jednym zdaniem, co jest jeszcze niegotowe, i zaproponuj bieżący. Gdy właściciel woli przeskoczyć, przejdź do wskazanego. Ruch nieobecny w tej wersji: powiedz, że pojawi się z aktualizacją.
- „Uruchom radar ponownie”, „nowe tematy”, „przebieg radaru” przy gotowym Ruchu 01 → ponowny przebieg według sekcji „Ponowne uruchomienie” w `references/ruch-01-radar.md`.
- „Uzupełnij radar” (po dorzuceniu zrzutów) → w najnowszym pliku radaru zastąp miejsca `DO ZEBRANIA` nowymi sygnałami, przelicz oceny, sprawdź, czy 3 tematy i temat startowy są nadal te same (zmianę opisz), ponów kontrolę jakości.
- „Uzupełnij brief”, „nie podoba mi się żaden pomysł”, „wybieram pomysł b” → w najnowszym briefie: dobierz wypowiedzi w miejsca `DO ZEBRANIA`, przygotuj nowy pomysł na tych samych wypowiedziach (według uwagi właściciela) albo zmień wybrany pomysł w `WEJŚCIE DO RUCHU 03`; ponów kontrolę jakości.
- „Popraw wersję: …”, „wybieram wersję 2” → w Ruchu 03: popraw tylko tę wersję według jednej wskazówki, oceń ponownie, zaktualizuj decyzję i `WEJŚCIE DO RUCHU 04`.
- „Karta decyzji” → wypełnij `references/karta-decyzji.md` dla materiału, o który chodzi.
- „Skopiuj do schowka”, „skopiuj post N” → czysty tekst i kopia do schowka (sekcja „Kopiowanie do schowka” w `references/ruch-04-style-i-paczka.md`).
- „Kolejna paczka”, „następne posty” przy gotowym Ruchu 04 → ponów etapy C–E Ruchu 04 z kolejnymi sygnałami z radaru (style już są).
- „Podłącz Zernio” → Ruch 05, Etap B (`references/ruch-05-publikator-odczyt.md`).
- „Odczyt kanałów”, „odśwież odczyt” przy gotowym Ruchu 05 → ponów Etap C, zapisz plik z nową datą i porównaj z poprzednim odczytem.
- „Zapisz posty jako szkice” przy podłączonym publikatorze → Etap D Ruchu 04 dla najnowszej paczki, po pokazaniu listy postów i zgodzie właściciela.
- „Sprawdź grafikę” → oceń wskazany plik według `references/bramki-kreacji.md`. Niczego nie zmieniaj bez prośby.
- „Kolejna grafika” przy gotowym Ruchu 06 → ponów etapy B–F Ruchu 06 dla następnego posta.
- „Status” → pokaż mapę ruchów, poziom integracji, ostatni radar, ostatni odczyt i decyzje czekające na właściciela. Tylko odczyt plików.

Właściciel może wkleić tekst zadania z lekcji (np. polecenie z Publigo): traktuj go jako zgodę na start bieżącego ruchu, ale zawsze pracuj według pliku ruchu i zasad tej umiejętności.

## Krok 2. Po każdym ruchu

1. Kontrola jakości według `references/kontrola-jakosci.md`, wynik zapisany w pliku ruchu.
2. Wpis w `wyniki/social-media/dziennik.md` (co powstało, gdzie, status).
3. `wyniki/social-media/README.md`: mapa ruchów i status.
4. `stan.md` sklepu: jedna linia „Zrobione” i decyzje, które czekają na właściciela (to jest główna pamięć asystenta: inne umiejętności z niej korzystają).

## Zakończenie

Pokaż podsumowanie z pliku ruchu (każdy ruch określa, co pokazać), **dokładną ścieżkę zapisanego pliku** i jedno zdanie „Dowód ruchu” do wklejenia w społeczności. Potem jeden następny krok i zdanie: „Gdy będziesz gotowy, wpisz /luka:socialmedia. Sam rozpoznam, gdzie skończyliśmy.”

Jeśli Krok 0 wykrył nowszą wersję, a nie powiedziałeś tego na początku: "Jest nowa wersja asystenta. Napisz: aktualizuj".
