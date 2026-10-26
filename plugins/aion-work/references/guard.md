# Bezpiecznik zawartości AION WORK

Skrypt `scripts/guard/work_guard.py` chroni przed oczywistymi wyciekami sekretów i danych uwierzytelniających. Nie ocenia organizacji repo ani przydatności jego plików. Agent używa zwykłego Gita i przestrzega zasad repozytorium. Skrypt nie wykonuje clone, add, commit, push, merge, rebase ani reset, nie wybiera gałęzi i nie narzuca struktury dokumentów.

## Zakres

- `staged`: sprawdza cały aktualny indeks Git, czyli treści przygotowane do commita, również pliki już śledzone. Nie skanuje zamiast tego wersji roboczych.
- `pre-push`: czyta aktualizacje referencji przekazane przez Git na stdin. Kontroluje docelowe drzewa, nowe commity i ich metadane oraz metadane tagów. Usunięcie sekretu w kolejnym commicie nie usuwa go z wysyłanej historii. Dla nowej gałęzi lub nieznanego lokalnie zdalnego commita sprawdza całą osiągalną historię. Usuwanie referencji nie wysyła treści.
- `install`: instaluje lokalne hooki `pre-commit` i `pre-push` wraz z kopią skryptu i polityki w katalogu hooków Git. Nie nadpisuje cudzych hooków i nie zmienia `core.hooksPath`. Przy istniejących hookach lub własnym `core.hooksPath` zatrzymuje instalację; potrzebna jest integracja z dotychczasowym mechanizmem zespołu.
- `status`: potwierdza zgodność zainstalowanych plików i wykonywalność hooków. Zmiana wersji skryptu lub interpretera wymaga ponownej integracji; nie przedstawiaj starej instalacji jako aktualnej.

Polityka blokuje składniki ścieżek niezależnie od wielkości liter: `.git`, `.ssh`, `.aws`, `.azure`, `.gnupg`, `.kube`, pliki i katalogi zaczynające się od `.env`, standardowe nazwy prywatnych kluczy SSH oraz magazyny kluczy `.p12` i `.pfx`. Blokuje też konkretne pliki logowania `.codex/auth.json` i `.claude/.credentials.json`, również wewnątrz podfolderów. `.claude/`, `.codex/` i `.agents/` są dozwolone: instrukcje, skille i konfigurację zespołu można współdzielić według zasad repo. Sama nazwa `AION_LOCAL` lub rozszerzenie `.key` nie powodują odmowy; prywatna zawartość nadal wymaga ochrony. `.gitignore` nie zastępuje kontroli sekretów.

Zwykłe skrypty UTF-8 `.py` i `.sh` są dozwolone także w historii, jeżeli ich ścieżka i treść przechodzą kontrolę. AION WORK nie używa starego helpera `aion_git.py` ani jego poleceń `save-draft` i `update`; nie przenoś jego listy formatów do AION WORK. Nie usuwaj skryptów ani nie przepisuj historii tylko z powodu rozszerzenia.

Po przygotowaniu usunięcia pliku w indeksie `staged` nie skanuje jego dawnej wersji. `pre-push` nadal kontroluje nowe, wysyłane commity: jeżeli zawierają niedozwoloną treść, późniejsze usunięcie jej nie usuwa z historii. To inna blokada niż rozszerzenie pliku. Odmowa publikacji nie blokuje samej edycji lokalnej ani odczytu; zachowaj lokalne wyniki i wyjaśnij, czego nie wysłano.

W treści sprawdza rozpoznane wzorce kluczy prywatnych, tokenów GitHub, AWS i API oraz adresów z hasłem. Nie blokuje samego formatu JWT ani przypisania do zmiennej o nazwie `password` lub `token`: takie heurystyki mylą publiczne dane i kod z sekretami. Nie wypisuje znalezionych wartości, treści plików ani stderr Gita. Wynik JSON zawiera kod odmowy i ewentualną ścieżkę.

## Przygotowanie

Wymaga Pythona 3.10+ i dostępnego Gita. Nie wymaga dodatkowych pakietów Pythona. Użyj wykrytego interpretera w tym samym środowisku co Git. Zastąp poniższe ścieżki faktycznymi lokalizacjami; nie kopiuj placeholderów do polecenia:

```sh
python3 "<plugin>/scripts/guard/work_guard.py" install --repo "<repo>"
python3 "<plugin>/scripts/guard/work_guard.py" status --repo "<repo>"
python3 "<plugin>/scripts/guard/work_guard.py" staged --repo "<repo>"
```

Na Windows użyj potwierdzonego interpretera; dla cytowanej ścieżki programu w PowerShellu zastosuj `&`. Instalacja dotyczy wybranego repozytorium; worktree tego samego repo mogą współdzielić katalog hooków. Nie zmieniaj globalnej konfiguracji Git. Samo zbudowanie lub zainstalowanie pluginu nie podłącza hooków do repo.

Po instalacji zwykłe `git commit` i `git push` wywołują kontrolę. Nie uruchamiaj commita ani pushu tylko dla sprawdzenia gotowości. Dla własnych hooków zespołu należy zachować dotychczasowe kontrole i przekazać pełny stdin `pre-push` również do AION WORK; hook, który wcześniej zużył stdin, nie może przekazać pustego wejścia. Nie oznaczaj takiej integracji jako gotowej bez jej weryfikacji.

## Aktualizacja istniejącego guarda

Aktualizacja pluginu nie aktualizuje kopii w katalogu hooków Git. Zlecenie aktualizacji obejmujące istniejącego guarda pozwala odświeżyć tę kopię, ale nie zakładać hooków w kolejnych repozytoriach. `install` nie jest poleceniem aktualizacji i odmawia nadpisania różniących się plików.

1. Przed zmianą pluginu sprawdź tylko bieżące repo i inne repo wyraźnie wskazane przez użytkownika. Odczytaj `core.hooksPath` oraz rzeczywisty katalog hooków przez Git; nie zakładaj, że `.git` jest katalogiem w root. Nie skanuj dysku ani nie klonuj katalogu AION. Ten sam katalog hooków współdzielony przez worktree obsłuż raz. Brak instalacji AION oznacza pominięcie, nie zgodę na `install`.
2. Zachowaj poza repo lokalną kopię `pre-commit`, `pre-push`, `work-guard/work_guard.py`, `work-guard/policy.json`, ich uprawnień oraz źródeł guarda z poprzedniej wersji pluginu. Nie zapisuj do backupu sekretów ani całej konfiguracji klienta. Nie usuwaj backupu przed sprawdzeniem wyniku. Przy braku dostępu zgłoś niesprawdzone repo, bez zastępczego zapisu w innym repo.
3. Rozpoznaj standardową instalację przed zapisem: brak własnego `core.hooksPath`, zwykłe pliki bez dowiązań i przekierowań oraz oba hooki dokładnie zgodne z wrapperami generowanymi przez `installation` poprzedniego skryptu. Skrypt i polityka muszą odpowiadać źródłom tej wersji pluginu. Porównuj treść jako dane, nie wykonuj starego kodu do jej rozpoznania. Sam komentarz `AION WORK content guard` nie potwierdza pochodzenia. Jeśli brakuje zaufanego źródła poprzedniej wersji, pliki są zmodyfikowane albo istnieje integracja z hookami zespołu, pozostaw je bez zmian i opisz potrzebną integrację. Nie usuwaj hooków ani nie zmieniaj `core.hooksPath`, aby przejść kontrolę.
4. Po aktualizacji pluginu uruchom `status` z nowego skryptu dla rozpoznanej standardowej instalacji. Sukces oznacza brak potrzebnych zmian. Przy różnicy wersji i spełnionych warunkach poprzedniego kroku odśwież wyłącznie cztery pliki AION: skrypt, politykę i oba wrappery. Użyj treści nowego pakietu oraz dokładnego formatu wrapperów z jego funkcji `installation`, rzeczywistej ścieżki kopii guarda i potwierdzonego interpretera. Zachowaj prawidłowe cytowanie ścieżek i wykonywalność hooków. Przed zastąpieniem porównaj stan z backupem, aby nie nadpisać równoległej zmiany. Zapisuj przez pliki tymczasowe w tym samym katalogu i atomową podmianę każdego pliku; nie kasuj katalogu hooków.
5. Potwierdź wynik poleceniem `status` z nowego skryptu. Nie wykonuj commita ani pushu tylko dla sprawdzenia. Jeśli zapis lub weryfikacja się nie powiedzie, przywróć wyłącznie zmienione przez siebie pliki z backupu wraz z uprawnieniami, po sprawdzeniu, że nie pojawiły się cudze zmiany. Nie obchodź odmowy hosta podczas przywracania. Sprawdź zgodność przywróconych plików z backupem; przy problemie zatrzymaj dalsze zmiany i wskaż pozostały stan.
6. Raportuj osobno wersję pluginu, wynik guarda dla każdego repo i połączenie z AION. Dopuszczalne wyniki guarda to: aktualny, odświeżony i zweryfikowany, nie był podłączony, przywrócony do poprzedniej wersji lub wymaga integracji. Repo niedostępne i niestandardowe nie są zweryfikowane. `status` potwierdza pliki standardowej instalacji, nie działanie całego procesu publikacji ani niestandardowych hooków.

## Odmowa i granice

Nie zeruj kodu zakończenia, nie używaj `--no-verify`, alternatywnego `core.hooksPath`, konektora ani własnej wysyłki, żeby ominąć odmowę. Zatrzymaj publikację i wyjaśnij konkretny kod. Nie dodawaj wyjątków ani nie usuwaj historii automatycznie. Przy fałszywym alarmie potrzebny jest przegląd reguły i konkretnego przypadku, bez ujawniania sekretu w rozmowie.

Grafiki i inne pliki binarne są dozwolone. Guard szuka rozpoznawalnych tekstowych sygnatur sekretów w surowych bajtach niezależnie od rozszerzenia; nie wykonuje OCR, nie rozpakowuje archiwów ani nie dekoduje zawartości obrazów. Wskaźniki Git LFS, dowiązania i submoduły są dozwolone. Sprawdza tekst wskaźnika LFS i zapisaną ścieżkę dowiązania, ale nie pobiera obiektów LFS, nie podąża za dowiązaniami i nie skanuje zawartości submodułów. Nie przedstawiaj tych treści jako sprawdzonych.

Brak Pythona, błąd odczytu, niepełna historia lub przekroczenie budżetu skanowania nadal zatrzymują operację jako kontrolę nieukończoną, nie wykryty wyciek. Limity techniczne: 50 MiB na obiekt, 128 MiB unikalnych odczytanych obiektów, 100 000 wpisów drzew/indeksu, 10 000 commitów na aktualizację referencji i 120 sekund na wywołanie. Odczyt zawartości obiektu dopuszcza 50 MiB wyniku polecenia Git; pozostałe polecenia zachowują limit 16 MiB. Nie pomijaj takich wyników po cichu.

Wzorce nie wykryją każdego sekretu ani danych poufnych opisanych zwykłym tekstem. Lokalne hooki można świadomie ominąć; nie obejmują też zmian wysłanych bez lokalnego Gita, np. przez API GitHuba. Kontrola wymuszana po stronie serwera to osobny mechanizm. Nie obiecuj pełnej ochrony przed wyciekiem.

Praca bez folderu i zwykły folder współdzielony nie wymagają tych hooków ani Pythona. Bez gotowego bezpiecznika można czytać i edytować lokalnie; nie oznaczaj publikacji przez AION WORK jako gotowej.
