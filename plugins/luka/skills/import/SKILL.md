---
name: import
description: Przenosi dotychczasową pracę nad sklepem z ChatGPT, Claude (claude.ai) albo Gemini do pamięci asystenta w folderze dane/. Czyta podsumowania, eksporty rozmów, instrukcje projektów i gotowe teksty z folderu import/, wybiera to, co dotyczy sklepu, i po zgodzie dopisuje do plików. Używaj, gdy użytkownik pisze "import", "przenieś moją pracę", "mam rozmowy w ChatGPT", "pracowałem w Gemini", "eksport z Claude", "wczytaj stare materiały", "przenieś historię".
---

# Import dotychczasowej pracy

Pomagasz przenieść wiedzę o sklepie z innych aplikacji AI do tego folderu. Cel: właściciel nie zaczyna od zera, a asystent zna wszystko, co już zostało ustalone.

## Zasady

1. Prosty język, krótkie zdania. Właściciel nie jest techniczny.
2. **Przenosisz tylko to, co dotyczy sklepu i marketingu.** Eksporty zawierają wszystkie rozmowy, także prywatne. Prywatnych treści nie czytasz dokładnie, nie streszczasz i nie zapisujesz.
3. **Fakty, nie domysły.** Zapisujesz tylko to, co jest w materiałach. Gdy coś jest niejasne albo sprzeczne, pytasz.
4. **Nic nie nadpisujesz.** Istniejące pliki w `dane/` uzupełniasz. Przy sprzeczności pokazujesz obie wersje i pytasz, która jest aktualna.
5. **Plan przed zapisem.** Zapis tylko po "OK".
6. Nie usuwasz plików z `import/`. Nic nie wysyłasz poza komputer.

## Krok 0. Przygotowanie

1. Raz na rozmowę sprawdź po cichu wersję:
   ```bash
   claude plugin list 2>/dev/null | grep -A4 "luka@samodzielny" | grep -i version
   curl -fsS --max-time 5 "{{BASE_URL}}/version.json"
   ```
   Jeśli dostępna wersja jest wyższa, na końcu pracy dodaj: "Jest nowa wersja asystenta. Napisz: aktualizuj". Błąd albo brak internetu = pomiń.
2. Sprawdź, czy w bieżącym folderze jest folder `import/` z plikami. Jeśli go nie ma albo jest pusty, wyjaśnij:
   "Utwórz w folderze Mój sklep folder o nazwie import i wrzuć do niego materiały z poprzedniej aplikacji: podsumowanie od starego asystenta, eksport rozmów (rozpakowany), instrukcje projektu i gotowe teksty. Instrukcja jest w materiałach społeczności. Gdy skończysz, napisz: import."
   Możesz też przyjąć tekst wklejony wprost do rozmowy. Wtedy zapisz go najpierw jako `import/wklejone_[RRRR-MM-DD].md` (po zgodzie).
3. Przeczytaj `stan.md` i `dane/`, jeśli istnieją. Jeśli nie ma `dane/sklep.md`, zapytaj tylko o nazwę i adres sklepu. Resztę spróbujesz wyciągnąć z importu, a brakujące informacje uzupełni później skill `start`.

## Krok 1. Spis materiałów

Wypisz pliki z `import/` (także w podfolderach) i rozpoznaj ich rodzaj:

| Rodzaj | Jak rozpoznać |
|---|---|
| Podsumowanie od starego asystenta | plik tekstowy lub dokument z sekcjami o sklepie, klientach, marce |
| Eksport ChatGPT | `conversations.json` albo `conversations-000.json` i kolejne, `chat.html`, `user.json` |
| Eksport Claude (claude.ai) | `conversations.json`, `projects.json`, `users.json`, czasem plik z pamięcią (memory) |
| Eksport Gemini (Google Takeout) | folder `Takeout`, w nim `Moja aktywność` / `My Activity`, podfolder `Gemini Apps` (`MojaAktywność.html` / `MyActivity.html` albo `.json`); osobno folder `Gemini` z Gemami |
| Instrukcje projektu, GPT, Gema, pamięć | krótkie pliki tekstowe skopiowane przez właściciela |
| Gotowe materiały | opisy produktów, teksty, brand book, strategie (`.md`, `.txt`, `.docx`, `.pdf`) |
| Archiwum `.zip` | rozpakuj do podfolderu `import/rozpakowane/[nazwa]` (po zgodzie), oryginał zostaw |

Pokaż spis w prostej tabeli: plik, rodzaj, wielkość. Duże eksporty (ponad kilka MB) zapowiedz: "To pełny eksport. Najpierw znajdę tylko rozmowy o sklepie."

## Krok 2. Znajdź rozmowy o sklepie (tylko dla pełnych eksportów)

Nie czytaj całego eksportu naraz. Przygotuj krótki skrypt w Pythonie (zapisz go w katalogu tymczasowym, nie w folderze właściciela), który wypisze listę rozmów: tytuł, data, liczba wiadomości.

- ChatGPT: lista obiektów z `title`, `create_time`, `mapping` (wiadomości w `mapping[*].message.content.parts`).
- Claude: lista obiektów z `name`, `created_at`, `chat_messages` (tekst w `text` albo w `content[*].text`).
- Gemini (Takeout HTML/JSON): wpisy aktywności z datą, treścią pytania i odpowiedzi. Kolejne wpisy jednego dnia na ten sam temat traktuj jak jedną rozmowę.

Formaty eksportów się zmieniają. Jeśli struktura jest inna, najpierw obejrzyj początek pliku i dopasuj skrypt.

Następnie:
1. Zaznacz rozmowy, które pasują do sklepu: nazwa sklepu, nazwy produktów i kategorii, słowa typu marka, klient, opis produktu, SEO, reklama, Instagram, newsletter, sprzedaż, cena, konkurencja. Zapytaj właściciela o 3–5 dodatkowych słów, po których rozpoznać jego tematy.
2. Pokaż listę znalezionych rozmów (tytuł, data) i zapytaj: "Te rozmowy wyglądają na pracę nad sklepem. Którą pominąć albo dodać?"
3. Czytaj wyłącznie zatwierdzone rozmowy.

## Krok 3. Wyciągnij wiedzę

Z podsumowań, instrukcji, zatwierdzonych rozmów i materiałów wypisz fakty w tych grupach. Przy każdym fakcie zapisz źródło (plik albo tytuł rozmowy i datę).

1. **Sklep i oferta** → `dane/sklep.md`: co sprzedaje, kluczowe produkty, różnice, ceny i marże, dostawa i zwroty, platforma.
2. **Klienci** → `dane/klienci.md`: grupy klientów, pytania przed zakupem, obawy, dosłowne słowa klientów.
3. **Marketing** → `dane/marketing.md`: kanały, co działało i co nie (z liczbami i datami, jeśli są), cele, budżety.
4. **Marka** → `dane/marka_z_importu.md`: wyróżnik, ton, słowa ulubione i zakazane, kolory, fonty, hasła. To materiał roboczy. Skill `branding` sprawdzi go z właścicielem i zbuduje z niego `dane/marka.md`.
5. **Gotowe teksty** → `wyniki/import/teksty.md`: opisy produktów, posty, maile, hasła, które właściciel zatwierdził albo używa. Kopiuj dosłownie.
6. **Decyzje i pomysły** → `wyniki/import/decyzje_i_pomysly.md`: co zostało ustalone, co odrzucone i dlaczego, pomysły na później.

Ważne:
- Gdy w rozmowach jest kilka wersji tego samego (np. trzy wersje hasła), weź tę, którą właściciel wybrał albo która jest najnowsza, i oznacz pozostałe jako wcześniejsze.
- Odpowiedzi starego asystenta to nie są fakty o sklepie. Faktem jest to, co powiedział właściciel albo co zatwierdził.
- Liczby (sprzedaż, wyniki reklam) przenoś tylko z datą i źródłem.

## Krok 4. Porównaj z tym, co już jest

Jeśli `dane/` już istnieje (np. po `start`):
- Nowe informacje: dopisz w sekcji `## Z importu ([źródło], [data])` na końcu właściwego pliku.
- Sprzeczności: pokaż tabelę "Teraz w dane/ | W imporcie | Źródło" i zapytaj, co jest aktualne.
- Duplikaty: pomiń.

## Krok 5. Plan i zapis

Pokaż plan:

```text
Z Twoich materiałów przeniosę:
- dane/sklep.md: [liczba] informacji (np. kluczowe produkty, dostawa)
- dane/klienci.md: [...]
- dane/marketing.md: [...]
- dane/marka_z_importu.md: [...] (wersja robocza do kroku branding)
- wyniki/import/teksty.md: [liczba] gotowych tekstów
- wyniki/import/decyzje_i_pomysly.md: [...]
Pominę: [np. 42 rozmowy niezwiązane ze sklepem, nie czytałem ich]
Do wyjaśnienia: [sprzeczności, jeśli są]

Niczego nie usuwam. Zapisać? Wystarczy OK.
```

Po zgodzie zapisz pliki. Jeśli `dane/` nie istniało, utwórz pliki według szablonów ze skilla `start` (sklep, klienci, marketing), a brakujące pola oznacz `BRAK DANYCH`. Utwórz też `stan.md` i `CLAUDE.md` tak jak w skillu `start`, jeśli ich nie ma.

Zapisz raport `import/_raport_importu_[RRRR-MM-DD].md`: jakie pliki przeczytane, które rozmowy użyte, co gdzie trafiło, co pominięte.

Dopisz do `stan.md`: "[data] import: przeniesiono pracę z [aplikacja]".

## Krok 6. Co dalej

```text
Gotowe. Przeniosłem Twoją dotychczasową pracę.

Czego brakuje: [najważniejsze BRAK DANYCH]
Proponuję:
1. start: uzupełnimy braki (asystent zapyta tylko o to, czego nie wie)
2. branding: zbudujemy brand book na bazie tego, co już masz
```

Na koniec przypomnij: "Pliki eksportu w folderze import zawierają wszystkie Twoje stare rozmowy, także prywatne. Gdy sprawdzisz, że wszystko się przeniosło, możesz je usunąć albo przenieść w bezpieczne miejsce."
