# Przygotowanie Git i Pythona

Czytaj wyłącznie dla brakującego narzędzia z wybranej gałęzi drzewa przygotowania w `references/setup.md`. Wiedza zdalna i zwykła praca na folderze nie potrzebują Git ani Pythona. Gałąź Git wymaga Pythona 3.10+ dla [bezpiecznika zawartości](guard.md) przed commitem i pushem. Samymi operacjami Git zarządza agent. Poza tą gałęzią instaluj Python wyłącznie na prośbę użytkownika lub dla konkretnego narzędzia, które go wymaga.

## 1. Najpierw wykryj środowisko

- Sprawdź, gdzie naprawdę wykonujesz polecenia. Git, interpreter i folder muszą być dostępne w tym samym środowisku. Zachowaj działającą konfigurację Windows/WSL.
- W Windows sprawdź `Get-Command git, python, py, pymanager -ErrorAction SilentlyContinue`. W powłoce POSIX użyj `command -v git` i `command -v python3`.
- Dla znalezionego Git uruchom `git --version`. Dla interpretera sprawdź `import sys; print(sys.version.split()[0]); print(sys.executable)` jego faktycznym poleceniem.
- Alias Windows Store albo menedżer Python bez interpretera nie oznacza działającego środowiska. Sprawdź zainstalowane interpretery przez wykrytego menedżera, zanim uruchomisz alias mogący otworzyć instalator.

## 2. Wybierz instrukcję dla systemu

Przed poleceniami sprawdź bieżącą oficjalną instrukcję i dostępne wersje. Pokaż użytkownikowi tylko jeden potrzebny krok, sprawdź jego wynik i dopiero wtedy podaj kolejny.

- **Windows, Git:** użyj oficjalnego [instalatora Git for Windows](https://git-scm.com/install/windows). Jeśli istnieje WinGet, najpierw sprawdź jego pomoc i pakiet `Git.Git`. Dla nowego HTTPS zachowaj Git Credential Manager; nie zastępuj działającego SSH.
- **Windows, Python:** korzystaj z [oficjalnej instrukcji instalacji](https://docs.python.org/3/using/windows.html). Wybierz wspierany stabilny interpreter zgodny z potrzebnym narzędziem. Sam menedżer nie wystarcza — potwierdź zainstalowany interpreter. Wykorzystaj istniejącego menedżera lub oficjalny instalator, bez dokładania kolejnego zestawu narzędzi.
- **macOS lub Linux:** użyj już zatwierdzonego menedżera pakietów albo oficjalnych instalatorów [Git](https://git-scm.com/install/) i [Python](https://www.python.org/downloads/). Nie instaluj menedżera pakietów tylko po to, by ominąć ustalenie dozwolonej drogi. Zachowaj systemowy Python i istniejące wersje. Ograniczenia firmowe mogą wymagać działania IT.
- **Chmura:** stosuj [ograniczenia hosta](cloud.md); instalacja dotyczy maszyny tymczasowej, nie komputera użytkownika.

## 3. Sprawdź i wróć do drzewa

Uruchom wymagane polecenie w środowisku agenta. Jeśli nowy terminal je widzi, a agent nie, wyjaśnij potrzebę ponownego uruchomienia aplikacji w celu odświeżenia PATH. Zostaw krótkie podsumowanie i numer kroku do wznowienia. Nie instaluj ponownie działającego narzędzia ani nie zastępuj całego PATH. Restart komputera jest potrzebny tylko wtedy, gdy wymaga go instalator lub administrator.

Krok kończy się dopiero po udanym uruchomieniu wymaganych poleceń. Działający interpreter nie jest jeszcze potwierdzeniem działania konkretnego pomocnika. Wróć do kroku 9 lub 10, z którego odczytano tę instrukcję.
