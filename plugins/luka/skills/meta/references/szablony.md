# Szablony plików kampanii

Wszystkie pliki w `wyniki/meta-ads/`. Czytasz cały plik, zmieniasz, zapisujesz cały. Bez komentarzy z nawiasami kwadratowymi w gotowym pliku.

## wyniki/meta-ads/README.md

```markdown
# Reklamy Meta: [NAZWA SKLEPU]

Doświadczenie z reklamami Meta: [wcale / trochę / dużo]
Konto reklamowe i strona na Facebooku: [nazwa, jeśli znana / BRAK DANYCH]
Instagram połączony z kontem: [@nazwa / nie / BRAK DANYCH]
Zaktualizowano: [DATA]

## Fundamenty

- [✓/–] Piksel Meta na stronie sklepu: [działa / nie ma / nie wiadomo]; Conversions API i deduplikacja: [działa / nie ma / nie wiadomo]
- [✓/–] Progi rentowności: Max CPA [kwota] zł, BE ROAS [liczba] (z [kalkulator / wzór], [DATA])
- [✓/–] Profil na Instagramie i Facebooku: [żywy / do odświeżenia]
- [✓/–] Wykluczenie kupujących: [lista klientów / kupujący z piksela X dni / brak]

## Kampanie

| Kampania | Etap | Ostatnie działanie | Następne działanie (kto) | Data |
|---|---|---|---|---|
| [nazwa] | [wywiad / plan / reklamy / ustawienie / działa / wstrzymana / zakończona] | [...] | [...] | [DATA] |
```

## kampanie/<nazwa>/stan.md

```markdown
# Stan: [nazwa]

Etap: [etap]
Zaktualizowano: [DATA]

## Otwarte rekomendacje
- R1 ([DATA]): [co] - na podstawie: [dowód] - czeka na decyzję
(albo: Brak.)

## Ostatnia analiza
[DATA, okres danych, jedno zdanie] (albo: Jeszcze nie było.)
```

## kampanie/<nazwa>/plan.md

```markdown
# Plan: [nazwa]

Wersja: [n], [DATA]

## Cel i miara sukcesu
## Oferta i produkty
## Odbiorcy
## Budżet i czas
## Strona docelowa
## Co liczymy (zdarzenie i czy piksel je widzi)
## Reklamy (kąt, tekst, nagłówek, przycisk, grafika)
## Plan testu
## Czego nie wiemy (założenia)
```

Niewiadome sekcje: „Jeszcze nieustalone. Ustali to etap planu.”

## kampanie/<nazwa>/decyzje.md

Tylko dopisywanie na końcu. Jedyna dozwolona zmiana wcześniejszego wpisu: uzupełnienie „Wynik: czeka” po fakcie.

```markdown
### [DATA] - [krótko, np. Etap: plan → reklamy]
- Rekomendacja: [co i dlaczego]
- Podstawa: [prośba właściciela / analiza z DATA, okres danych / plik z wynikami]
- Decyzja: [kto zdecydował]
- Wynik: [zrobione / czeka]
```

## Liczby

- Decyzje Luki i właściciela zapisuj zwykłymi liczbami („50 zł dziennie przez 14 dni”).
- Liczby z Menedżera reklam zapisuj jako obserwację z okresem i źródłem:
  `- Zaobserwowano: koszt zakupu 41 zł, 2 reklamy [okres 2026-11-10..2026-11-16; źródło: eksport z Menedżera reklam z 2026-11-17]`
- Nigdy nie nazywaj obserwacji „aktualną”. To zdjęcie z dnia.
