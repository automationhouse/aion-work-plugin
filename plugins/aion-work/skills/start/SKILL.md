---
name: start
description: >-
  Połącz lub skonfiguruj AION WORK na „AION start”, „/aion-start” albo jawny
  wybór tego skilla. Samo „start” obsłuż tylko bez lokalnego przypisania
  w repo. Zwykłe zadanie, wznowienie pracy i pytanie o możliwości nie
  uruchamiają tego skilla automatycznie.
---

Najpierw rozstrzygnij [wybór procedury](../../references/routines.md#wybór-procedury-w-istniejącym-repozytorium). Dalsze kroki dotyczą wyłącznie wybranego skilla AION.

Stosuj [minimum komunikacji](../../references/communication.md). Wykorzystuj znane odpowiedzi i wyniki narzędzi. Wyraźne zlecenie samego lokalnego przeglądu przygotowanej kopii może skorzystać z opisanego niżej trybu bez MCP; nie uruchamiaj wtedy logowania tylko dla pomiaru.

1. Wykorzystaj potwierdzony dostęp do konta albo zastosuj [łączenie konta](../../references/connection.md). Przy `needs_auth`, HTTP 401 lub żądaniu ponownego logowania rozpocznij OAuth w tej rozmowie: dostępnym terminalem i obsługiwanym `claude mcp login <NAZWA>` albo natywną akcją Codexa / `codex mcp login <NAZWA> --scopes email,profile`. Użyj zwykłej przeglądarki systemowej, pokaż zwrócony link i poczekaj na zgodę. `connected` nie zastępuje udanego `get_profile`. Ręczny krok podaj dopiero po potwierdzeniu, że dostępne narzędzia nie pozwalają uruchomić logowania.
2. Po potwierdzeniu dostępu od razu pobierz rdzeń jednym wywołaniem `read_instruction({"paths":["welcome.md","communication.md","repository.md"]})`. Pomijaj tylko dokumenty już przeczytane w tej rozmowie. `welcome.md` określa domyślną pracę nad zadaniem, dobiera metodę i prowadzi powitanie, `communication.md` określa sposób rozmowy, a `repository.md` współpracę, prywatność i publikację. Nie czekaj na wzmiankę o nich w rutynie.
3. Wykonuj prośbę według rdzenia i wskazanych przez niego metod, w tej samej rozmowie. Dalsze potrzebne dokumenty czytaj razem; nowe metody odkrywaj przez `list_instructions` lub `search_instructions`, bez czytania całej bazy. Rutyny mają osobne krótkie wejścia w pluginie; ich aktualny katalog i kroki pochodzą z wiedzy. Nie kopiuj zdalnych instrukcji do skilli. Zwykłe zadanie wykonuj według `welcome.md`, bez osobnej rutyny „Dzień” i bez uruchamiania przeglądu.

Przy pierwszym przygotowaniu lub zmianie środowiska użyj [przygotowania do pierwszego zadania](../../references/setup.md); wykrywaj stan automatycznie i pytaj tylko o brak potrzebny do zlecenia. Brak profilu nie uruchamia ustawienia osobistego; po przygotowaniu od razu wykonaj znane zadanie. Samo „AION start” nie zleca tworzenia repo ani importu. Zadania i rutyny w gotowym środowisku nie uruchamiają konfiguracji ponownie. Pełny katalog repozytoriów pobieraj przez `list_team_repositories`, wybierając miejsce według przeznaczenia i niezależnych uprawnień. Do pracy firmy przekazuj potwierdzony `teamId`.

At the end of initial or resumed repository setup, before reporting completion or starting the first task, check the selected customer's repository root for `AION_INSTALLATION.md` and follow the [installation extension procedure](../../references/setup.md#repository-installation-extension). Skip a missing file silently. Ordinary tasks and returning to a prepared environment do not rerun this extension.

Operacje Git wykonuj zwykłymi narzędziami hosta według zasad firmy i [kontraktu bezpiecznika](../../references/guard.md). Nie ma obowiązkowej gałęzi pracownika. Prywatny profil, dziennik, sprawy i zgody pozostają w osobistym folderze poza synchronizacją firmy; jawne preferencje potwierdzonej osoby należą do istniejącego miejsca przyjętego przez zespół, a przy braku odpowiedniej konwencji do AION_USERS, według zdalnego `working-folder.md`. Rutyny końca dnia synchronizują osobiste repo tylko w uzgodnionym zakresie; publikacja firmowa wymaga zlecenia lub wcześniej ustalonego zakresu i respektuje reguły PR.

MIND i import Company Context pozostają dostępne przez narzędzia AION WORK z ich własnymi kontrolami uprawnień. Osobisty MIND zalogowanej osoby czytaj tylko wtedy, gdy jego dane są potrzebne do bieżącego zadania, bez dodatkowej zgody; eksport, zapis i import zachowują osobne zasady z odczytanych metod. Surowych danych MIND nie zapisuj w dokumentach firmy. Dostęp do MCP daje aktywne członkostwo firmowe albo uprawnienie abonamentowe, również legacy; sam OAuth nie wymaga firmy.

Gdy MCP jest niedostępne, nazwij brak i zachowaj pracę. Lokalny przegląd folderu wykonaj przez [health](../../references/health.md), jeśli użytkownik go zlecił. Nie zgaduj brakujących procedur OS ani nie deklaruj odczytu wiedzy. Nowa rozmowa jest potrzebna tylko przy potwierdzonym problemie załadowania narzędzi.
