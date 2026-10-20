# Gdzie co zmienić: popularne platformy sklepów

Używaj jako punktu startu. Panele platform często się zmieniają. Jeśli właściciel nie widzi opisanego miejsca, wyszukaj w internecie aktualną instrukcję w pomocy platformy (np. "Shoper meta title produktu") i podaj link do źródła. Nie zgaduj nazw przycisków.

## Rozpoznanie platformy po kodzie strony

| Ślad w kodzie strony | Platforma |
|---|---|
| `cdn.shopify.com`, `Shopify.theme` | Shopify |
| `wp-content`, `woocommerce` | WooCommerce (WordPress) |
| `prestashop`, `/modules/ps_` | PrestaShop |
| `shoper`, `/environment/cache/` | Shoper |
| `idosell`, `iai-` | IdoSell |

## Shopify
- Tytuł i opis meta produktu, kategorii (kolekcji), strony: na dole edycji, sekcja "Wpis w wyszukiwarce" (Search engine listing).
- Mapa strony tworzy się automatycznie: `/sitemap.xml`.
- `robots.txt` generowany automatycznie. Zmiany przez szablon `robots.txt.liquid` w edycji kodu motywu (zadanie dla osoby technicznej).
- Dane strukturalne produktu zwykle dodaje motyw. Sprawdź kompletność.
- Weryfikacja Search Console: najprościej przez tag HTML w ustawieniach motywu albo przez rekord DNS domeny.

## WooCommerce (WordPress)
- Tytuły i opisy meta: przez wtyczkę SEO (Yoast SEO, Rank Math, SEOPress). Pole pod edycją produktu albo kategorii.
- Mapa strony: tworzona przez wtyczkę SEO (często `/sitemap_index.xml`) albo przez WordPress (`/wp-sitemap.xml`).
- `robots.txt`: edycja we wtyczce SEO.
- Brak wtyczki SEO = pierwsze zadanie: zainstalować jedną (tylko jedną).
- Weryfikacja Search Console: zwykle w ustawieniach wtyczki SEO albo Site Kit by Google.

## PrestaShop
- Tytuł i opis meta produktu: edycja produktu, zakładka SEO. Kategorie: edycja kategorii, pola meta.
- Ustawienia przyjaznych adresów: Preferencje → Ruch i SEO (nazwa menu zależy od wersji).
- Mapa strony: moduł mapy witryny Google (sprawdź, czy włączony i jak często odświeżany).

## Shoper
- Pola SEO są w edycji produktu i kategorii (sekcja SEO / pozycjonowanie). Sprawdź w pomocy Shoper aktualną ścieżkę.
- Mapa strony i `robots.txt`: ustawienia w panelu, sekcja związana z SEO. Sprawdź w pomocy.

## IdoSell
- Pola SEO przy edycji towaru i kategorii (meta tytuł, meta opis). Sprawdź w pomocy IdoSell aktualną ścieżkę.
- Mapa strony i ustawienia robotów: w ustawieniach SEO sklepu.

## Gdy platforma nie pozwala czegoś zmienić
Powiedz to wprost i daj opcje: zgłoszenie do pomocy technicznej platformy (przygotuj gotową treść zgłoszenia), osoba techniczna/agencja albo inne rozwiązanie. Nie proponuj obejść, które mogą zepsuć sklep.
