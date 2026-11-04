# Wyniki, kalkulacje i briefy

## A. Minimalne dane od właściciela
1. WWW + branża + platforma (Shoper/WooCommerce/Shopify/Presta/inne).
2. Cel: maksymalizacja zysku / przychodu / pozyskanie klienta / wyprzedaż zapasów; produkty promocyjne, liczba SKU.
3. Miesięczny przychód, AOV, marża brutto lub koszt produktu, koszty realizacji zamówienia, stany.
4. Budżet, aktywne kanały, dotychczasowy CPA/ROAS/MER/GA4, lista e-mail.
5. Możliwości: kreacje, CRM, logistyka, analytics, osoba decyzyjna, termin zatwierdzenia.

Jeśli odpowiedzi są niepełne, działaj na **jawnych założeniach**. Nie proś o dane wrażliwe ani dostęp do kont bez potrzeby. Unikaj rozbudowanej ankiety na starcie.

## B. Karta audytu
| Wymiar | Ocena 0–2 / brak danych | Co sprawdzić | Dowód | Ryzyko | Zadanie | Właściciel | Termin |
|---|---|---|---|---|---|---|---|
| Ekonomika | | ceny, koszty, rabaty, CAC | | | | | |
| Stany | | SKU, sell-through, lead time | | | | | |
| UX/IT | | mobile, checkout, szybkość, 404 | | | | | |
| Operacje | | dostawy, pakowanie, zwroty | | | | | |
| Pomiar | | GA4/GTM/zgody/feed | | | | | |
| Reklamy | | Google/Meta/TikTok + assets | | | | | |
| CRM | | segmenty, zgody, flow | | | | | |
| Compliance | | Omnibus, regulamin, warunki | | | | | |

Wynik 0–16 to samoocena operacyjna, nie predykcja wyniku sprzedaży. Ryzyko krytyczne może zablokować publikację niezależnie od sumy.

## C. Ekonomika zamówienia / scenariusze
- Operuj na **przychodzie netto bez VAT** i spójnej bazie kosztów. Przy odmiennym ujęciu brutto/netto wskaż korektę zamiast mieszać dane.
- Wartość zamówienia netto po rabacie = cena jednostkowa netto po rabacie × ilość + ewentualne opłaty od klienta netto (ustal, czy zaliczasz dostawę).
- Kontrybucja I = przychód netto po rabacie − COGS − koszt płatności − koszt dostawy pokryty przez sklep − opakowania − koszt realizacji − oczekiwany koszt zwrotów (i inne koszty zmienne).
- Marża kontrybucyjna przed reklamą = kontrybucja I / przychód netto po rabacie.
- CPA na progu rentowności pierwszego zamówienia = kontrybucja I na zamówienie (jeśli brak innych kosztów i nie uwzględniasz LTV).
- Break-even ROAS na przychodzie netto = 1 / marża kontrybucyjna przed reklamą, jeśli marża >0. Przy marży 25% → 4,0; przy 40% → 2,5. To przykłady matematyczne, NIE benchmarks rynkowe.
- Przy budżecie 10 000 zł i założonym CPA 50 zł, model daje 200 zamówień reklamowych przed ograniczeniami atrybucji; oznacz jako **scenariusz**, nie prognozę zysku.
- Porównaj zawsze: bez promocji (baseline), wariant ostrożny, wariant ofensywny. Uwzględnij efekt kanibalizacji zakupów organicznych i zakupów, które i tak nastąpiłyby.
- Rozróżnij przychód przypisany do reklam (platformy) od sprzedaży **przyrostowej**. Dla dużych kampanii rozważ holdout/geo test. Nie sumuj ROAS i raportowanych przychodów z Meta/Google bez deduplikacji.

### Karta produktu do analizy
`SKU | nazwa | cena regularna brutto/netto | najniższa cena 30 dni | proponowana cena | COGS | pozostały koszt zmienny | zapas | oczekiwana liczba szt. | kontrybucja/szt. | CPA max | uwagi Omnibus`

## D. Warianty podziału czasu
### T-60/T-30
Zbadaj dane historyczne, zapasy i marże, przygotuj ofertę, UX, CRM, feedy, produkcję i testy kreacji.
### T-14
Sfinalizuj ceny i kreacje, uruchom teaser, e-mail warmup, audience/remarketing (jeśli legalne), test checkout/GA4.
### T-7
Ogranicz nowe eksperymenty, pilnuj poprawności feedów, finalizuj animacje/tekst, przeprowadź próbne zamówienia, przetestuj reguły rabatu.
### T-3 / akcja trwa
Wybierz produkty z najwyższą kontrybucją, wykorzystaj istniejące sprawne kampanie/CRM, usuń błędy krytyczne. Codziennie sprawdzaj stany, płatności, checkout, budżet, kontrybucję, odrzuty.

## E. Szablon wyniku strategii
1. **Executive summary:** cel, daty i 3 kluczowe ryzyka.
2. **Diagnoza:** 8 obszarów, luki i dowody.
3. **Oferta:** 2–3 mechaniki, cena, marża, zapas, ryzyko prawne.
4. **Plan kanałów:** kanał, rola w lejku, dowód z danych sklepu, KPI, budżet scenariuszowy, czego nie robić.
5. **Harmonogram:** data, działania, rezultat, właściciel, status.
6. **Asset production:** format, cel, tekst, placement, wersja, osoba zatwierdzająca.
7. **CRM:** 4–6 wiadomości z datą/segmentem/tematem/preheaderem/CTA/warunkiem prawnym; nie wysyłaj bez zgody.
8. **Monitoring:** KPI dzień po dniu, triggery stop/scale, analiza po kampanii.
9. **Lista decyzji:** max 5 konkretów do zatwierdzenia przez klienta.

## F. 5 rodzajów kreacji
- Oferta wprost: jeden wyrazisty warunek rabatu i produkt.
- Bestseller: krótka korzyść produktowa + rzeczywista cena promocyjna.
- Gift guide: prezent dla kogoś / podział wg budżetu, wyłącznie przy aktualnej dostępności.
- UGC/social proof: realne opinie za zgodą, bez fałszywych ocen.
- Countdown: wyłącznie do rzeczywistego końca akcji, bez resetowania.
Odpowiednie formaty produkcyjne wg dokumentu Blue Mint: 1080×1080, 1080×1920, 1200×1200, 1200×628; video pion 9:16 z centralną strefą bezpieczną, każdą kreację przetestować w podglądach platform.

## G. Przykładowy harmonogram e-mail (do dopasowania)
| Faza | Segment | Cel wiadomości | CTA |
|---|---|---|---|
| T-14 | zgody marketingowe, nowi i VIP | zapowiedź, inspiracja prezentowa | zobacz zapowiedź / dołącz |
| T-7 | zainteresowani kategorią | porównanie produktów / lista życzeń | zaplanuj zakupy |
| T-2 | VIP | rzeczywisty early access, jeśli istnieje | skorzystaj wcześniej |
| Start | aktywna baza | konkretna promocja, wyłączenia | zobacz ofertę |
| BF | aktywna baza, niekupujący | aktualne bestsellery, realne stany | wybierz produkt |
| CM | uprawnieni odbiorcy | przedłużenie/nowa realna akcja | skorzystaj do końca |
| Po | kupujący | onboarding, obsługa, cross-sell za zgodą | zobacz pomoc |
