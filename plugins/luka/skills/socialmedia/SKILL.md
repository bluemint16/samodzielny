---
name: socialmedia
description: Maszyna social media sklepu internetowego, budowana ruch po ruchu (jeden ruch = jedna lekcja społeczności). Ruch 01 - radar tematów (10 prawdziwych pytań klientów ze źródłami, 3 tematy, temat startowy, wynik początkowy metryki). Ruch 02 - brief tematu (5 dosłownych wypowiedzi klientów, główna myśl, reakcja odbiorcy, 3 pomysły). Ruch 03 - 3 wersje posta (praktyczna, historia, opinia) w głosie sklepu, z oceną. Ruch 04 - 3 style pisania właściciela i paczka 3 postów z różnych sygnałów, zapisane jako szkice w publikatorze (np. Zernio) albo pliki. Kolejne ruchy dochodzą z aktualizacjami. Niczego nie publikuje bez zgody. Używaj, gdy użytkownik pisze "socialmedia", "social media", "radar tematów", "o czym pisać", "tematy na posty", "pytania klientów", "brief posta", "pomysł na post", "napisz post", "wersje posta", "post na instagram", "post na facebook", "ruch 01", "ruch 02", "ruch 03", "ruch 04", "style pisania", "karta decyzji", "następny ruch".
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
Ruch 05  Grafika do wybranego posta
Dalej    wideo → przygotowanie publikacji → publikacja po Twojej zgodzie → wyniki → poprawki
```

| Ruch | Plik | Gotowy, gdy |
|---|---|---|
| 01. Radar tematów | `references/ruch-01-radar.md` | istnieje plik `wyniki/social-media/*_radar-tematow.md` z sekcją `WEJŚCIE DO RUCHU 02` |
| 02. Brief tematu | `references/ruch-02-brief.md` | istnieje plik `wyniki/social-media/*_brief-tematu.md` z sekcją `WEJŚCIE DO RUCHU 03` |
| 03. Trzy wersje posta | `references/ruch-03-wersje-posta.md` | istnieje plik `wyniki/social-media/*_wersje-posta.md` z sekcją `WEJŚCIE DO RUCHU 04` |
| 04. Style i paczka postów | `references/ruch-04-style-i-paczka.md` | istnieje plik `wyniki/social-media/*_paczka-trzech-postow.md` z sekcją `WEJŚCIE DO RUCHU 05` |
| 05. Grafika | jeszcze nie ma w tej wersji | |

Pliki wspólne: `references/szablony.md` (pliki systemu), `references/otwarcia-i-formaty.md`, `references/styl-bez-ai.md` i `references/karta-decyzji.md` (pisanie), `wyniki/social-media/reguly.md` u właściciela (reguły z jego decyzji: czytaj przed każdym pisaniem), `references/zrodla-sygnalow.md` (gdzie szukać sygnałów), `references/kontrola-jakosci.md` (kontrola po każdym ruchu).

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

## Krok 1. Który ruch

- Wiadomość wskazuje ruch („ruch 01”, „radar”, „ruch 02”) → ten ruch. Gdy wskazany ruch nie istnieje w tej wersji: powiedz, że pojawi się z aktualizacją, i zaproponuj to, co jest dostępne.
- „Uruchom radar ponownie”, „nowe tematy”, „przebieg radaru” przy gotowym Ruchu 01 → ponowny przebieg według sekcji „Ponowne uruchomienie” w `references/ruch-01-radar.md`.
- „Uzupełnij radar” (po dorzuceniu zrzutów) → w najnowszym pliku radaru zastąp miejsca `DO ZEBRANIA` nowymi sygnałami, przelicz oceny, sprawdź, czy 3 tematy i temat startowy są nadal te same (zmianę opisz), ponów kontrolę jakości.
- „Uzupełnij brief”, „nie podoba mi się żaden pomysł”, „wybieram pomysł b” → w najnowszym briefie: dobierz wypowiedzi w miejsca `DO ZEBRANIA`, przygotuj nowy pomysł na tych samych wypowiedziach (według uwagi właściciela) albo zmień wybrany pomysł w `WEJŚCIE DO RUCHU 03`; ponów kontrolę jakości.
- „Popraw wersję: …”, „wybieram wersję 2” → w Ruchu 03: popraw tylko tę wersję według jednej wskazówki, oceń ponownie, zaktualizuj decyzję i `WEJŚCIE DO RUCHU 04`.
- „Karta decyzji” → wypełnij `references/karta-decyzji.md` dla materiału, o który chodzi.
- „Skopiuj do schowka”, „skopiuj post N” → czysty tekst i kopia do schowka (sekcja „Kopiowanie do schowka” w `references/ruch-04-style-i-paczka.md`).
- „Kolejna paczka”, „następne posty” przy gotowym Ruchu 04 → ponów etapy C–E Ruchu 04 z kolejnymi sygnałami z radaru (style już są).
- „Podłącz Zernio” → sekcja o Zernio w Etapie D `references/ruch-04-style-i-paczka.md` (podłączenie po zgodzie, logowanie w przeglądarce, nigdy klucz w rozmowie).
- Wiadomość ogólna („socialmedia”) → pierwszy niegotowy ruch z tabeli. Pokaż mapę z „← jesteś tutaj”.
- Wszystkie dostępne ruchy gotowe → powiedz, co już masz, zaproponuj ponowny przebieg radaru (gdy ostatni jest starszy niż 7 dni) i poinformuj, że kolejny ruch przyjdzie z aktualizacją.

Przeczytaj plik ruchu i prowadź według niego. Właściciel może wkleić tekst zadania z lekcji (np. polecenie z Publigo): traktuj go jako zgodę na start ruchu, ale zawsze pracuj według pliku ruchu i zasad tej umiejętności.

## Krok 2. Po każdym ruchu

1. Kontrola jakości według `references/kontrola-jakosci.md`, wynik zapisany w pliku ruchu.
2. Wpis w `wyniki/social-media/dziennik.md` (co powstało, gdzie, status).
3. `wyniki/social-media/README.md`: mapa ruchów i status.
4. `stan.md` sklepu: jedna linia „Zrobione” i decyzje, które czekają na właściciela (to jest główna pamięć asystenta: inne umiejętności z niej korzystają).

## Zakończenie

Pokaż podsumowanie z pliku ruchu (każdy ruch określa, co pokazać), **dokładną ścieżkę zapisanego pliku** i jedno zdanie „Dowód ruchu” do wklejenia w społeczności. Potem jeden następny krok.

Jeśli Krok 0 wykrył nowszą wersję, a nie powiedziałeś tego na początku: "Jest nowa wersja asystenta. Napisz: aktualizuj".
