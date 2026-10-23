# Bezpiecznik zawartości AION WORK

Skrypt `scripts/guard/work_guard.py` kontroluje zawartość. Agent używa zwykłego Gita i przestrzega zasad repozytorium. Skrypt nie wykonuje clone, add, commit, push, merge, rebase ani reset, nie wybiera gałęzi i nie narzuca struktury dokumentów.

## Zakres

- `staged`: sprawdza cały aktualny indeks Git, czyli treści przygotowane do commita, również pliki już śledzone. Nie skanuje zamiast tego wersji roboczych.
- `pre-push`: czyta aktualizacje referencji przekazane przez Git na stdin. Kontroluje docelowe drzewa, nowe commity i ich metadane oraz metadane tagów. Usunięcie sekretu w kolejnym commicie nie usuwa go z wysyłanej historii. Dla nowej gałęzi lub nieznanego lokalnie zdalnego commita sprawdza całą osiągalną historię. Usuwanie referencji nie wysyła treści.
- `install`: instaluje lokalne hooki `pre-commit` i `pre-push` wraz z kopią skryptu i polityki w katalogu hooków Git. Nie nadpisuje cudzych hooków i nie zmienia `core.hooksPath`. Przy istniejących hookach lub własnym `core.hooksPath` zatrzymuje instalację; potrzebna jest integracja z dotychczasowym mechanizmem zespołu.
- `status`: potwierdza zgodność zainstalowanych plików i wykonywalność hooków. Zmiana wersji skryptu lub interpretera wymaga ponownej integracji; nie przedstawiaj starej instalacji jako aktualnej.

Polityka blokuje składniki ścieżek niezależnie od wielkości liter: `AION_LOCAL`, `.git`, `.ssh`, `.aws`, `.azure`, `.gnupg`, `.kube`, `.codex`, `.claude`, `.agents`, pliki i katalogi zaczynające się od `.env`, standardowe nazwy prywatnych kluczy SSH oraz rozszerzenia `.key`, `.p12`, `.pfx`. `.github`, `.gitignore`, `.gitattributes`, kod i zwykłe dokumenty tekstowe są dozwolone, o ile przejdą kontrolę treści. `.gitignore` nie zastępuje tej kontroli.

Zwykłe skrypty UTF-8 `.py` i `.sh` są dozwolone także w historii, jeżeli ich ścieżka i treść przechodzą kontrolę. AION WORK nie używa starego helpera `aion_git.py` ani jego poleceń `save-draft` i `update`; nie przenoś jego listy formatów do AION WORK. Nie usuwaj skryptów ani nie przepisuj historii tylko z powodu rozszerzenia.

Po przygotowaniu usunięcia pliku w indeksie `staged` nie skanuje jego dawnej wersji. `pre-push` nadal kontroluje nowe, wysyłane commity: jeżeli zawierają niedozwoloną treść, późniejsze usunięcie jej nie usuwa z historii. To inna blokada niż rozszerzenie pliku. Odmowa publikacji nie blokuje samej edycji lokalnej ani odczytu; zachowaj lokalne wyniki i wyjaśnij, czego nie wysłano.

W treści sprawdza rozpoznane wzorce kluczy prywatnych, tokenów GitHub, AWS, API, JWT, adresów z hasłem oraz literalnych przypisań haseł i tokenów. Nie wypisuje znalezionych wartości, treści plików ani stderr Gita. Wynik JSON zawiera kod odmowy i ewentualną ścieżkę.

## Przygotowanie

Wymaga Pythona 3.10+ i dostępnego Gita. Nie wymaga dodatkowych pakietów Pythona. Użyj wykrytego interpretera w tym samym środowisku co Git. Zastąp poniższe ścieżki faktycznymi lokalizacjami; nie kopiuj placeholderów do polecenia:

```sh
python3 "<plugin>/scripts/guard/work_guard.py" install --repo "<repo>"
python3 "<plugin>/scripts/guard/work_guard.py" status --repo "<repo>"
python3 "<plugin>/scripts/guard/work_guard.py" staged --repo "<repo>"
```

Na Windows użyj potwierdzonego interpretera; dla cytowanej ścieżki programu w PowerShellu zastosuj `&`. Instalacja dotyczy wybranego repozytorium; worktree tego samego repo mogą współdzielić katalog hooków. Nie zmieniaj globalnej konfiguracji Git. Samo zbudowanie lub zainstalowanie pluginu nie podłącza hooków do repo.

Po instalacji zwykłe `git commit` i `git push` wywołują kontrolę. Nie uruchamiaj commita ani pushu tylko dla sprawdzenia gotowości. Dla własnych hooków zespołu należy zachować dotychczasowe kontrole i przekazać pełny stdin `pre-push` również do AION WORK; hook, który wcześniej zużył stdin, nie może przekazać pustego wejścia. Nie oznaczaj takiej integracji jako gotowej bez jej weryfikacji.

## Odmowa i granice

Nie zeruj kodu zakończenia, nie używaj `--no-verify`, alternatywnego `core.hooksPath`, konektora ani własnej wysyłki, żeby ominąć odmowę. Zatrzymaj publikację i wyjaśnij konkretny kod. Nie dodawaj wyjątków ani nie usuwaj historii automatycznie. Przy fałszywym alarmie potrzebny jest przegląd reguły i konkretnego przypadku, bez ujawniania sekretu w rozmowie.

Brak Pythona, błąd odczytu, niepełna historia, przekroczenie limitu lub nieskanowalna treść blokują operację. Ta wersja skanuje tekst UTF-8; odmawia plików binarnych, wskaźników Git LFS, dowiązań i submodułów. Limity: 5 MiB na obiekt, 128 MiB unikalnych odczytanych obiektów, 100 000 wpisów drzew/indeksu, 10 000 commitów na aktualizację referencji i 120 sekund na wywołanie. Nie pomijaj zablokowanych plików po cichu.

Wzorce nie wykryją każdego sekretu ani danych poufnych opisanych zwykłym tekstem. Lokalne hooki można świadomie ominąć; nie obejmują też zmian wysłanych bez lokalnego Gita, np. przez API GitHuba. Kontrola wymuszana po stronie serwera to osobny mechanizm. Nie obiecuj pełnej ochrony przed wyciekiem.

Praca bez folderu i zwykły folder współdzielony nie wymagają tych hooków ani Pythona. Bez gotowego bezpiecznika można czytać i edytować lokalnie; nie oznaczaj publikacji przez AION WORK jako gotowej.
