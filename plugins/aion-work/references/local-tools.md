# Przygotowanie CLI, Git i Pythona

## CLI aplikacji przed instalacją i reautoryzacją

Przy lokalnej instalacji lub aktualizacji AION WORK przygotuj CLI wybranej aplikacji, również gdy użytkownik korzysta z aplikacji desktopowej: Claude Code CLI (`claude`) dla Claude albo Codex CLI (`codex`) dla Codexa. Gdy konfiguruje obie aplikacje, przygotuj oba. Sam interfejs desktopowy nie potwierdza dostępności polecenia w terminalu agenta. Przy reautoryzacji najpierw wykorzystaj natywną akcję hosta; jeśli potrzebny jest terminal, brak CLI jest brakującym narzędziem do przygotowania, nie końcem próby połączenia.

1. Sprawdź polecenie w tym samym środowisku i profilu użytkownika co aplikacja: `claude --version` albo `codex --version`. W PowerShellu ustal ścieżkę przez `Get-Command claude` lub `Get-Command codex`; w powłoce POSIX przez `command -v claude` lub `command -v codex`. Nie przenoś konfiguracji ani poświadczeń między Windows, WSL i chmurą.
2. Jeśli CLI brakuje, w ramach zleconej instalacji lub połączenia zainstaluj je według aktualnej oficjalnej instrukcji dla wykrytego systemu i powłoki: [Claude Code CLI](https://code.claude.com/docs/en/setup) albo [Codex CLI](https://developers.openai.com/codex/cli). Użyj instalatora dostawcy lub już dostępnego, zatwierdzonego menedżera pakietów. Sprawdź wymagania wybranej metody; nie zakładaj obecności Node.js ani npm. Zachowaj działające instalacje i respektuj zgody hosta. Bez lokalnego terminala lub przy blokadzie nazwij brak i podaj jeden możliwy krok użytkownika; instalacja w chmurze nie przygotowuje jego komputera.
3. Potwierdź wersję w terminalu agenta. Po zmianie PATH otwórz nowy terminal albo użyj zweryfikowanej ścieżki programu (w PowerShellu `&` przed cytowaną ścieżką). Nie zastępuj całego PATH. Jeśli aplikacja wymaga restartu, pozostaw konkretny krok do wznowienia; nie zamykaj jej bez uzgodnienia.
4. Wróć do instalacji pluginu lub [uruchomienia OAuth](connection.md#uruchomienie-oauth). Sprawdź aktualne `mcp --help` i rzeczywisty serwer w tym profilu. Zainstalowane CLI nie dowodzi obsługi `mcp login`, wykrycia pluginu ani połączenia konta. Nie dodawaj drugiego serwera, gdy CLI nie widzi połączenia aplikacji. Logowanie i zgodę w przeglądarce kończy użytkownik.

## Git i Python dla potrzebnej czynności

Czytaj wyłącznie dla brakującego narzędzia potrzebnego do bieżącej czynności według przygotowania w `references/setup.md`. Wiedza zdalna i zwykła praca na folderze nie potrzebują Git ani Pythona. Gałąź Git wymaga Pythona 3.10+ dla [bezpiecznika zawartości](guard.md) przed commitem i pushem. Samymi operacjami Git zarządza agent. Poza tą gałęzią instaluj Python wyłącznie na prośbę użytkownika lub dla konkretnego narzędzia, które go wymaga.

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

## 3. Sprawdź i kontynuuj pracę

Uruchom wymagane polecenie w środowisku agenta. Jeśli nowy terminal je widzi, a agent nie, wyjaśnij potrzebę ponownego uruchomienia aplikacji w celu odświeżenia PATH. Zostaw krótkie podsumowanie i konkretną czynność do wznowienia. Nie instaluj ponownie działającego narzędzia ani nie zastępuj całego PATH. Restart komputera jest potrzebny tylko wtedy, gdy wymaga go instalator lub administrator.

Krok kończy się dopiero po udanym uruchomieniu wymaganych poleceń. Działający interpreter nie jest jeszcze potwierdzeniem działania konkretnego pomocnika. Kontynuuj czynność, do której potrzebne było narzędzie.
