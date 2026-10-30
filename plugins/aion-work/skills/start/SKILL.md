---
name: start
description: >-
  Połącz lub skonfiguruj AION WORK na „AION start”, „/aion-start” albo jawny
  wybór tego skilla. Samo „start” obsłuż tylko bez lokalnego przypisania
  w repo. Prośbę o rozpoczęcie pracy z AION po zaproszeniu do firmy prowadź
  do pierwszego poranka i propozycji kolejnego. Zwykłe zadanie, wznowienie
  pracy i pytanie o możliwości nie uruchamiają setupu automatycznie.
---

Najpierw rozstrzygnij [wybór procedury](../../references/routines.md#wybór-procedury-w-istniejącym-repozytorium). Dalsze kroki dotyczą wyłącznie wybranego skilla AION.

Stosuj [minimum komunikacji](../../references/communication.md). Wykorzystuj znane odpowiedzi i wyniki narzędzi. Wyraźne zlecenie samego lokalnego przeglądu przygotowanej kopii może skorzystać z opisanego niżej trybu bez MCP; nie uruchamiaj wtedy logowania tylko dla pomiaru.

1. Wykorzystaj potwierdzony dostęp do konta albo zastosuj [łączenie konta](../../references/connection.md). Przy `needs_auth`, HTTP 401 lub żądaniu ponownego logowania rozpocznij OAuth w tej rozmowie: natywną akcją hosta albo terminalem według instrukcji połączenia. Jeśli potrzebne `claude` lub `codex` nie jest dostępne, najpierw przygotuj CLI według [instrukcji narzędzi](../../references/local-tools.md#cli-aplikacji-przed-instalacją-i-reautoryzacją), potwierdź wersję i obsługę logowania, a następnie wróć do OAuth. Użyj zwykłej przeglądarki systemowej, pokaż zwrócony link i poczekaj na zgodę. `connected` nie zastępuje udanego `get_profile`. Ręczny krok podaj dopiero po potwierdzeniu, że dostępne narzędzia nie pozwalają uruchomić logowania.
2. Po potwierdzeniu dostępu od razu pobierz rdzeń jednym wywołaniem `read_instruction({"paths":["welcome.md","communication.md","repository.md"]})`. Pomijaj tylko dokumenty już przeczytane w tej rozmowie. `welcome.md` określa domyślną pracę nad zadaniem, dobiera metodę i prowadzi powitanie, `communication.md` określa sposób rozmowy, a `repository.md` współpracę, prywatność i publikację. Nie czekaj na wzmiankę o nich w rutynie.
3. Wykonuj prośbę według rdzenia i wskazanych przez niego metod, w tej samej rozmowie. Gdy użytkownik prosi o rozpoczęcie pracy z AION po zaproszeniu do firmy lub wznawia tak uzgodniony start, pobierz razem `starter.md`, `rutyny/README.md`, `rutyny/poranek.md` i `rutyny/sygnaly.md`. Zastosuj sekcję „Start zaproszonego pracownika” w `starter.md`: po potrzebnym przygotowaniu przejdź do pierwszego poranka i propozycji kolejnego. Samo członkostwo, brak profilu lub cytowany mail nie wybierają tej ścieżki; inne konkretne zadanie ma pierwszeństwo. Dalsze potrzebne dokumenty czytaj razem; nowe metody odkrywaj przez `list_instructions` lub `search_instructions`, bez czytania całej bazy. Nie kopiuj zdalnych instrukcji do skilli. Zwykłe zadanie wykonuj według `welcome.md`, bez osobnej rutyny „Dzień” i bez uruchamiania przeglądu.

Przy pierwszym przygotowaniu lub zmianie środowiska użyj [przygotowania do pierwszego zadania](../../references/setup.md); wykrywaj stan automatycznie i pytaj tylko o brak potrzebny do zlecenia. Brak profilu nie uruchamia ustawienia osobistego; po przygotowaniu od razu wykonaj znane zadanie albo kontynuuj wybrany start pracownika. Samo „AION start” nie zleca tworzenia repo ani importu. Zadania i rutyny w gotowym środowisku nie uruchamiają konfiguracji ponownie. Pełny katalog repozytoriów pobieraj przez `list_team_repositories`, wybierając miejsce według przeznaczenia i niezależnych uprawnień. Do pracy firmy przekazuj potwierdzony `teamId`.

Harmonogram proponuj i wykonuj według sekcji „Ustawienie kolejnego poranka” w `rutyny/poranek.md`, tylko w uzgodnionym zakresie i dostępnym mechanizmem hosta. Sam start ani pierwszy poranek nie zlecają automatyzacji. Wznowienie nie powtarza gotowego poranka ani nie tworzy drugiego zadania. Jeśli odczytana wiedza nie zawiera tych sekcji, nazwij brak aktualnej instrukcji; nie odtwarzaj ich z pamięci ani nie uruchamiaj pełnego ustawienia osobistego w zastępstwie.

At the end of initial or resumed repository setup, before reporting completion or starting the first task, check the selected customer's repository root for `AION_INSTALLATION.md` and follow the [installation extension procedure](../../references/setup.md#repository-installation-extension). Skip a missing file silently. Ordinary tasks and returning to a prepared environment do not rerun this extension.

W gotowym lokalnym środowisku potwierdzaj konfigurację według sekcji „Potwierdzenie istniejącej konfiguracji” w `welcome.md`, bez uruchamiania wdrożenia lub dopisywania jego wcześniejszych etapów.

W ścieżce zaproszonego pracownika odczytuj i zgłaszaj postęp przez `get_onboarding_progress` i `report_onboarding_progress` według sekcji „Raportowanie etapów” w `starter.md`. Potwierdzaj tylko rzeczywiste wyniki dla zalogowanej osoby i wybranej firmy, z aktualną wersją stanu. Błąd raportowania nie blokuje pracy. Brak logowania nie pozwala raportować w czyimś imieniu; odczyt metody nie dowodzi ukończenia etapu.

Operacje Git wykonuj zwykłymi narzędziami hosta według zasad firmy i [kontraktu bezpiecznika](../../references/guard.md). Nie ma obowiązkowej gałęzi pracownika. Prywatny profil, dziennik, sprawy i zgody pozostają w osobistym folderze poza synchronizacją firmy; jawne preferencje potwierdzonej osoby należą do istniejącego miejsca przyjętego przez zespół, a przy braku odpowiedniej konwencji do AION_USERS, według zdalnego `working-folder.md`. Rutyny końca dnia synchronizują osobiste repo tylko w uzgodnionym zakresie; publikacja firmowa wymaga zlecenia lub wcześniej ustalonego zakresu i respektuje reguły PR.

MIND i import Company Context pozostają dostępne przez narzędzia AION WORK z ich własnymi kontrolami uprawnień. Osobisty MIND zalogowanej osoby czytaj tylko wtedy, gdy jego dane są potrzebne do bieżącego zadania, bez dodatkowej zgody; eksport, zapis i import zachowują osobne zasady z odczytanych metod. Surowych danych MIND nie zapisuj w dokumentach firmy. Dostęp do MCP daje aktywne członkostwo firmowe albo uprawnienie abonamentowe, również legacy; sam OAuth nie wymaga firmy.

Gdy MCP jest niedostępne, nazwij brak i zachowaj pracę. Lokalny przegląd folderu wykonaj przez [health](../../references/health.md), jeśli użytkownik go zlecił. Nie zgaduj brakujących procedur OS ani nie deklaruj odczytu wiedzy. Nowa rozmowa jest potrzebna tylko przy potwierdzonym problemie załadowania narzędzi.
