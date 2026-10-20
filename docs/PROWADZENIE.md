# Jak udostępnić asystenta społeczności: krok po kroku

Sześć etapów. Etapy 1–4 robisz raz (około 2–3 godzin), etap 6 przy każdej nowej umiejętności.

---

## Etap 1. Decyzje przed startem (15 minut)

1. **Nazwy.** Katalog nazywa się `samodzielny`, plugin `luka`, więc komendy to `/luka:start`, `/luka:seo`. Po starcie nie zmieniaj nazw, bo zepsujesz instalacje uczestnikom. Jeśli chcesz inne, zmień je teraz w tych miejscach:
   - `scripts/build.py` → `MARKETPLACE_NAME`
   - `plugins/luka/.claude-plugin/plugin.json` → `name` (i nazwa folderu `plugins/luka`)
   - wszystkie wystąpienia `luka@samodzielny` w `plugins/luka/skills/` i `docs/index.html`
2. **Publiczność treści.** Strona z paczką (GitHub Pages) jest publiczna: kto zna adres, pobierze pliki. Repozytorium może być prywatne, ale wtedy GitHub Pages wymaga płatnego planu GitHub Pro. Wartością społeczności są aktualizacje, prowadzenie i ludzie, a nie same pliki. Adresu nie publikuj poza społecznością.
3. **Folder projektu:** `~/Desktop/Samodzielny e-commerce/samodzielny`. Uwaga: jeśli Biurko jest synchronizowane z iCloud, przy problemach z gitem (pliki "konflikt", zablokowany commit) przenieś folder poza Biurko i Dokumenty.

## Etap 2. Test na Twoim komputerze (30 minut)

W terminalu (albo poproś Claude w zakładce Code, żeby to uruchomił):

```bash
cd ~/Desktop/"Samodzielny e-commerce"/samodzielny
claude plugin validate .
claude plugin marketplace add ./
claude plugin install luka@samodzielny-dev
```

Następnie:
1. Utwórz pusty folder testowy, np. `~/Desktop/Samodzielny e-commerce/Test sklep`, i otwórz go w Claude (zakładka Code), w nowej rozmowie.
2. Napisz `start` i przejdź cały wywiad na danych prawdziwego sklepu (najlepiej Twojego albo zaprzyjaźnionego).
3. Potem `branding` (przynajmniej moduł 1) i `seo` (audyt).
4. Zapisuj, co było niejasne albo za długie. Poprawiaj pliki w `plugins/luka/skills/` i wpisz `/reload-plugins` albo otwórz nową rozmowę. Plugin z lokalnego katalogu czyta pliki na bieżąco.

Gdy wszystko działa, usuń wersję roboczą, żeby nie dublowała się z wersją dla uczestników:

```bash
claude plugin marketplace remove samodzielny-dev
```

## Etap 3. Publikacja na GitHub (45 minut)

1. Załóż konto na github.com (jeśli nie masz).
2. Zainstaluj **GitHub Desktop** (desktop.github.com). To najprostszy sposób bez komend.
3. W GitHub Desktop: File → Add local repository → wskaż `~/Desktop/Samodzielny e-commerce/samodzielny` → "create a repository". Nazwa: `samodzielny`.
4. Kliknij **Publish repository**. Wybierz publiczne albo prywatne (patrz Etap 1, punkt 2).
5. Na github.com w repozytorium: **Settings → Pages → Build and deployment → Source: GitHub Actions**.
6. Zakładka **Actions**: uruchom "Publikacja dla uczestników" (Run workflow) albo zrób dowolny commit i push. Po 1–2 minutach powinien być zielony znaczek.
7. Sprawdź w przeglądarce:
   - `https://TWOJ-LOGIN.github.io/samodzielny/`: strona instalacji,
   - `https://TWOJ-LOGIN.github.io/samodzielny/marketplace.json`: katalog,
   - `https://TWOJ-LOGIN.github.io/samodzielny/version.json`: wersja.

Możesz też podpiąć własną domenę (np. `asystent.twojadomena.pl`) w Settings → Pages → Custom domain. Zrób to przed startem, bo adres trafia do instalacji uczestników.

## Etap 4. Test jak uczestnik (30 minut, nie pomijaj)

Na **innym komputerze** albo innym koncie użytkownika (najlepiej jeden Mac i jeden Windows):
1. Zainstaluj aplikację Claude, zaloguj się, otwórz zakładkę Code.
2. Wejdź na stronę instalacji, skopiuj wiadomość i wklej ją do Claude. Zapisz, co było trudne.
3. Sprawdź `start`, potem aktualizację: na swoim komputerze podnieś wersję na `0.1.1`, dopisz wpis w CHANGELOG, zrób push. Na testowym komputerze w nowej rozmowie zrób dowolną pracę, asystent powinien napisać "Jest nowa wersja". Napisz `aktualizuj`.
4. Sprawdź włączenie automatycznych aktualizacji (`/plugin` → Marketplaces → samodzielny → Enable auto-update) i zapisz, gdzie to jest w aplikacji desktopowej. Uzupełnij tę instrukcję dla uczestników.

To jedyny sposób, żeby wyłapać problemy, których nie widać na komputerze twórcy (brak polecenia `claude`, uprawnienia, Windows).

## Etap 5. Start w społeczności

1. **Beta (tydzień):** zaproś 5 zaangażowanych osób. Instalacja razem na krótkim spotkaniu online. Zbierz uwagi.
2. **Wideo:** nagraj 3 minuty instalacji i 5 minut pierwszego `start`. Mac i Windows osobno, jeśli różnią się kroki.
3. **Ogłoszenie:** gotowe teksty w `docs/OGLOSZENIE.md`.
4. **Wątek "Pomoc z asystentem":** jedno miejsce na problemy. Uczestnicy wklejają opis, który podaje skill `aktualizuj` przy błędzie.
5. **Spotkanie "instalujemy razem"** w pierwszym tygodniu. Rozwiązuje większość problemów naraz.

## Etap 6. Każda nowa umiejętność (stały rytm, np. co 2 tygodnie)

1. Zbierz w społeczności propozycje (ankieta, wątek). Wybierz jedną.
2. Utwórz folder `plugins/luka/skills/NAZWA/SKILL.md`. Najłatwiej z pomocą `/skill-creator` w Claude Code: opisz, co skill ma robić, a Claude napisze i przetestuje go z Tobą.
3. Trzymaj się wzorca istniejących skilli: Krok 0 (sprawdzenie wersji, czytanie `dane/` i `stan.md`), prosty język, plan przed zapisem, wyniki w `wyniki/`, linia w `stan.md`.
4. Przetestuj lokalnie (Etap 2), najlepiej też z 2–3 osobami z bety.
5. Dopisz nowy skill do menu w `plugins/luka/skills/co-nowego/SKILL.md` i do listy w `plugins/luka/skills/start/SKILL.md` (sekcja CLAUDE.md).
6. Dopisz wpis na górze `plugins/luka/CHANGELOG.md`.
7. Podnieś wersję w `plugins/luka/.claude-plugin/plugin.json`: nowa umiejętność `0.2.0`, poprawka `0.1.1`.
8. Commit i push (w GitHub Desktop: Commit, potem Push origin). Po zielonym znaczku w Actions odczekaj do 10 minut: GitHub Pages trzyma pliki w pamięci podręcznej, więc wcześniej asystenci mogą widzieć starą wersję.
9. Ogłoś w społeczności: co nowego, 2-minutowe demo, "napisz: aktualizuj".

**Bez podniesienia wersji uczestnicy nie dostaną zmian.**

## Gdy coś pójdzie nie tak

- **Zła wersja poszła do ludzi:** popraw, podnieś wersję o jeden (`0.2.1`), push. Nie cofaj numeru wersji.
- **Uczestnik ma błąd przy instalacji:** poproś o opis od asystenta. Najczęstsze przyczyny: brak polecenia `claude` w systemie, brak internetu, stara wersja Claude (zaktualizuj aplikację).
- **Chcesz usunąć umiejętność:** usuń folder skilla, wpisz w CHANGELOG, podnieś wersję.

## Później (gdy społeczność urośnie)

- **Kanał beta:** drugi katalog (`samodzielny-beta`) dla testerów, z osobnym repozytorium lub gałęzią.
- **Drugi plugin:** osobny obszar dla innej grupy (np. `reklamy` dla zaawansowanych). Dopisuje się go do `plugins/`, a `build.py` zbuduje go automatycznie.
- **Kontrola dostępu:** gdy pliki trzeba chronić, potrzebny jest serwer z logowaniem (wtedy archiwa z nagłówkami autoryzacji). To osobny projekt.
