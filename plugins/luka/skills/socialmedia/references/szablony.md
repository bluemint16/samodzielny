# Szablony plików systemu social media

Wszystko w `wyniki/social-media/`. Bez nawiasów kwadratowych w gotowych plikach.

## README.md (opis systemu)

```markdown
# Maszyna social media: [NAZWA SKLEPU]

Zaktualizowano: [DATA]

## Na czym pracujemy
Oferta: [oferta]
Odbiorcy: [grupa]
Główna metryka: [metryka], wynik początkowy: [wartość albo „nieznany”] ([okres], [źródło]), ponowny pomiar: [DATA +30 dni]

## Ruchy
| Ruch | Status | Plik |
|---|---|---|
| 01. Radar tematów | [gotowe / w trakcie] | [ścieżka] |
| 02. Brief tematu | [gotowe / w trakcie / czeka] | [ścieżka] |
| 03. Trzy wersje posta | [gotowe / w trakcie / czeka] | [ścieżka] |
| 04. Style i paczka postów | [gotowe / w trakcie / czeka] | [ścieżka] |
| 05. Grafika | [czeka] | |

## Radar: jak uruchomić ponownie
Kiedy: [raz w tygodniu, dzień]
Jak: napisz „socialmedia: uruchom radar” i wrzuć nowe zrzuty do `wyniki/social-media/sygnaly/`
Ostatni przebieg: [DATA], [ścieżka]

## Decyzje, które czekają na właściciela
- [...] (albo: Brak.)
```

## dziennik.md

```markdown
# Dziennik systemu social media

## [DATA]
- Powstało: [co]
- Plik: [ścieżka]
- Status: [gotowe / do poprawy: ...]
```

Nowe wpisy dopisujesz na górze, wcześniejszych nie zmieniasz.

## [DATA]_radar-tematow.md

```markdown
# Radar tematów: [DATA]

## 1. Oferta i odbiorcy
Oferta: [...] (skąd: [plik])
Odbiorcy: [...] (skąd: [plik])
Dlaczego teraz: [sezon, cel]

## 2. Wynik początkowy
Metryka: [...]
Wartość: [liczba / nieznana]
Okres: [od–do]
Źródło: [gdzie odczytane, kto odczytał]
Ponowny pomiar: [DATA +30 dni]

## 3. Sygnały
| # | Pytanie albo problem (słowa klienta) | Źródło | Data | Dlaczego pasuje do oferty |
|---|---|---|---|---|
| 1 | „...” | ... | ... | ... |

## 4. Ocena
| # | Siła problemu | Dopasowanie | Dowód | Suma | Uzasadnienie |
|---|---|---|---|---|---|
| 1 | 0–3 | 0–3 | 0–3 | 0–9 | ... |

## 5. Trzy najmocniejsze tematy
1. **[temat z perspektywy klienta]**: sygnały [#], suma [X], pasuje: [produkt / dowód z UVP]
2. ...
3. ...

## 6. Temat startowy
[temat]. Dlaczego: [...]

## 7. Radar: ponowne uruchomienie
Kiedy: [...]
Jak: [...]
Źródła tego sklepu: [lista adresów, fraz, sklepów konkurencji]
Wykorzystane tematy: [lista]

## 8. Kontrola jakości
[wynik według kontrola-jakosci.md]

## WEJŚCIE DO RUCHU 02
Temat startowy: [zdanie]
Oferta i odbiorcy: [...]
Sygnały i źródła:
- „[cytat]” ([źródło], [data])
Główna metryka: [metryka], wynik początkowy: [wartość / nieznany]
Otwarte pytania do właściciela: [...]
```

## [DATA]_brief-tematu.md

```markdown
# Brief tematu: [DATA]

## 1. Temat
[temat] (skąd: [plik radaru, sekcja WEJŚCIE DO RUCHU 02 / pytania klientów: plik])
Oferta i odbiorcy: [...]

## 2. Głos klienta
| # | Wypowiedź (dosłownie) | Typ | Źródło | Data |
|---|---|---|---|---|
| 1 | „...” | pytanie / obiekcja / problem / po zakupie | ... | ... |

Słowa klienta: „...”, „...”, „...”

## 3. Fakty i interpretacje
| Fakt (źródło) | Interpretacja |
|---|---|
| ... ([#] / [plik]) | ... |

Usunięte jako niepotwierdzone: [... / nic]

## 4. Główna myśl
„[jedno zdanie]” (filar marki: [...])

## 5. Reakcja odbiorcy
[reakcja]. Dlaczego: [...]

## 6. Pomysły na post
### a. Praktyczny: [tytuł roboczy]
Zarys: 1) ... 2) ... 3) ...
Format: [...]
Dowód: [#, fakt]
Czego nie dopowiadać: [...]
Od właściciela: [... / nic]

### b. Historia albo obserwacja: [tytuł roboczy]
(jak wyżej)

### c. Wyrazista opinia: [tytuł roboczy]
(jak wyżej)

## 7. Rekomendacja
[pomysł]. Dlaczego: [...]

## 8. Kontrola jakości
[wynik według kontrola-jakosci.md]

## WEJŚCIE DO RUCHU 03
Wybrany pomysł: [tytuł], [typ], format: [...]
Zarys: [...]
Główna myśl: „...”
Reakcja: [...]
Źródła:
- „[cytat]” ([źródło], [data])
Słowa klienta: [...]
Czego nie dopowiadać: [...]
Od właściciela: [...]
Główna metryka: [metryka], wynik początkowy: [wartość / nieznany]
```

## [DATA]_wersje-posta.md

```markdown
# Wersje posta: [DATA]

## 1. Temat i brief
Temat: [...] (brief: [ścieżka] / odtworzony brief niżej)
Główna myśl: „...”
Reakcja: [...]
Kanał i format: [...]

## 2. Głos sklepu
[2–3 cechy tonu] (z: [dane/marka.md / nota o tonie])

## 3. Wersje
### Wersja 1. Praktyczna
[pełny tekst]

Typ otwarcia: [...]
Dowód źródeł: [#: „cytat”, plik]
Bramka stylu: [OK / Poprawiono: ...]
Grafika lub wideo: [jedno zdanie]

### Wersja 2. Historia albo obserwacja
(jak wyżej)

### Wersja 3. Opinia
(jak wyżej)

## 4. Ocena
| Kryterium | W1 | W2 | W3 |
|---|---|---|---|
| Siła pierwszego zdania | 0–3 | | |
| Konkret | | | |
| Wiarygodność | | | |
| Zgodność z głosem | | | |
| Szansa na reakcję | | | |
| Suma (0–15) | | | |

Uzasadnienia: [...]

## 5. Rekomendacja i decyzja
Rekomendowana: [wersja]. Dlaczego: [...]
Największy brak: [...]
Decyzja właściciela ([DATA]): [wersja], poprawka: [... / brak]

## 6. Publikator
[jest: nazwa / brak: co założyć przed następnym ruchem]

## 7. Kontrola jakości
[wynik według kontrola-jakosci.md]

## WEJŚCIE DO RUCHU 04
Wersja wybrana:
[pełny tekst]
Źródła: [...]
Brak do usunięcia na warsztacie: [...]
Grafika lub wideo: [...]
Główna metryka: [metryka], wynik początkowy: [wartość / nieznany]
Publikator: [jest / do założenia]
```

## Sekcja „Style pisania” w dane/marka.md (źródło prawdy)

```markdown
## Style pisania
Źródło: Ruch 04 maszyny social media ([DATA]), na podstawie: [materiały właściciela]. Ton i słowa: patrz sekcje wyżej (bez powtarzania).

### 1. [nazwa po ludzku] (praktyczny konkret)
Kiedy: [...]
Konstrukcja: otwarcie [...] / środek [...] / zakończenie [...]
Przykład otwarcia: „...”
Emocje: [...]
Nigdy: [...]

### 2. [nazwa] (historia albo obserwacja)
(jak wyżej)

### 3. [nazwa] (wyrazista teza)
(jak wyżej)
```

## reguly.md

```markdown
# Reguły pisania z decyzji właściciela

## [DATA] ([ruch])
Decyzja: [co wybrał, połączył albo poprawił]
Powód: [jego słowami]
Stosuj: [konkretna reguła]
```

Nowe reguły dopisujesz na górze. Reguła sprzeczna z wcześniejszą: zapytaj, którą zostawić, i oznacz starą jako zastąpioną.

## [DATA]_paczka-trzech-postow.md

```markdown
# Paczka trzech postów: [DATA]

## 1. Style pisania
Źródło prawdy: dane/marka.md, sekcja „Style pisania”
1. [nazwa]: [kiedy, jedno zdanie]
2. ...
3. ...

## 2. Tabela
| # | Temat | Źródło | Styl | Reakcja | Status |
|---|---|---|---|---|---|
| 1 | ... | ... | ... | ... | szkic w [publikator], id [...] / plik [ścieżka] |

## 3. Posty
### Post 1: [temat]
Karta decyzji: [skrót: dla kogo, obietnica, dowód, działanie]
Kanał: [...]

[pełny tekst]

Kontrola tekstu: [OK / poprawiono: ...]
Szkic: [id, odczyt kontrolny: zgodny / różnica] albo [plik]

### Post 2 / Post 3
(jak wyżej)

## 4. Publikator
[podłączony: nazwa / brak: posty w plikach do ręcznego wklejenia]

## 5. Reguły z decyzji
[nowe reguły i odnośnik do reguly.md / brak]

## 6. Kontrola jakości
[wynik]

## WEJŚCIE DO RUCHU 05
Post do grafiki: [#, temat]
Dlaczego: [...]
Szkic: [id w publikatorze / ścieżka pliku]
Styl, główna myśl, dowód: [...]
```

