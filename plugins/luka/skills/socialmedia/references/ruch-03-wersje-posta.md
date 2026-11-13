# Ruch 03. Trzy wersje jednego posta

**Po co:** przy pisaniu najłatwiej o ogólnikowy ton AI. Dlatego nie piszesz jednego posta do poprawiania, tylko trzy wersje tego samego tematu o różnej budowie. Oceniasz je i polecasz jedną.

**Wynik ruchu:**
1. trzy wersje posta, które naprawdę różnią się budową i otwarciem,
2. ocena każdej wersji,
3. wersja rekomendowana z uzasadnieniem i decyzja właściciela,
4. kontrola jakości,
5. sekcja `WEJŚCIE DO RUCHU 04` (wersja wybrana i decyzja właściciela: materiał do zapisania jego stylów pisania; brak do dopracowania).

Pliki wiedzy: `references/otwarcia-i-formaty.md` (otwarcia, budowa wersji, formaty platform), `references/styl-bez-ai.md` (bramka stylu).

## Etap A. Rozpoznanie (tylko do odczytu)

Niczego nie zapisuj. Przeczytaj:
- najnowszy `wyniki/social-media/*_brief-tematu.md`, przede wszystkim `WEJŚCIE DO RUCHU 03` (wybrany pomysł, główna myśl, reakcja, źródła, słowa klienta, czego nie dopowiadać, od właściciela, metryka), oraz sekcję „Głos klienta”,
- **warstwę stylu sklepu**: `dane/marka.md` (ton, słowa, których używamy i unikamy, przykłady), `wyniki/branding/3_ton.md`, `wyniki/branding/test_opisu.md`. To jest głos właściciela. Nie twórz nowej warstwy stylu, jeśli te pliki istnieją. Gdy ich nie ma: weź ton z 3–5 tekstów właściciela (opisy produktów, posty w `import/`, strona sklepu) i zapisz krótką notę o tonie tylko w pliku tego ruchu,
- `dane/uvp.md` (dowody), `dane/sklep.md` (fakty o produkcie, ceny), `dane/marketing.md` (kanały).

**Gdy nie ma briefu:** nie każ nadrabiać Ruchu 02. Odtwórz minimum z plików projektu: jedno prawdziwe źródło (wypowiedź klienta z datą), główną myśl, reakcję i trzy pomysły w jednym zdaniu każdy. Zapisz je w pliku tego ruchu w sekcji „Odtworzony brief”.

**Publikator.** Sprawdź, czy w projekcie jest już skonfigurowane narzędzie do planowania i publikacji z oficjalnym API (np. Zernio, Buffer, Publer, Metricool, Later; ślady w `dane/marketing.md`, `CLAUDE.md`, `.mcp.json`, plikach konfiguracji). Powiedz jednym zdaniem, czy przed następnym ruchem właściciel musi coś założyć albo podłączyć. **Nigdy nie proś o klucz API, hasło ani token w rozmowie** i nie zapisuj ich w plikach.

Pokaż krótko: temat i wybrany pomysł, z którego briefu, jaki głos sklepu bierzesz (2–3 cechy tonu z `dane/marka.md`), zdanie o publikatorze, **plan zmian** (plik `[DATA]_wersje-posta.md`, dziennik, README, `stan.md`) i prośbę o jedno „OK”.

## Etap B. Trzy wersje

Wszystkie trzy na ten sam temat, z tą samą główną myślą, dla tej samej grupy odbiorców i na ten sam kanał (główny kanał z `dane/marketing.md`; gdy nie wiadomo: post na Instagramie z opisem).

| Wersja | Budowa |
|---|---|
| **1. Praktyczna** | konkretna pomoc, krótki proces (2–5 kroków) albo błąd, którego warto uniknąć |
| **2. Historia albo obserwacja** | prawdziwa sytuacja z prawdziwego źródła: rozmowa z klientką, zamówienie, wiadomość, coś, co właściciel zauważył. Zero zmyślonych scen, imion i dialogów. Gdy prawdziwej historii brak (pole „od właściciela” w briefie puste): zapytaj właściciela przed pisaniem albo zbuduj obserwację na dosłownych wypowiedziach klientów („W tym miesiącu trzy razy dostałam to samo pytanie: …”), tylko jeśli tak było |
| **3. Wyraźna opinia** | jasna teza sklepu, uzasadniona dowodem. Bez sztucznego konfliktu: bez wymyślonego wroga, wyśmiewania klientów i atakowania konkretnych firm |

Każda wersja musi:
1. **zaczynać się inaczej** niż pozostałe (inny typ otwarcia z `otwarcia-i-formaty.md`; pierwsze zdanie przyciąga konkretną grupę, np. zwraca się do niej wprost),
2. nieść **jedną główną myśl** z briefu,
3. używać **konkretu ze źródła** i słów klienta z briefu,
4. **nie wymyślać** liczb, klientów, opinii, wyników ani cech produktu (sprawdź listę „czego nie dopowiadać”),
5. kończyć się **naturalnym pytaniem albo następnym krokiem** dopasowanym do reakcji i metryki (np. „Napisz w wiadomości, dla kogo szukasz, podpowiem rozmiar”, gdy metryką są rozmowy),
6. przejść **bramkę stylu** z `styl-bez-ai.md` (popraw, zanim pokażesz),
7. trzymać się formatu platformy (długość, akapity, emoji i hashtagi według `otwarcia-i-formaty.md` i `dane/marka.md`).

Pod każdą wersją dopisz:
- **dowód źródeł**: które wypowiedzi i fakty z briefu wykorzystała (numery i krótkie cytaty) i z jakich plików. Wersja bez dowodu źródeł nie przechodzi,
- **typ otwarcia**,
- **propozycję grafiki lub wideo** jednym zdaniem (bez tworzenia: to późniejszy ruch).

Gdy post wspomina obniżkę, cenę promocyjną albo obietnicę o działaniu produktu: sprawdź według `${CLAUDE_PLUGIN_ROOT}/skills/meta/references/tryb-zasady.md` (najniższa cena z 30 dni, obietnice zdrowotne).

## Etap C. Ocena

Każdą wersję oceń 0–3 w pięciu kryteriach (suma 0–15), każdą ocenę uzasadnij kilkoma słowami:

| Kryterium | 0 | 3 |
|---|---|---|
| **Siła pierwszego zdania** | ogólnik, można go przewinąć | zatrzymuje właściwą osobę, mówi o jej sprawie |
| **Konkret** | przymiotniki i hasła | rzeczy, liczby i sytuacje ze źródła |
| **Wiarygodność** | obietnice bez pokrycia | każde twierdzenie ma źródło, nic nie jest przesadzone |
| **Zgodność z głosem sklepu** | brzmi jak każdy sklep albo jak AI | brzmi jak właściciel (ton i słowa z `dane/marka.md`) |
| **Szansa na wybraną reakcję** | reakcja niejasna | tekst prowadzi do reakcji z briefu i kończy się działaniem, które ją wywołuje |

## Etap D. Rekomendacja i decyzja

Poleć jedną wersję (zwykle najwyższa suma; przy remisie wiarygodność, potem pierwsze zdanie) i uzasadnij w 2–3 zdaniach. Wskaż też **największy brak** wersji rekomendowanej (jedna rzecz do dopracowania na warsztacie, np. „brak zdjęcia produktu na nadgarstku”, „pierwsze zdanie za długie”).

Poproś właściciela: „Akceptujesz wersję [X]? Możesz też dać jedną wskazówkę do poprawy albo wybrać inną.” Przy wskazówce popraw tylko tę wersję, pokaż ją ponownie i oceń jeszcze raz. Do decyzji nic nie zapisuj.

## Etap E. Zapis (po decyzji)

Plik `wyniki/social-media/[DATA]_wersje-posta.md` według szablonu z `references/szablony.md`: temat i brief, głos sklepu, trzy wersje (tekst, dowód źródeł, typ otwarcia, propozycja grafiki), ocena, rekomendacja, decyzja właściciela (wersja wybrana i ewentualna poprawka), zdanie o publikatorze, kontrola jakości, `WEJŚCIE DO RUCHU 04`:
- wersja wybrana (pełny tekst),
- jej źródła,
- brak do usunięcia na warsztacie,
- propozycja grafiki lub wideo,
- główna metryka i wynik początkowy,
- stan publikatora (jest / do założenia przed następnym ruchem).

Potem Krok 2 z `SKILL.md` (kontrola jakości, dziennik, README, `stan.md`, decyzje czekające na właściciela, np. podłączenie publikatora, zdjęcie do posta).

## Podsumowanie dla właściciela

Pokaż:
1. trzy wersje posta,
2. ocenę każdej (tabela),
3. wersję rekomendowaną z uzasadnieniem i decyzją,
4. dokładną ścieżkę zapisanego pliku,
5. wynik kontroli jakości,
6. zdanie o publikatorze,
7. jedno zdanie „Dowód ruchu”, np.: „Ruch 03 gotowy: 3 wersje posta o »[temat]«, wybieram wersję [praktyczną / historię / opinię] ([suma]/15), na warsztacie dopracuję [brak].”

**Nic nie publikujesz i nie wysyłasz.** Następny krok: Ruch 04, zapisanie trzech stylów pisania właściciela i paczka trzech postów. Wersja wybrana dzisiaj będzie jednym z wzorów stylu.
