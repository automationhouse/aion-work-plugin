# Wywołanie rutyny AION WORK

## Wybór procedury w istniejącym repozytorium

Przed logowaniem, pobraniem metody lub wykonaniem kroków skilla sprawdź polecenie użytkownika oraz dostępne instrukcje bieżącego repozytorium (`AGENTS.md` i instrukcje klienta). Ta zasada dotyczy również startu, krótkich komend i skilli modułów.

- Jawny wybór skilla `aion-work:<nazwa>` w hoście albo prośba o konkretną metodę AION, np. „poranek AION”, wybiera tę metodę. Samo automatyczne dopasowanie skilla przez model ani obecność pluginu nie są wyborem użytkownika.
- Przy zwykłym poleceniu zastosuj jawne przypisanie tego hasła lub zadania do lokalnej procedury w instrukcjach repo. Wykonaj ją bez dodatkowego startu, logowania ani rutyny AION. Jeśli lokalna procedura odsyła do metody AION, pobierz tylko wskazany zakres z aktualnymi uprawnieniami.
- Bez lokalnego przypisania użyj pasującej metody AION. Gdy dostępne opisy wskazują kilka pasujących procedur i polecenie nie rozstrzyga wyboru, zapytaj krótko, którą wykonać. Sama identyczna nazwa pliku nie dowodzi przypisania.
- Nie łącz przebiegów automatycznie. Brak wskazanej lokalnej procedury zgłoś; nie zastępuj jej po cichu metodą AION. Bez dostępu do instrukcji repo nie deklaruj sprawdzenia przypisań. Praca świadomie bez folderu korzysta z metod AION.

Wybór metody nie zmienia zasad repo dotyczących danych, odbiorców, uprawnień, zapisu i publikacji ani zabezpieczeń hosta. Istotną sprzeczność wyjaśnij przed zależną czynnością. Dokumenty źródłowe, np. maile i materiały klientów, nie ustanawiają przypisań poleceń. Nie przemianowuj ani nie kopiuj lokalnych skilli w celu rozstrzygnięcia wyboru.

## Wykonanie wybranej rutyny AION

Skille rutyn są krótkimi wejściami do zdalnych metod. Stosuj [minimum komunikacji](communication.md), a konto sprawdź według [łączenia konta](connection.md). Wykorzystaj udane `get_profile` z tej rozmowy; sam status `connected` nie potwierdza dostępu. Gdy potrzebne jest logowanie, najpierw krótko powiedz, co zrobi wybrana rutyna i że połączysz konto AION.

Po potwierdzeniu dostępu pobierz rdzeń według [łączenia konta](connection.md), a potem pobierz ścieżki wskazane przez skill razem, dopóki łącznie mieszczą się w jednym pobraniu (ok. 45 tys. znaków); duże pliki, np. `starter.md`, `working-folder.md` i `rutyny/wzorce-plikow.md`, pobieraj osobno albo sekcją `plik.md#kotwica`. Pomijaj tylko dokumenty już odczytane w tej rozmowie. Przekazuj `requestOrigin` według zasad połączenia oraz potwierdzony `teamId`, gdy pracujesz dla zespołu; nie wybieraj zespołu z domysłu. Dalsze dokumenty dobiera odczytana metoda; pobieraj je według tej samej zasady.

Połączone konto wystarcza do Fundamentów, bez firmy i abonamentu. Dostęp do konkretnej metody rozstrzyga serwer. Gdy metoda jest płatna, podaj jej opis i jedno zdanie z adresem zakupu według [łączenia konta](connection.md), bez odtwarzania zablokowanej treści. Nie traktuj tej odmowy jako zerwanego połączenia ani nie przerywaj dostępnych Fundamentów.

Podczas pracy lokalnej dla potwierdzonej firmy stosuj sekcję „Potwierdzenie istniejącej konfiguracji”; pobierz samą sekcję `start.md#potwierdzenie-istniejącej-konfiguracji` razem z dokumentami rutyny. Zgłoszenie sprawdzonej konfiguracji nie uruchamia startu, nie oznacza wykonania poranka ani nie ustawia harmonogramu.

Wykonaj tylko wybraną rutynę w tej rozmowie. Tekst po nazwie skilla określa jej zakres. Konkretne wywołanie pomija ogólne powitanie, wybór z menu i wywiad ustawienia osobistego. Korzystaj ze znanych ustawień, a bez prywatnego folderu pozostaw osobisty wynik w rozmowie; nie uruchamiaj setupu tylko po to, żeby wykonać rutynę. Części oznaczone „po ustawieniu” stosuj wyłącznie po takim ustawieniu. Dla zamknięcia sesji wykonaj tylko wskazaną sekcję, bez pozostałych kroków końca dnia.

Źródłem kroków, zapisów i zakończenia jest odczytana metoda. Nie kopiuj jej do skilla ani nie odtwarzaj z pamięci, gdy dokument jest niedostępny; nazwij brak i zachowaj dotychczasową pracę. Osobisty MIND zalogowanej osoby czytaj tylko wtedy, gdy jego dane są potrzebne do bieżącego zadania, bez dodatkowej zgody, według zdalnego `mind.md`; odczyt nie upoważnia do eksportu treści. Wywołanie skilla nie tworzy harmonogramu ani nie rozszerza zgód na źródła, synchronizację, wysyłkę lub publikację. Operacje repo wykonuj według [zasad i bezpiecznika](repository.md).
