# Narzędzia do grafiki i dołączanie do szkicu

## Sprawdzenie narzędzi

Nigdy nie pokazuj wartości kluczy.

```bash
for K in GEMINI_API_KEY GOOGLE_API_KEY OPENAI_API_KEY ZERNIO_API_KEY; do eval "V=\${$K}"; [ -n "$V" ] && echo "$K: ustawiony" || echo "$K: brak"; done; unset V
ls "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge" "/c/Program Files/Google/Chrome/Application/chrome.exe" "/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe" 2>/dev/null
```

Sprawdź też narzędzia graficzne dostępne w tej sesji, np. Canva.

| Droga | Kiedy | Koszt |
|---|---|---|
| **A. Układ HTML z prawdziwym zdjęciem albo samą typografią** | domyślnie, gdy jest Chrome albo Edge | bezpłatnie |
| **B. Scena z AI: Gemini** | ustawiony `GEMINI_API_KEY` | orientacyjnie 0,05 USD za obraz 2K, bez darmowego limitu |
| **C. Scena z AI: OpenAI** | ustawiony `OPENAI_API_KEY` | orientacyjnie 0,04–0,20 USD za obraz, zależnie od jakości |

Ceny i nazwy modeli często się zmieniają. Przed pierwszym płatnym wywołaniem sprawdź aktualną dokumentację i podaj właścicielowi koszt.

## Droga A. Układ HTML

Zapisz `wyniki/social-media/assets/[DATA]_grafika-[temat].html`. Nazwa pliku: małe litery, bez spacji i polskich znaków. Zdjęcie umieść w tym samym folderze. Podmień kolory, font, tekst i układ zgodnie z marką i wybranym pomysłem.

```html
<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Lato:wght@400;700;900&display=swap" rel="stylesheet">
<style>
  :root { --tlo:#ECDFDF; --tekst:#121212; --akcent:#8C3A55; }
  * { box-sizing:border-box; margin:0; }
  html, body { width:1080px; height:1350px; overflow:hidden; }
  body { position:relative; background:var(--tlo); color:var(--tekst); font-family:Lato,Arial,sans-serif; }
  .zdjecie { position:absolute; inset:0 0 470px 0; background:var(--akcent) center/cover no-repeat; }
  .tresc { position:absolute; left:80px; right:80px; bottom:80px; }
  h1 { font-size:92px; line-height:1.05; font-weight:900; }
  p { margin-top:28px; font-size:40px; line-height:1.25; color:var(--akcent); font-weight:700; }
</style>
</head>
<body>
  <div class="zdjecie" style="background-image:url('zdjecie-produktu.jpg')"></div>
  <div class="tresc">
    <h1>Hasło do sześciu słów</h1>
    <p>Jedna krótka linia</p>
  </div>
</body>
</html>
```

Render uruchom w folderze `assets`. Ustaw `P` na ścieżkę wykrytej przeglądarki:

```bash
P="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"; F="nazwa-pliku"; D="$(pwd)"; U="file://$(printf '%s' "$D" | sed 's/ /%20/g')/$F.html"; "$P" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 --window-size=1080,1350 --virtual-time-budget=6000 --screenshot="$D/$F.png" "$U"
```

W Windows adres zaczyna się od `file:///C:/...`. Sprawdź wymiary i wagę pliku. Na macOS zamień plik na JPEG:

```bash
sips -g pixelWidth -g pixelHeight "$F.png"; sips -s format jpeg -s formatOptions 88 "$F.png" --out "$F.jpg"; ls -lh "$F.jpg"
```

## Drogi B i C. Scena z AI

Model tworzy wyłącznie **scenę bez napisów, logo i sprzedawanego produktu**. Hasło i prawdziwe zdjęcie produktu nakładasz w układzie HTML z drogi A. Każda próba liczy się do limitu wydatku. Odpowiedź API zapisuj do pliku tymczasowego i nie pokazuj danych base64 w rozmowie.

**Gemini:** dokumentacja `https://aistudio.google.com/docs/image-generation`. Klucz w `GEMINI_API_KEY`. Ustaw proporcje `4:5`, rozmiar `2K`. Użyj przykładu REST z aktualnej dokumentacji.

**OpenAI:** dokumentacja `https://developers.openai.com/api/docs/guides/image-generation`. Klucz w `OPENAI_API_KEY`, adres `https://api.openai.com/v1/images/generations`. Wymiar `1088x1360`, bo boki muszą być wielokrotnością 16, potem przytnij do 1080 × 1350 w układzie HTML.

## Dołączanie do szkicu w Zernio

Instagram przyjmuje JPEG i PNG do 8 MB, a Facebook do 4 MB. Trzymaj plik poniżej 4 MB. Nigdy nie wysyłaj `publishNow`, `scheduledFor`, `queuedFromProfile` ani `isDraft: false`.

### Gdy Zernio jest podłączone przez logowanie

1. Wywołaj `media_generate_upload_link`. Daj właścicielowi link, ważny 30 minut, i ścieżkę pliku: „Otwórz link i przeciągnij tam ten plik. Napisz »gotowe«.” Na macOS pokaż plik w Finderze: `open -R "ścieżka"`.
2. Wywołaj `media_check_upload_status` z tokenem. Odczytaj adres pliku, gdy status to `completed`.
3. Wywołaj `posts_get` i zapamiętaj treść, platformy oraz status szkicu.
4. Przez `search_tools` znajdź narzędzie aktualizacji posta odpowiadające `PUT /v1/posts/{postId}`, które przyjmuje `mediaItems`. Samo `posts_update` nie ma pola na media. Wyślij niezmienioną treść i platformy, `mediaItems: [{"url":"ADRES","type":"image"}]` oraz `isDraft: true`.
5. Gdy takiego narzędzia nie ma: utwórz nowy szkic przez `posts_create` z tą samą treścią i kontami, `media_urls` oraz `is_draft: true`. Powiedz, że stary szkic bez grafiki nadal istnieje. Usuń go tylko po osobnej zgodzie.
6. **Odczyt kontrolny:** `posts_get`: status `draft`, treść bez zmian, adres grafiki w `mediaItems`.

Gdy posta nie ma jeszcze w Zernio, po zgodzie 3 utwórz szkic przez `posts_create` z `media_urls` i `is_draft: true`.

### Gdy ustawiony jest klucz `ZERNIO_API_KEY`

```bash
curl -sS -X POST "https://zernio.com/api/v1/media/presign" -H "Authorization: Bearer $ZERNIO_API_KEY" -H "Content-Type: application/json" -d '{"filename":"grafika.jpg","contentType":"image/jpeg"}'
curl -sS -X PUT "UPLOAD_URL" -H "Content-Type: image/jpeg" --data-binary @grafika.jpg
curl -sS "https://zernio.com/api/v1/posts/POST_ID" -H "Authorization: Bearer $ZERNIO_API_KEY"
```

Następnie wyślij `PUT https://zernio.com/api/v1/posts/POST_ID` z dotychczasową treścią i platformami, `mediaItems` z adresem `publicUrl` oraz `isDraft: true`. Potem ponów GET i wykonaj odczyt kontrolny jak wyżej. Nie używaj `curl -v`.

### Gdy Zernio nie jest podłączone

Zapisz grafikę w `assets/`, wskaż plik do ręcznego dołączenia i nazwij jeden brak: „Zernio nie jest podłączone.”
