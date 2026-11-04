# Testy umiejętności black-week

Uruchamiaj w `Test sklep` (albo w pustym folderze testowym), każdy test w nowej rozmowie. Sprawdzasz zachowanie asystenta, nie konkretne liczby. Źródło scenariuszy: wsad Blue Mint (listopad 2026).

| # | Wiadomość do asystenta | Oczekiwane zachowanie |
|---|---|---|
| 1 | „black week. Sklep odzieżowy, 150 tys. zł miesięcznie, marży nie znam, 12 tys. zł na reklamy, 400 produktów” | Dopytuje o marżę lub koszty, daje plan wstępny, nie podaje „bezpiecznego” rabatu, proponuje arkusz kalkulacji |
| 2 | „Jest 18 listopada, nie mam grafik, działam tylko na Meta Ads. Ułóż plan” | Tryb ratunkowy, plan na kilka dni, wykorzystanie istniejących materiałów, termin 30.10 jako minięty bez straszenia, bramka Omnibus |
| 3 | „TikTok ma ponad 27 godzin czasu miesięcznie, więc dam mu 60% budżetu” | Wyjaśnia różnicę popularności i skuteczności, proponuje mały test zamiast 60% |
| 4 | „Chcę napisać -30% od 300 zł. Najniższa cena z 30 dni to 250 zł, nowa cena 245 zł” | Oznacza RYZYKO: rabat od 250 zł to 2%, pokazuje poprawny zapis, sugeruje konsultację prawną przy wątpliwościach |
| 5 | „Do Black Friday 3 dni, kilka bestsellerów się wyprzedało” | Priorytet: stany, koszyk, newsletter, ograniczenie reklam na wyprzedane produkty |
| 6 | „Średni koszyk 200 zł brutto, koszt produktu 80 zł netto, policz zysk z reklam” | Zauważa mieszanie brutto i netto, prosi o spójne dane albo przelicza z jawnym założeniem VAT |
| 7 | „black week. 80 tys. zł miesięcznie, marży i kosztu pozyskania klienta nie znam, 10 tys. zł budżetu, 10 dni do Black Friday” | Działa na brakujących danych, ustala priorytety, szybki harmonogram, nie wymyśla liczb |
| 8 | (w folderze z `dane/marka.md` i `dane/uvp.md`) „przygotuj 5 maili na Black Week” | Ton z brand booku, oferta zgodna z UVP, miejsce na najniższą cenę z 30 dni, nic nie wysyła |
