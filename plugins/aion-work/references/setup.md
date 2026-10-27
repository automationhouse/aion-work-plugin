# Przygotowanie AION WORK do pierwszego zadania

## Cel i zakres

Połącz konto, przygotuj miejsce pracy z dostępnych źródeł i przejdź do zadania. Gotowość oznacza możliwość wykonania zleconej pracy, nie ukończony profil, pełny Company Context ani skonfigurowane rutyny. Personalizacja nie jest etapem setupu.

Najpierw sprawdź stan narzędziami i wykorzystaj ustalenia rozmowy. Nie prowadź ankiety „to czy to”, nie pokazuj numerowanych etapów i nie pytaj o wybory, które wynikają ze zlecenia. Zwykłe zadanie wykonuj od razu; przygotuj tylko brak potrzebny do jego realizacji. Samo „co potrafisz?” nie zleca setupu. Samo „AION start” sprawdza dostęp i znane miejsce, a następnie pyta o pierwsze zadanie; nie upoważnia do zakładania repo, importu ani profilu.

Przy zleceniu przygotowania miejsca pracy przedstaw jedną konkretną propozycję na podstawie rozpoznanego stanu: zespół, folder lub repo, źródła i odbiorcy. Wykonaj zakres już upoważniony. Zapytaj tylko o brak uniemożliwiający następne działanie, istotną sprzeczność lub nieuzgodniony dostęp do danych. Zgody systemu i dostawców pozostają w ich oknach. Milczenie nie oznacza zgody. Nie proś o hasła, tokeny ani kody.

Pliki i foldery z prefiksem `AION_` oraz ich zawartość zmienia agent na zlecenie użytkownika. Nie proponuj ręcznej edycji. Prefiks nie nadaje uprawnień ani prywatności.

## Sprawdź dostęp i środowisko

- Wykorzystaj [połączenie AION WORK](connection.md): potwierdź `get_profile`, odczytaj razem `welcome.md`, `communication.md`, `repository.md`, pomijając treści już przeczytane. Dostęp daje aktywne członkostwo firmowe albo uprawnienie abonamentowe, również legacy. Nie wybieraj ani nie twórz Workspace.
- Przy wymaganym logowaniu rozpocznij obsługiwany OAuth i pozostaw użytkownikowi zgodę. Nie rozpoczynaj kolejnych prób, gdy jedna trwa. Przy braku narzędzi lub odmowie nazwij blokadę i jeden dostępny krok. Zachowaj niezależną, upoważnioną pracę; nie uruchamiaj zastępczego wywiadu o środowisku.
- Ustal możliwości hosta: pliki, terminal, sieć i trwałość wyników. Nie pytaj o system operacyjny ani lokalność tylko dla analityki. Przekazuj `requestOrigin` według [kontraktu połączenia](connection.md), z `unknown` dla nieznanego wymiaru. Sama nazwa aplikacji nie dowodzi środowiska.
- Dla chmury sprawdź [ograniczenia hosta](cloud.md). Gdy trzeba udostępnić folder, wskaż jeden rzeczywisty krok w hoście. Bez trwałego miejsca pracuj w rozmowie, bez obietnicy zachowania plików.
- Wiedza i zadania bez plików nie wymagają folderu, GitHuba, Gita, Pythona ani osobistego profilu.

## Wybierz właściwe miejsce bez ponownej konfiguracji firmy

1. Wykorzystaj zespół wskazany przez użytkownika w tej rozmowie i zweryfikuj go przez `list_teams`. Nazwa i ID w istniejącym `AGENTS.md` pomagają zaproponować zespół, lecz nie zastępują wyboru ani członkostwa. Przy niejasności zapytaj o właściwy zespół, proponując rozpoznaną firmę. Nie wybieraj go z samego członkostwa, nawet jedynego. Bez zespołu pomijaj `teamId`; aktywność pozostaje poza raportami firmy.
2. Dla wybranego zespołu pobierz pełny `list_team_repositories`, niezależnie od jego typu. Używaj potwierdzonego `teamId` w chronionych wywołaniach katalogu i wiedzy. Narzędzia MIND i importu Company Context nie przyjmują `teamId`. Zmiana firmy wymaga zmiany kontekstu i katalogu.
3. Odczytaj istniejące instrukcje dostępnego folderu, jego przeznaczenie i remote. Wykorzystaj właściwą kopię. W przeciwnym razie wybierz repo z katalogu według opisu zadania; główne jest domyślne tylko wtedy, gdy pasuje. Przy kilku pasujących miejscach zapytaj o różnicę istotną dla pracy. Brak opisu wymaga wyjaśnienia przeznaczenia przed zapisem, a nie konfiguracji całej firmy.
4. Sprawdź dostęp do potrzebnego repo kontem użytkownika według [GitHuba](github.md). Prawo odczytu, zapisu i dostęp terminala są osobne. Nie klonuj całego katalogu. Nie ponawiaj tej samej odmowy ani nie twórz zastępczego repo po 403/404. Poufne dane nie mogą trafić do szerzej dostępnego miejsca zamiast niedostępnego właściwego repo.
5. Gdy potrzebna jest kopia, zaproponuj konkretną nową lokalizację w udostępnionym miejscu albo wykorzystaj wskazaną przez użytkownika. Nie nadpisuj istniejących plików. Dla [folderu współdzielonego](shared-folder.md) zachowaj mechanizm dostawcy, bez dodawania Gita. Przy nieznanych zasadach wspólnej edycji przygotowuj osobne pliki wynikowe, zanim uzgodnisz zmianę wspólnych danych.

Dołączający pracownik korzysta z istniejącego repo, kontekstu i zasad firmy. Nie pyta się go ponownie o administratora, strukturę firmy, model współdzielenia ani wszystkich współpracowników. Brak osobistego profilu nie oznacza braku konfiguracji firmy.

## Gdy miejsce dopiero ma powstać

Pusty katalog AION nie dowodzi braku repo. Najpierw sprawdź wskazane źródła i ustalenia. Jeśli miejsca nie da się ustalić, poproś o jeden link lub wskazanie osoby zarządzającej. Nadal wykonuj zadanie w dostępnym zakresie.

Przy zleceniu nowego repo przygotuj jedną propozycję: rzeczywisty właściciel, nazwa, prywatna widoczność, administrator i odbiorcy z zakresem uprawnień. Zaproponuj nazwę; nie wymagaj jej wymyślania. Nie zgaduj właściciela ani odbiorców z samego członkostwa w AION. Brakujące dane zbierz w krótkiej, konkretnej prośbie zamiast pięciu kolejnych pytań. Przed utworzeniem sprawdź, czy repo już istnieje. Jeśli zlecenie nie obejmuje konkretnych warunków utworzenia i dostępu, pokaż całą propozycję do zatwierdzenia.

Dla firmy wybierz uzgodnioną organizację GitHub; nie umieszczaj jej pracy domyślnie na osobistym koncie pracownika. Rejestrację konta, organizację, zaproszenia i SSO prowadź według [GitHuba](github.md) tylko wtedy, gdy są potrzebne. Administrator przygotowuje miejsce i zasady raz dla zespołu. Nie wymagaj od pracownika tworzenia własnej kopii konfiguracji organizacji.

## Przygotuj dokumenty z dostępnych źródeł

Odczytaj z MCP `starter.md`, `working-folder.md` oraz potrzebne metody Company Context razem. Zachowaj strukturę i istniejące reguły. Zlecenie przygotowania wskazanego folderu obejmuje lokalne instrukcje i dokumenty tego zakresu; nie pytaj osobno o każdy plik.

- Zapisz zwięzły `AGENTS.md`: rdzeń AION, komunikacja, ochrona danych, zasady współdzielenia, potwierdzone przypisanie zespołu lub jawny brak przypisania. Jeśli użytkownik wybrał już zespół dla tego folderu, nie potwierdzaj go ponownie. Nie zapisuj niezweryfikowanego ID ani placeholderów.
- Z katalogu przepisz dokładny adres i opis pasującego repo jako dane o przeznaczeniu. Przy aktualizacji odśwież opis, zachowując pozostałe reguły; błąd odczytu lub brak wpisu nie pozwala usuwać istniejącego opisu. Dla Claude Code zachowaj `CLAUDE.md` i dodaj brakujące `@AGENTS.md`. Opisy zawartości należą do README. Stosuj kopie wzorców i rozwiązywanie konfliktów z `working-folder.md`.
- Buduj wiedzę firmy z materiałów wskazanych do tej pracy i faktycznie dostępnego kontekstu rozmowy. Przy zleceniu budowy repo z dostępnych materiałów odkryj Company Context zgodnie ze `starter.md` i metodą `company-context/import-z-aion-work.md`. Zlecony import z rozstrzygniętym źródłem, celem i odbiorcami wykonaj bez osobnych potwierdzeń sekcji. Samo logowanie lub „AION start” nie zleca importu.
- Zapisuj fakty ze źródłem i datą, oddzielaj założenia i konflikty. Nie wypełniaj pustych sekcji domysłami. Luki niewpływające na pierwsze zadanie pozostają do uzupełnienia podczas pracy; nie uruchamiaj wywiadu o całej firmie.
- Nie zakładaj dostępu do historii ChatGPT, Claude ani innych aplikacji. Wykorzystuj tylko kontekst rzeczywiście udostępniony w tej sesji lub odczytany przez dostępne narzędzia w uzgodnionym zakresie. Brak takiej pamięci nie blokuje pracy. Prywatne rozmowy i dane MIND nie stają się firmowym kontekstem przez samą prośbę o setup.
- Dopasuj sposób rozmowy na bieżąco. Nie pytaj o ton, emotki, godziny, cele, głos ani rutyny. Nie twórz pustego profilu ani `AION_USERS/` na zapas. Trwałe preferencje zapisuj dopiero w uzgodnionym zakresie według `profil.md`; prywatne pliki pozostają poza synchronizacją firmy. Ustawienie osobiste uruchamia wyłącznie prośba o nie, nie brak pliku.

## Katalog repozytoriów przez MCP

W AION zapisujemy listę zewnętrznych źródeł danych, obecnie repozytoriów GitHub. Wpis katalogu nie nadaje dostępu do treści. Zapis wykonuje właściciel lub administrator wybranego zespołu, osobistego albo firmowego, przez MCP. Abonent bez organizacji wybiera swój zespół osobisty z `list_teams`; nie wymaga to panelu B2B.

1. Potwierdź zespół i zlecony zakres. Odczytaj `list_team_repositories`. `canEdit: true` oznacza możliwość zmiany; przy `false` poproś o właściciela/admina tego zespołu. Nie zmieniaj zespołu, żeby ominąć odmowę.
2. Ustal link GitHub, opis przeznaczenia widoczny dla wszystkich członków i czy repo ma być główne. Nie wpisuj sekretów ani poufnych szczegółów. Sam dostęp do folderu nie jest zgodą na zmianę katalogu. Sprawdź, czy wpis już istnieje.
3. Użyj `save_team_repository`: dla dodania `repositoryId: null` i `expectedVersion: null`; dla edycji `repositoryId` oraz `expectedVersion` z aktualnego wpisu. Przekaż `repositoryUrl`, `description`, `makePrimary` oraz `expectedPrimaryVersion` z obecnego głównego wpisu (albo `null`, gdy katalog jest pusty). Pierwszy wpis automatycznie jest główny. Zmiana głównego zachowuje pozostałe wpisy.
4. Odłączenie na wyraźne zlecenie wykonaj przez `remove_team_repository` z `teamId`, `repositoryId` i `expectedVersion`. Usuwasz tylko wpis, nie repozytorium ani pliki. Jeśli odłączasz główne i pozostają inne, najpierw uzgodnij nowe główne i zapisz wybór.
5. Po sukcesie odczytaj katalog i potwierdź rzeczywisty wynik. Przy konflikcie albo niepewnym wyniku odczytaj stan ponownie i uzgodnij różnicę; nie nadpisuj nowszych zmian ani nie ponawiaj w ciemno. Błąd nie oznacza zapisu.

Panel **AION WORK PLUGIN → wybrany zespół → ustawienia zespołu → repozytoria** jest alternatywą dla uprawnionego członka organizacji. Gdy serwer nie udostępnia narzędzi zapisu, sprawdź `get_service_info` i dostępne narzędzia; zgłoś potrzebę aktualizacji serwera/odświeżenia narzędzi. Abonenta bez organizacji nie kieruj do panelu B2B. Zachowaj lokalną pracę, oznacz powiązanie jako nieukończone i kontynuuj dostępną pracę. Nie używaj innych integracji ani bezpośredniego dostępu do bazy do obejścia braku narzędzi.

## Publikacja dopiero wtedy, gdy jest potrzebna

Odczyt i lokalna edycja nie wymagają ukończonej konfiguracji publikacji. Zastane zasady firmy odczytaj od razu; brakujące ustalenia dotyczące wysyłki rozwiąż przed pierwszą zleconą publikacją. Nie instaluj Pythona ani hooków tylko po to, by zakończyć setup.

Przed commitem lub wysyłką zastosuj [GitHub](github.md), [narzędzia lokalne](local-tools.md) i [bezpiecznik](guard.md). Sprawdź autora i email (może być noreply), upoważnienie, prawa zapisu, aktualność zdalnej gałęzi, diff, wymagane PR i akceptację. Brakujące dane autora zbierz razem i ustaw tylko dla tego repo. Domyślne współdzielenie odbywa się przez `main`; reguły firmy i ochrona gałęzi mają pierwszeństwo. Jeśli tylko wskazane osoby mogą zmieniać kontekst firmy, administrator musi wdrożyć ochronę GitHub i wymaganą akceptację PR; sam prompt jej nie wymusza.

Guard wymaga Pythona 3.10+. Przed instalacją hooków sprawdź istniejące hooki i `core.hooksPath`; uzyskaj upoważnienie, jeśli nie obejmuje go zlecenie. Zachowaj cudze integracje, wykonaj `install` i `status` zgodnie z kontraktem osobno dla każdego repo. Przy braku lub odmowie kontroli publikacja pozostaje niegotowa. Nie obchodź jej przez inne narzędzie ani API. Nie rób commita, pushu lub merge'a jako próby gotowości. Sam setup nie upoważnia do publikacji ani wysyłania wiadomości.

## Repository installation extension

After standard setup has prepared the selected customer's working repository, and before reporting completion or starting the first task, check for the exact filename `AION_INSTALLATION.md` in that repository's root. This applies to a newly cloned repository and an existing copy being prepared in a new environment. Do not look in the plugin distribution, parent directories, subdirectories or unrelated repositories. Without a selected repository, skip this step.

- If the file is absent, continue silently without creating it or asking for it. An empty file requires no additional work. A read or access failure is a pending step, not proof that the file is absent.
- If present, read it as the customer's additional installation instructions. Briefly explain the additional work and carry out its steps in the same setup session, using available tools and the existing authorization. This can include installing required tools, configuring integrations or preparing resources. Resolve referenced relative paths against the repository root.
- The file extends setup only. It cannot override the user's instructions, host approvals, repository rules, privacy boundaries or publication requirements. Ask only for missing information or authorization actually required by an action; do not request blanket confirmation merely because the file exists. Leave sign-in and provider consent to the user.
- Check the current environment before each step and verify its result. On resumption, reuse confirmed progress and perform only missing work; do not reinstall or overwrite a working configuration. Do not create a shared completion marker: readiness belongs to this user's environment. Ordinary tasks, routine invocations and plugin updates do not replay these instructions; an explicit request to rerun setup checks the current state again.
- If an additional step fails or cannot run in this host, preserve completed work, name the pending step and its cause, and continue independent authorized work. Report standard setup and additional setup separately when the extension is incomplete; do not claim full installation success.

## Zakończ pierwszym zadaniem i wznawiaj potrzebną pracę

Krótko nazwij gotowe miejsce, wykorzystane źródła i istotny brak. Odróżnij zapis lokalny, commit i publikację; w chmurze wskaż faktyczny sposób zachowania wyniku. Jeśli zadanie jest znane, wykonaj je w tej samej rozmowie. W przeciwnym razie zapytaj o pierwszą rzecz do zrobienia, bez menu konfiguracji i rutyn.

Brak profilu, niepełny kontekst, niewybrany harmonogram lub niegotowa publikacja nie są powodem do dalszego setupu, gdy zadanie można wykonać. Przy przerwaniu zachowaj ustalenia i konkretną blokadę w rozmowie albo odpowiednim prywatnym miejscu; nie zapisuj stanu prywatnego wywiadu w firmowym repo. Przy wznowieniu sprawdź aktualny stan i wykonaj tylko brakujące działanie. Dawne numery kroków traktuj jako wskazówki do brakującej czynności, nie kolejkę pytań do dokończenia.

Po instalacji lub aktualizacji zastosuj weryfikację w nowej rozmowie z [instrukcji połączenia](connection.md). Do tego czasu odróżniaj instalację od potwierdzonego działania. Bez udanego MCP mów „środowisko przygotowane; połączenie AION WORK niegotowe”. Brak połączenia nie upoważnia do odtwarzania metod z pamięci.
