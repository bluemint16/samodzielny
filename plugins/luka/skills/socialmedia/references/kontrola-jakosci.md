# Kontrola jakości systemu social media

Uruchamiasz po każdym ruchu i po każdym ponownym przebiegu radaru. Wynik zapisujesz w pliku ruchu (sekcja „Kontrola jakości”) i podajesz właścicielowi.

## Zawsze

1. **Nic nie zostało opublikowane ani wysłane.**
2. **Jeden system:** pliki tylko w `wyniki/social-media/`, `dane/` bez zmian.
3. **Prawdziwość:** każdy cytat i każda liczba mają źródło i datę. Żadnego cytatu nie da się uznać za wymyślony albo sklejony z kilku wypowiedzi.
4. **Prywatność:** brak imion, nazwisk, nazw prywatnych kont, adresów, numerów zamówień klientów.
5. **Nieznane to nie zero:** brakujące liczby opisane jako „nieznane” z metodą pomiaru.
6. **Ślad:** wpis w `dziennik.md`, status w `README.md`, linia w `stan.md`.

## Ruch 01. Radar tematów

7. Jest 10 sygnałów, a każdy ma 4 pola (pytanie lub problem, źródło, data, dlaczego pasuje). Miejsca `DO ZEBRANIA` są dozwolone, ale policzone i zgłoszone właścicielowi.
8. Co najmniej 3 sygnały pochodzą ze źródeł własnych sklepu (jeśli mniej: uwaga, nie błąd, z podpowiedzią, jak zebrać).
9. Każda ocena 0–3 ma uzasadnienie, sumy są policzone poprawnie.
10. 3 tematy są różne i każdy wskazuje sygnały źródłowe.
11. Temat startowy jest jednym z 3 i ma powód wyboru.
12. Nie powstał post ani gotowy tekst do publikacji.
13. Jest wynik początkowy z okresem, źródłem i datą ponownego pomiaru.
14. Jest instrukcja ponownego uruchomienia radaru i lista źródeł tego sklepu.
15. Jest sekcja `WEJŚCIE DO RUCHU 02` z tematem, źródłami i metryką.

## Ruch 02. Brief tematu

16. Jest co najmniej 5 wypowiedzi klientów (albo policzone miejsca `DO ZEBRANIA`), każda ze źródłem, datą i typem.
17. Wypowiedzi są dosłowne: bez poprawionego języka, bez dopisków, skróty oznaczone „[…]”, relacje właściciela oznaczone jako relacje.
18. Tabela fakty i interpretacje: każdy fakt ma źródło, niepotwierdzone usunięte albo oznaczone „do potwierdzenia”.
19. Jest jedna główna myśl (jedno zdanie, bez „i” łączącego dwie myśli) i jedna reakcja z uzasadnieniem.
20. 3 pomysły są wyraźnie różne (praktyczny, historia lub obserwacja, opinia) i każdy ma dowód oraz „czego nie dopowiadać”.
21. Żadna historia nie jest wymyślona: brak prawdziwej historii = szkielet z pytaniem do właściciela.
22. Nie powstał pełny post.
23. Jest rekomendacja z uzasadnieniem i sekcja `WEJŚCIE DO RUCHU 03`.

## Ruch 03. Trzy wersje posta

24. Są 3 wersje o różnej budowie (praktyczna, historia lub obserwacja, opinia) i z różnymi typami otwarcia.
25. Każda niesie tę samą główną myśl z briefu i ma dowód źródeł (numery i cytaty z briefu).
26. Żadna nie wymyśla liczb, klientów, opinii, wyników ani scen; historia ma prawdziwe źródło albo jest obserwacją na dosłownych wypowiedziach.
27. Każda kończy się jednym naturalnym pytaniem albo następnym krokiem.
28. Każda przeszła bramkę stylu (brak słów-widm, ton z `dane/marka.md`).
29. Ocena w 5 kryteriach z uzasadnieniem, sumy poprawne, rekomendacja i największy brak wskazane.
30. Jest decyzja właściciela, a plik zapisano dopiero po niej.
31. W plikach i rozmowie nie ma kluczy API, haseł ani tokenów; nic nie opublikowano.
32. Jest sekcja `WEJŚCIE DO RUCHU 04` z wersją wybraną, źródłami, brakiem i stanem publikatora.

## Ruch 04. Style i paczka postów

33. Głos oparty na 3–10 prawdziwych materiałach właściciela albo na najwyżej 3 przykładach od niego, nie na branży.
34. Są 3 style różne konstrukcją (praktyczny konkret, historia lub obserwacja, teza), każdy z nazwą, zastosowaniem, konstrukcją, emocjami i zakazami.
35. Style zapisane w jednym miejscu (`dane/marka.md`, sekcja „Style pisania”), bez powtarzania zasad tonu; w paczce tylko odnośnik.
36. Paczka: 3 różne sygnały z prawdziwym źródłem, 3 różne tematy, konstrukcje i otwarcia, każdy post w innym stylu, karta decyzji z jedną obietnicą.
37. Każdy post przeszedł twarde progi tekstu (80 znaków, kotwice wzroku, 60 znaków na punkt, źródło i jedna myśl, zero myślników).
38. Zapis dopiero po decyzji właściciela; w publikatorze tylko szkice, bez publikacji i terminu; odczyt kontrolny każdego szkicu albo nazwany brak publikatora i pliki `.txt`.
39. Decyzje właściciela zapisane jako reguły w `reguly.md`.
40. Jest sekcja `WEJŚCIE DO RUCHU 05` z postem do grafiki, powodem i identyfikatorem szkicu albo ścieżką pliku.

## Wynik

```text
KONTROLA JAKOŚCI ([DATA]): [OK / DO POPRAWY]
Spełnione: [X] z [Y]
Do poprawy: [punkt: co dokładnie, albo „nic”]
Uwagi: [np. tylko 2 sygnały własne, zbierz zrzuty wiadomości]
```

Gdy coś jest do poprawy, a możesz to naprawić sam (np. brak wpisu w dzienniku), napraw i sprawdź ponownie. Gdy wymaga właściciela (brak danych), zostaw jako uwagę.
