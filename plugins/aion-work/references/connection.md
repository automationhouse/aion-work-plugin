# Połączenie AION WORK

Czytaj przy łączeniu konta oraz zawsze, gdy użytkownik chce korzystać ze zdalnej wiedzy AION, również bez folderu i bez konfiguracji. Weryfikacja połączenia i odczyt wiedzy nie rozpoczynają wywiadu setupu. Przy zleceniu konfiguracji stosuj `references/setup.md`, bez wywiadu o personalizacji.

W każdym wywołaniu MCP przekazuj `requestOrigin` z `agent: "claude" | "gpt" | "unknown"` i `executionEnvironment: "cloud" | "local" | "unknown"`. GPT obejmuje ChatGPT i Codex; local oznacza komputer użytkownika (także WSL), a cloud zdalną sesję agenta, nawet jeśli interfejs jest otwarty na komputerze. Korzystaj z kontekstu hosta i potwierdzonych ustaleń rozmowy. Nie wnioskuj o środowisku z nazwy aplikacji, systemu operacyjnego, terminala lub folderu. Nieznany wymiar oznacz `unknown`; nie zadawaj dodatkowego pytania wyłącznie dla analityki. Kontekst dotyczy bieżącego wywołania i zmienia się wraz z sesją. Nie przekazuj w nim danych konta, ścieżek ani nazwy modelu.

1. Sprawdź faktycznie dostępne narzędzia serwera `aion-work`. `get_service_info` opisuje możliwości bez logowania; nie potwierdza konta. Przy braku narzędzi sprawdź raz natywny stan pluginu i jego MCP: sama obecność skilli nie potwierdza wykrycia serwera, a brak narzędzi nie dowodzi wylogowania. Przygotowanie lokalne może trwać dalej, ale wiedza zdalna nie jest gotowa.
2. Wywołaj `get_profile`, jeśli jest dostępny. Przy pierwszej instalacji bez potwierdzonego logowania, `needs_auth` albo HTTP 401 sam rozpocznij natywny OAuth według procedury poniżej. Użytkownik kończy logowanie i zatwierdza zgodę w przeglądarce. Udany odczyt profilu ma pierwszeństwo przed ogólnym statusem hosta; odmowa uprawnień do produktu nie jest powodem ponownego logowania. Przy anulowaniu podaj konkretny sposób wznowienia, zgodny z dostępną akcją hosta. Błąd adresu zwrotnego wymaga sprawdzenia rejestracji klienta przez administratora integracji; nie ponawiaj bez końca.
3. Sukces `get_profile` potwierdza tożsamość i dostęp: aktywne członkostwo firmowe albo uprawnienie abonamentowe, również legacy. OAuth nie wymaga firmy. Odczytaj `list_teams`, aby ustalić z użytkownikiem zespół bieżącej pracy, jeśli zadanie tego wymaga; lista obejmuje własne zespoły osobiste i firmowe oraz role. Gdy serwer odmawia dostępu, wyjaśnij potrzebę aktywnego członkostwa firmowego albo uprawnienia abonamentowego; gdy użytkownik ma opłacony dostęp albo jest w firmie, a odmowa trwa, zastosuj [pomoc AION](#pomoc-aion). Nie wybieraj ani nie twórz Workspace.
4. Po uwierzytelnieniu wywołaj `read_instruction` z `paths: ["welcome.md", "communication.md", "repository.md"]`, pomijając dokumenty już przeczytane w tej rozmowie. Zrób to przed udzieleniem odpowiedzi opartej na wiedzy AION WORK, także przy prośbie o samą wiedzę bez instalacji i repozytorium. Opisy narzędzi i ogólna wiedza modelu nie zastępują odczytu. Samo ogólne „Co potrafisz?” może otrzymać krótki, warunkowy opis możliwości bez sprawdzania konta; nie nazywaj wtedy dostępu zweryfikowanym. Pozostałe dokumenty znajduj przez `list_instructions` lub `search_instructions`. Po potwierdzeniu zespołu przekazuj jego `teamId` w tych wywołaniach; przed wyborem i przy pracy bez zespołu pomijaj ten parametr. Zmiana zespołu wymaga zmiany kontekstu, nie ponownego odczytywania już znanych dokumentów. Sukces odczytu potwierdza dostęp do wiedzy; sam status „połączono” nie wystarcza.
5. Kontynuuj zleconą pracę z rzeczywistym wynikiem sprawdzenia. Po wyborze dowolnego zespołu pobierz pełny katalog przez `list_team_repositories`, bez sprawdzania typu teamu. Konfigurację zmienia owner/admin przez MCP według sekcji katalogu w `setup.md`; abonent bez firmy używa swojego zespołu osobistego. Panel B2B jest alternatywą dla członków organizacji. To lista zewnętrznych źródeł danych; administrator organizacji ustawia dostęp do ich treści w GitHubie lub innej usłudze przechowującej dane. MCP nie klonuje repozytorium i nie przechowuje plików firmy.

Nie kopiuj tokenów, kodów autoryzacji ani parametrów adresu zwrotnego do rozmowy lub folderu. Logowanie AION i GitHub jest osobne. Logowanie OAuth nie potwierdza wyboru zespołu ani praw do repozytorium.

## Uruchomienie OAuth

Instalacja z polityką `ON_USE` nie gwarantuje otwarcia okna logowania. W ramach zleconej instalacji lub łączenia konta rozpocznij logowanie, zamiast kończyć na poleceniu szukania ustawień. Powiedz: „Otworzę logowanie do AIONa. Zaloguj się i zatwierdź połączenie w przeglądarce”. Samo pytanie „co potrafisz?” nie rozpoczyna tego procesu.

1. Użyj natywnej akcji OAuth udostępnionej przez hosta. Jeśli potrzebny jest terminal tego samego klienta i profilu, najpierw sprawdź `claude --version` albo `codex --version`. Brak polecenia obsłuż przez [przygotowanie CLI](local-tools.md#cli-aplikacji-przed-instalacją-i-reautoryzacją), a następnie wróć do logowania w tej samej rozmowie. Nie odsyłaj użytkownika do ręcznego logowania tylko dlatego, że CLI nie było zainstalowane. Sprawdź aktualne `mcp --help` i listę serwerów. Dla Codexa, gdy lista potwierdza serwer AION WORK i właściwy URL, użyj `codex mcp login <NAZWA> --scopes email,profile`. W Claude Code korzystaj z `claude mcp login <NAZWA>` tylko wtedy, gdy pomoc potwierdza tę komendę. Używaj rzeczywistej nazwy z listy, nie zgaduj prefiksów pluginu.
2. Jeśli klient nie wykrywa MCP zainstalowanego AION WORK, zastosuj [pomoc AION](#pomoc-aion) jako problem paczki lub aktywacji. Nie dopisuj drugiego serwera do ustawień, nie kopiuj poświadczeń WORK i nie implementuj własnego OAuth. Nowy czat nie naprawia brakującej konfiguracji serwera.
3. Utrzymuj jedną aktywną próbę logowania; nie używaj `--no-browser` w lokalnej instalacji. Gdy host zwróci adres autoryzacji, pokaż go jako link „Połącz konto AION” i otwórz w zwykłej przeglądarce użytkownika, jeśli nie otworzyła się automatycznie. Korzystaj wyłącznie z adresu bieżącej próby, bez zmieniania parametrów. Nie proś o wklejenie callbacka, kodu lub tokena. Hasło, MFA i zgodę pozostaw użytkownikowi. Podczas oczekiwania nie rozpoczynaj kolejnej próby ani wywiadu setupu.
4. Gdy CLI nie obsługuje logowania, skorzystaj z dostępnego interfejsu połączeń hosta. Dopiero po potwierdzeniu, że dostępne narzędzia nie pozwalają rozpocząć OAuth, podaj jeden konkretny krok ręczny na podstawie rzeczywistego ekranu lub komunikatu. Nie wymyślaj przycisków. Nie zamykaj aplikacji bez uzgodnienia.
5. Po ukończeniu OAuth sprawdź wynik klienta, następnie `get_profile` i trzy dokumenty rdzenia. Sam otwarty ekran zgody lub status `connected` nie potwierdzają dostępu. Jeśli dopiero załadowanie narzędzi wymaga nowej rozmowy, wyjaśnij tę granicę i użyj sprawdzenia poniżej; nie zastępuj logowania prośbą o restart.

## Sprawdzenie po instalacji i aktualizacji

Przy aktualizacji rozlicz też stan istniejących kopii guarda według [procedury aktualizacji](guard.md#aktualizacja-istniejącego-guarda). Wersja pluginu nie potwierdza aktualności hooków repo. Nie instaluj nowych hooków ani nie oznaczaj niesprawdzonej integracji jako gotowej.

Zainstalowana wersja, aktywacja pluginu, zalogowane konto i odczyt wiedzy to osobne wyniki. Po wymaganym restarcie sprawdź w nowej rozmowie narzędzia `aion-work`, `get_profile` i odczyt trzech dokumentów rdzenia według punktów powyżej. W folderze pracy sprawdź również odczyt `AGENTS.md` (w Claude Code przez istniejący import `@AGENTS.md`) i istniejących dopasowań potwierdzonego użytkownika. Brak profilu nie jest błędem weryfikacji ani powodem do ustawienia osobistego. Nie uruchamiaj setupu ponownie tylko dla tego sprawdzenia.

Gdy bieżąca sesja nie może otworzyć nowej rozmowy, powiedz „Instalacja potwierdzona; sprawdzenie w nowej rozmowie czeka” i podaj tekst do użycia po restarcie: „Sprawdź połączenie AION WORK, odczytaj rdzeń wiedzy i instrukcje tego folderu”. Nie zgłaszaj zakończonej weryfikacji, zanim otrzymasz jej wynik.

Jeśli narzędzia nie są dostępne, sprawdź osobno instalację i włączenie AION WORK w tym kliencie oraz zakresie, korzystając z jego aktualnej pomocy lub zarządzania pluginami. Zachowaj inne pluginy, uprawnienia i poświadczenia. Nie zastępuj całego pliku ustawień klienta. Nie próbuj naprawiać aktywacji przez kopiowanie starych metod AION WORK.

Narzędzia osobistego MIND i importu Company Context nie przyjmują `teamId`; nie przypisuj tych odczytów do firmy ani jej raportów.

## Pomoc AION

Zgłoszenie do pomocy AION WORK idzie formularzem pomocy AION, tym samym co w panelu app.aionwork.com. Zgłoszenie trafia do zespołu pomocy, który odpowiada w ciągu 24 godzin. Gdy formularz się nie otwiera, zapasem jest mail na support@automation.house. Sprawy AION MIND idą na hello@aionmind.com.

Zgłoszenie jest ostatnim krokiem. Gdy działa połączenie z AION, najpierw rozpoznaj i napraw problem według metody `pomoc.md` (skill [pomoc](../skills/pomoc/SKILL.md)). Ta sekcja wystarcza sama, gdy połączenia nie da się naprawić albo metody nie ma w bazie.

Rozpoznaj, kto może pomóc. Brak przydziału modułu, zaproszenia do firmy albo dostępu do repo na GitHubie rozwiązuje administrator firmy: podaj adres z odmowy serwera albo panel firmy. Do AION kieruj, gdy odmowa trwa mimo opłaconego dostępu lub członkostwa, gdy serwer zwraca `work.mcp.errors.unavailable` albo inny błąd po ponowieniu, gdy klient nie wykrywa MCP AION WORK i gdy brakuje narzędzi, które powinny być dostępne.

Przygotuj użytkownikowi link do formularza z wypełnionymi polami i tekst do pola „Szczegóły zgłoszenia”, którego link nie wypełnia. Link składasz z adresu `https://forms.clickup.com/24433538/f/q9mw2-664775/D7QTIEJQGWVJ8FRFKE` i parametrów zakodowanych jak w adresie URL:

- `Temat zgłoszenia`: jedno zdanie o problemie;
- `Aplikacja`: `AION WORK`;
- `Kategoria zgłoszenia`: `Technical Bugs / App Errors`, przy płatności `Billing & Subscriptions`, w innej sprawie `Other / General Inquiry`;
- `E-mail kontaktowy` i `email`: e-mail konta AION z `get_profile`; `user_id`: jego identyfikator, gdy jest znany;
- `source`: `work-plugin`; `app_version`: wersja wtyczki z manifestu; `os_version`: system i jego wersja.

Nie dodawaj innych parametrów: formularz odrzuca wartość spoza swojej listy. Tekst szczegółów zawiera firmę, aplikację (Claude Code albo Codex), krok, dokładny kod błędu, na przykład `work.mcp.errors.subscriptionRequired`, co już sprawdziłeś i co nie pomogło. Nie dołączaj treści firmy, plików, rozmów, haseł, tokenów ani kodów logowania. Pokaż link i tekst; formularz wysyła użytkownik. Otwórz link w przeglądarce, jeśli host to umożliwia i użytkownik się zgodzi.

Kody błędów serwera znaczą:

- `signInRequired`: konto AION nie jest połączone; uruchom OAuth.
- `subscriptionRequired`, `organizationRequired`: konto nie ma aktywnego abonamentu ani członkostwa w firmie.
- `teamUnavailable`: ten zespół jest niedostępny albo osoba nie ma uprawnień do zmiany jego konfiguracji.
- `instructionUnavailable`: tej procedury nie ma w aktualnej bazie; wyszukaj aktualną ścieżkę w katalogu.
- `unavailable`: serwer AION chwilowo nie odpowiada; ponów raz, potem pomoc AION.
