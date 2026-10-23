# Kontrakt diagnostyki folderu

`health` jest przeglądem lokalnego folderu, również bez Gita. Wymaga Pythona 3.10+, bez dodatkowych pakietów. Nie blokuje commitów, nie instaluje hooków, nie łączy się z siecią i nie zapisuje stanu. Bezpiecznik publikacji jest osobnym narzędziem opisanym w `guard.md`.

## Wywołanie

Zastąp ścieżki rzeczywistymi lokalizacjami. Użyj wykrytego interpretera; na Windows przy cytowanej ścieżce programu w PowerShellu dodaj `&`.

```sh
python3 "<plugin>/scripts/health/work_health.py" "<folder>"
python3 "<plugin>/scripts/health/work_health.py" "<folder>" --baseline "<poprzedni-raport.json>"
```

Domyślne progi można zmienić argumentami `--binary-mib 10`, `--markdown-kib 64`, `--growth-kib 32`. Są to progi diagnostyczne, nie limity zabraniające pracy. Raport JSON trafia na stdout. Nie zapisuj go automatycznie w folderze zespołu; jeśli użytkownik chce zachować pomiar do porównań, uzgodnij lokalizację. Raport zawiera nazwy plików, więc sam może ujawniać strukturę pracy firmy.

## Co sprawdza

- **Duże pliki binarne:** od 10 MiB, na podstawie znanych rozszerzeń lub próbki do 8 KiB. Inny duży plik trafia do `large_file`. To rozpoznanie potencjalnego problemu, bez odczytu całego binarium ani oceny jego przydatności.
- **Duże Markdowny:** od 64 KiB; raportuje rozmiar, liczbę przeczytanych wierszy, długość najdłuższego wiersza i powtarzające się długie wiersze. Powtórzenia mogą oznaczać doklejanie tej samej treści, ale wymagają interpretacji.
- **Wzrost Markdownów:** z `--baseline` pokazuje różnicę rozmiaru względem poprzedniego raportu i zgłasza wzrost od 32 KiB. Raport musi dotyczyć tego samego folderu i wersji formatu. Bez wcześniejszego pomiaru nie twierdzi, że plik stale rośnie.
- **Odnośniki:** sprawdza istnienie lokalnych celów standardowych, jednowierszowych linków Markdown i obrazków oraz referencji z definicjami. Obsługuje względne ścieżki, ścieżki absolutne znajdujące się wewnątrz wybranego folderu, lokalne `file:` oraz zakodowane znaki w ścieżkach. Pomija przykłady w blokach kodu i fragmentach inline.

Nie pobiera adresów HTTP(S), nie sprawdza kotwic nagłówków, HTML/JSX ani pełnej składni CommonMark. Linki wielowierszowe, zagnieżdżone etykiety i specyficzna składnia edytorów, np. `[[wikilinki]]`, pozostają poza zakresem. `.mdx` jest traktowany jako tekst Markdown, bez wykonania kodu. `/docs/plik.md` nie oznacza automatycznie ścieżki względem repozytorium: poza wybranym folderem taki cel jest oznaczany jako niesprawdzony.

Nie podąża za dowiązaniami ani przekierowaniami katalogów Windows. Nie czyta celów poza wybranym folderem. Pomija prywatne katalogi z polityki AION WORK, `.env*`, `.git`, `node_modules`, środowiska Python i typowe katalogi narzędzi. Pełna lista jest w `SKIP` skryptu; pominięcia pokazuje w raporcie. Błąd dostępu lub dowiązanie oznacza zakres niesprawdzony, nie dowód nieistnienia pliku.

## Wynik i ograniczenia

Raport zawiera `findingCounts`, maksymalnie 200 szczegółowych `findings`, 20 największych plików, pomiary Markdownów oraz liczniki linków. Zwraca ścieżki, rozmiary i numery wierszy, bez fragmentów treści, etykiet linków i parametrów URL. `complete` dotyczy wyłącznie obsługiwanego zakresu. `findingsTruncated` informuje o skróceniu listy.

Limity: 100 000 wpisów, 5 000 Markdownów, do 2 MiB odczytu pojedynczego Markdowna, 64 MiB łącznych odczytów, 20 000 linków i budżet 30 sekund sprawdzany pomiędzy operacjami. Odczyt na niedostępnym dysku sieciowym może trwać dłużej. Wiersze dłuższe niż 16 384 znaków nie są parsowane pod kątem linków i są oznaczane jako niesprawdzone. Dla częściowo przeczytanego pliku wynik obejmuje tylko początek; pozostałych linków nie uznawaj za poprawne. Limity i błędy odczytu ustawiają `complete: false`. Pomiar nie jest atomowym obrazem równoczesnej edycji.

Kod zakończenia 0 oznacza wygenerowanie raportu, także z problemami lub niepełnym zakresem. Kod 1 oznacza, że nie udało się wykonać przeglądu, np. nie ma folderu albo raport porównawczy jest niewłaściwy. `health` nie zastępuje kontroli sekretów, kopii zapasowych ani decyzji o sprzątaniu.
