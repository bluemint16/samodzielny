---
name: postep
description: Sprawdza, na jakim etapie pracy z asystentem jest właściciel sklepu (start, import, branding krok po kroku, zadanie domowe), pokazuje jeden następny krok i przygotowuje krótki raport do wklejenia na spotkaniu społeczności. Tylko czyta pliki, niczego nie zmienia. Używaj, gdy użytkownik pisze "postęp", "postep", "gdzie jestem", "status", "co już zrobiłem", "sprawdź zadanie domowe", "czy zadanie jest zrobione", "raport na spotkanie".
---

# Postęp: gdzie jesteś i co dalej

Ten skill tylko czyta pliki w folderze. Niczego nie zapisuje, nie poprawia i nie wysyła. Odpowiedź ma być krótka: mapa, jeden następny krok, raport do wklejenia.

## Krok 0. Sprawdź wersję (w tle)

```bash
claude plugin list 2>/dev/null | grep -A4 "luka@samodzielny" | grep -i version
curl -fsS --max-time 5 "{{BASE_URL}}/version.json"
```

Zapamiętaj zainstalowaną wersję do raportu. Jeśli dostępna jest wyższa, dodaj na końcu: "Jest nowa wersja asystenta. Napisz: aktualizuj". Błąd albo brak internetu = pomiń.

## Krok 1. Sprawdź folder

1. Sprawdź, gdzie pracujesz (`pwd`). Jeśli to katalog domowy albo Pulpit, a nie ma tu `stan.md`, powiedz: "Wygląda na to, że otwarty jest inny folder niż Twój sklep. Wybierz w Claude folder Mój sklep i napisz postęp jeszcze raz." Zakończ.
2. Sprawdź, które pliki istnieją (nie czytaj danych klientów w całości, wystarczy obecność i krótkie sprawdzenia poniżej):

| Etap | Plik | Zrobione, gdy |
|---|---|---|
| Start | `stan.md`, `dane/sklep.md`, `dane/klienci.md`, `dane/marketing.md` | wszystkie istnieją |
| Import (opcjonalny) | `import/_raport_importu_*.md` albo `dane/marka_z_importu.md` | istnieje którykolwiek |
| Branding 1. Pozycja | `wyniki/branding/1_pozycja.md` | istnieje |
| Branding 2. Filary | `wyniki/branding/2_filary.md` | istnieje |
| Branding 3. Ton | `wyniki/branding/3_ton.md` | istnieje |
| Branding 4. Wygląd | `wyniki/branding/4_wyglad.md` | istnieje |
| Branding 5. Doświadczenie | `wyniki/branding/5_doswiadczenie.md` | istnieje |
| Branding 6. Brand book | `dane/marka.md` i `wyniki/branding/test_opisu.md` | oba istnieją |
| UVP | pliki w `wyniki/uvp/`; gotowe, gdy jest `dane/uvp.md` | liczba modułów 1–6 |
| SEO | pliki w `wyniki/seo/` | istnieje którykolwiek |
| Black Week | pliki w `wyniki/black-week/` | liczba kroków 1–7 |

3. Policz w plikach `dane/*.md` wystąpienia `BRAK DANYCH`. To luki w wiedzy o sklepie.
4. Jeśli `stan.md` istnieje, przeczytaj sekcje "Zrobione" i "Następny krok".

## Krok 2. Sprawdź zadanie domowe (branding)

Tylko jeśli istnieje `dane/marka.md` albo `wyniki/branding/1_pozycja.md`. Sprawdź 4 warunki z lekcji:

1. `dane/marka.md` ma na górze sekcję "Szybki start".
2. Zdanie pozycji (w `1_pozycja.md` albo w `dane/marka.md`) jest zrozumiałe dla osoby spoza branży: bez żargonu, bez pustych haseł ("wysoka jakość", "pasja", "najlepsza obsługa"), ze wskazaniem, dla kogo jest sklep.
3. Wyróżnik ma przynajmniej jeden dowód (liczba, certyfikat, opinia, zdjęcie procesu).
4. Istnieje `wyniki/branding/test_opisu.md` z opisem przed i po.

Przy każdym warunku: spełniony albo co dokładnie brakuje (jedno zdanie). Jeśli zdanie pozycji ma puste hasła, zacytuj je i powiedz, co poprawić.

## Krok 3. Pokaż mapę

```text
Twój postęp (asystent Luka [wersja])

Start                 [zrobione / do zrobienia]
Import                [zrobione / nie dotyczy]
Branding              [X z 6 kroków]
  1. Pozycja          [✓ / –]
  2. Filary           [✓ / –]
  3. Ton głosu        [✓ / –]
  4. Wygląd           [✓ / –]
  5. Doświadczenie    [✓ / –]
  6. Brand book       [✓ / –]
UVP                   [X z 6 kroków / gotowe]
SEO                   [zaczęte / jeszcze nie]
Black Week            [X z 7 kroków / jeszcze nie]

Luki w wiedzy o sklepie: [liczba] pól "BRAK DANYCH"
```

Pod mapą, jeśli był Krok 2: wynik 4 warunków zadania domowego.

## Krok 4. Jeden następny krok

Wybierz dokładnie jeden, według kolejności:

1. Brak startu → "Napisz: start. Zajmie około 15 minut."
2. Start zrobiony, branding nie zaczęty → "Napisz: branding. Pierwszy krok to pozycja na rynku, około 20 minut. Przygotuj adresy 3 sklepów konkurencji."
3. Branding w trakcie → "Napisz: branding. Asystent zacznie od kroku [N]: [nazwa], około [15–20] minut."
4. Brand book jest, ale warunek zadania niespełniony → konkretna poprawka, np. "Dopisz dowód do wyróżnika: napisz branding i poproś o poprawkę kroku 1."
5. Zadanie domowe zrobione, UVP nie zaczęte lub w trakcie → "Gratulacje, brand book gotowy. Następny krok: uvp. Zamienimy markę w jedną obietnicę: dlaczego klient ma kupić u Ciebie."
6. UVP gotowe (`dane/uvp.md`) → "Następny krok: seo. Opisy i nagłówki pod Google powstaną wokół Twojego UVP."

Jeśli w `dane/` jest dużo `BRAK DANYCH` (5 i więcej), dodaj jedno zdanie: "Warto uzupełnić wiedzę o sklepie: napisz start i poproś o uzupełnienie braków."

## Krok 5. Raport na spotkanie

Zapytaj jednym zdaniem: "Czy coś Cię zablokowało albo z czym potrzebujesz pomocy? Napisz krótko albo: nie". Po odpowiedzi pokaż raport do skopiowania:

```text
Luka [wersja] | etap [A/B/C/D/E] | start [✓/–] | branding [X]/6 | uvp [X]/6 | następny krok: [krótko] | pomoc: [nie / treść]
```

Etapy:
- **A**: asystent nie działa albo nie ma pliku `stan.md` i `dane/` (nie zrobiony start).
- **B**: start zrobiony, branding nie zaczęty.
- **C**: branding w trakcie (1–5 z 6).
- **D**: brand book gotowy (`dane/marka.md` i `test_opisu.md`), UVP w toku albo nie zaczęte.
- **E**: UVP gotowe (`dane/uvp.md`).

Pod raportem dodaj: "Skopiuj tę linię i wklej na czacie spotkania albo w komentarzu pod lekcją. Nie zawiera danych Twoich klientów ani liczb sklepu."

Raport nie może zawierać nazw klientów, cytatów z opinii, marż ani obrotów.
