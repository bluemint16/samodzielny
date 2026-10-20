# Tryb 3. Karta produktu lub kategoria: gotowe teksty do wklejenia

Cel: kompletny zestaw tekstów dla jednej strony, gotowy do wklejenia w panel sklepu, pisany pod klienta, Google i asystentów AI jednocześnie.

## Krok 1. Zbierz materiał

1. Zapytaj o adres strony (albo nazwę produktu lub kategorii). Pobierz obecną wersję: tytuł, opis meta, H1, treść, zdjęcia i ich opisy `alt`, dane strukturalne.
2. Przeczytaj `dane/marka.md` (ton, wyróżnik, słowa zakazane) i `dane/klienci.md` (pytania i obawy).
3. Jeśli istnieje plik fraz z trybu 2 dla tej kategorii, weź przypisany temat i frazy. Jeśli nie, zbierz szybko 5–10 fraz z podpowiedzi Google (jak w `references/frazy.md`, Krok 2.1).
4. Fakty o produkcie (skład, wymiary, materiał, kraj produkcji, certyfikaty) bierz wyłącznie ze strony, pliku produktów albo od właściciela. Brakuje faktu? Zapytaj. Nie dopisuj z głowy.

## Krok 2. Napisz teksty

### Karta produktu

1. **Tytuł strony (title)**: nazwa produktu + najważniejsza cecha albo zastosowanie + ewentualnie marka sklepu. Najlepiej do około 60 znaków, żeby nie był ucięty w Google.
2. **Opis meta**: 140–160 znaków. Korzyść dla klienta, jeden konkret (np. darmowa dostawa, ręczne szycie), zaproszenie do działania.
3. **H1**: pełna nazwa produktu.
4. **Pierwsze dwa zdania opisu**: dla kogo jest produkt i jaki problem rozwiązuje. Pisz tak, żeby te zdania miały sens wyjęte z kontekstu, bo właśnie takie fragmenty cytują asystenci AI.
5. **Najważniejsze cechy**: 3–6 punktów, każda cecha z korzyścią ("bawełna organiczna, więc nie podrażnia wrażliwej skóry").
6. **Specyfikacja**: tabela z faktami (wymiary, materiał, waga, skład, pielęgnacja).
7. **Jak wybrać / jak używać**: rozmiar, dobór, zastosowanie (jeśli dotyczy).
8. **FAQ**: 3–5 prawdziwych pytań klientów z krótkimi odpowiedziami.
9. **Opisy zdjęć (alt)**: dla każdego zdjęcia jedno zdanie, co na nim widać.

### Kategoria

1. **Tytuł strony**: nazwa kategorii tak, jak szukają jej klienci, + wyróżnik albo marka sklepu.
2. **Opis meta**: jak przy produkcie.
3. **H1**: nazwa kategorii.
4. **Tekst nad produktami**: 2–3 zdania, które pomagają wybrać (nie "Witamy w kategorii...").
5. **Poradnik pod produktami**: 300–600 słów. Jak wybrać, na co zwrócić uwagę, różnice między typami, linki do podkategorii i 2–3 polecanych produktów.
6. **FAQ**: 3–5 pytań.

## Krok 3. Kontrola jakości

Sprawdź przed pokazaniem:
- [ ] Każdy fakt pochodzi ze sklepu, pliku albo od właściciela.
- [ ] Brak słów zakazanych z `dane/marka.md`, ton się zgadza.
- [ ] Frazy brzmią naturalnie, żadnego upychania (ta sama fraza najwyżej 2–3 razy w tekście).
- [ ] Pierwsze dwa zdania odpowiadają na "dla kogo i po co".
- [ ] Tekst nie powiela opisu producenta.
- [ ] Tytuł i opis meta mieszczą się w zalecanych długościach.

## Krok 4. Dane strukturalne

Najpierw sprawdź, czy platforma albo wtyczka już generuje `Product` i `BreadcrumbList` (zwykle tak). Jeśli tak, nie dodawaj drugich, tylko sprawdź, czy są kompletne. Jeśli brakuje albo są niepełne, wskaż w `references/platformy.md`, jak to uzupełnić na danej platformie. Kod JSON-LD przygotowuj tylko wtedy, gdy właściciel ma gdzie go wkleić, a platforma go nie tworzy.

Uwaga: dane strukturalne typu FAQ Google pokazuje dziś w wynikach tylko wyjątkowo. Sekcja FAQ na stronie ma sens dla klientów i asystentów AI, ale nie obiecuj z jej powodu wyróżnienia w Google.

## Wynik

Zapisz `wyniki/seo/teksty/[nazwa-strony].md` w układzie "pole w panelu → tekst":

```markdown
# [Nazwa strony], [data]
Adres: [URL]
Temat i frazy: [...]

## Tytuł strony (pole: [nazwa pola w platformie])
...
## Opis meta (pole: ...)
...
## H1 / nazwa
...
## Opis
...
## FAQ
...
## Opisy zdjęć (alt)
1. [plik] → "..."

## Przed i po
| Element | Teraz | Proponuję |
|---|---|---|
```

Na koniec powiedz, gdzie to wkleić w platformie właściciela (`references/platformy.md`) i jak sprawdzić efekt: po 3–4 tygodniach w Search Console, raport Skuteczność, filtr na tę stronę.
