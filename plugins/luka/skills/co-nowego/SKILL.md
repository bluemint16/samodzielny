---
name: co-nowego
description: Pokazuje, co nowego w asystencie marketingu sklepu i jakie umiejętności są dostępne. Używaj, gdy użytkownik pisze "co nowego", "co umiesz", "jakie masz umiejętności", "pomoc", "menu", "lista komend", "co potrafisz".
---

# Co nowego i co umiem

1. Przeczytaj `${CLAUDE_PLUGIN_ROOT}/CHANGELOG.md`. Jeśli ścieżka nie działa, znajdź plik poleceniem:
   ```bash
   find ~/.claude/plugins -path "*luka*" -name CHANGELOG.md 2>/dev/null | sort | tail -1
   ```
2. Pokaż użytkownikowi po ludzku dwie ostatnie wersje: co nowego i jak tego użyć (jedno zdanie przykładu na każdą nowość).
3. Pokaż menu wszystkich umiejętności:

```text
Co umiem:
- start: poznaję Twój sklep i zakładam pamięć asystenta
- branding: budujemy markę krok po kroku, kończymy brand bookiem
- seo: audyt, frazy, opisy kart i kategorii, widoczność w AI, przegląd Search Console
- aktualizuj: pobieram najnowszą wersję
- co nowego: to, co czytasz

Nie musisz pamiętać nazw. Napisz po prostu, czego potrzebujesz.
```

4. Jeśli w folderze jest `stan.md`, dodaj na końcu: "Ostatnio robiliśmy: [ostatnia linia z Zrobione]. Proponuję: [Następny krok]".
