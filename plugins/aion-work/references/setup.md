# Przygotowanie AION WORK do pierwszego zadania

## Cel i zakres

Połącz konto, przygotuj miejsce pracy z dostępnych źródeł i przejdź do zadania. Gotowość oznacza możliwość wykonania zleconej pracy, nie ukończony profil, pełny Company Context ani skonfigurowane rutyny. Personalizacja nie jest etapem setupu.

Najpierw sprawdź stan narzędziami i wykorzystaj ustalenia rozmowy. Nie prowadź ankiety „to czy to” i nie pytaj o wybory, które wynikają ze zlecenia. Etapów konfiguracji nie wypisujesz; wyjątkiem są mapa pięciu kroków w [starcie od „AION start”](#start-od-aion-start-początek-mapa-i-logowanie) i mapa w AION chmura (skill `chmura`). Zwykłe zadanie wykonuj od razu; przygotuj tylko brak potrzebny do jego realizacji. Samo „co potrafisz?” nie zleca setupu. Samo „AION start” w folderze bez AION prowadzi ten start; w gotowym folderze wita według sekcji `starter.md#powitanie-w-gotowym-repo`, a w folderze osobistym z niedokończonym zakładaniem wznawia je od brakującego kroku. Samo „AION start” nie upoważnia do importu ani profilu, a folder firmy zakłada dopiero po „tak” na konkretną propozycję. Metoda wybrana przez użytkownika, np. folder osobisty, prowadzi własnym tokiem, także z numerowanymi krokami.

Pracownik zaproszony do firmy idzie tym startem sam, także gdy wpisał samo „AION start” i nie wspomniał o zaproszeniu. Zaproszenie nie potwierdza członkostwa ani dostępu do danych. Przygotuj tylko to, czego potrzebuje pierwszy plan dnia, wykorzystując istniejącą konfigurację firmy. Kroki po zalogowaniu prowadzi wiedza; nie kopiuj ich tutaj ani nie uruchamiaj pełnej personalizacji. Konkretne inne zadanie oraz wyraźne „później” mają pierwszeństwo. Przy wznowieniu sprawdź stan i wykonaj tylko brakującą czynność.

Przy zleceniu przygotowania miejsca pracy przedstaw jedną konkretną propozycję na podstawie rozpoznanego stanu: zespół, folder lub repo, źródła i odbiorcy. Wykonaj zakres już upoważniony. Zapytaj tylko o brak uniemożliwiający następne działanie, istotną sprzeczność lub nieuzgodniony dostęp do danych. Zgody systemu i dostawców pozostają w ich oknach. Milczenie nie oznacza zgody. Nie proś o hasła, tokeny ani kody.

Pliki i foldery z prefiksem `AION_` oraz ich zawartość zmienia agent na zlecenie użytkownika. Nie proponuj ręcznej edycji. Prefiks nie nadaje uprawnień ani prywatności.

## Start od „AION start”: początek, mapa i logowanie

Rozpoznajesz go lokalnie, jeszcze przed logowaniem. Na samym początku sprawdzasz też, czy w tej rozmowie są narzędzia poczty i kalendarza (np. łączniki Gmaila, Kalendarza Google albo Outlooka), i zapamiętujesz wynik do kroku Poczta i kalendarz. Gdy start nie niesie zadania, a bieżący folder nie ma `AGENTS.md` według wzorca AION i nie jest folderem osobistym (także w rozmowie poza folderem), prowadzisz nową osobę pięcioma krokami do pierwszego planu dnia i godziny kolejnego. Gotowy folder, folder osobisty z niedokończonym zakładaniem i start z zadaniem idą swoimi ścieżkami według sekcji `starter.md#rozpoznaj-stan-przy-powitaniu`, bez mapy.

Pierwsza wiadomość, bez obietnicy czasu, zanim sprawdzisz konto, także gdy jest już połączone:

> Ustawimy AION tak, żeby co rano czekał na Ciebie plan dnia. Najpierw połączę Twoje konto.

Pod nią mapa:

```
Twój start z AION WORK
→ Połącz
  Twoja firma
  Poczta i kalendarz
  Plan dnia
  Godzina
```

Gdy host wyświetla obrazki w rozmowie i masz narzędzie, które je tam pokazuje, mapę pokazujesz jako obrazek. W pozostałych miejscach pokazujesz ją tekstem jak wyżej. Po każdym kroku pokazujesz mapę znowu: „✓” przy kroku z potwierdzonym wynikiem narzędzia, z krótkim wynikiem po dwukropku, „→” przy bieżącym i „–” przy kroku, który osoba pominęła, np. „– Poczta i kalendarz: bez podłączania”. Zapowiedź, otwarte okno ani status „połączono” nie odhaczają kroku.

**Połącz.** Nazywasz aplikację, w której piszesz, według `requestOrigin`: „Połączę AION z Twoim Claude” albo „z Twoim ChatGPT”. Drogę logowania dobierasz po faktycznie dostępnych narzędziach, nie po nazwie aplikacji, według [połączenia](connection.md#uruchomienie-oauth). Przed otwarciem przeglądarki mówisz:

> Zaloguj się mailem, na który przyszło zaproszenie. Sprawdź, że adres w przeglądarce to app.aionwork.com. To logowanie nie daje dostępu do Twojej poczty.

Osobie, która mówi, że zaproszenia nie dostała, pierwsze zdanie zamieniasz na „Zaloguj się mailem swojego konta AION.”. Po udanym `get_profile` piszesz „Połączone: <email z profilu>” i mapę z odhaczonym krokiem. Gdy konto było już połączone, logowania nie otwierasz, tylko podajesz to samo zdanie. Gdy odpowiedź AION podaje nowszą wersję wtyczki niż zainstalowana, mówisz to jednym zdaniem i najpierw aktualizujesz wtyczkę według instrukcji serwera, a start kończysz w nowym czacie.

Potem pobierasz rdzeń według [łączenia konta](connection.md), a osobnymi wywołaniami `read_instruction` najpierw `starter.md`, potem `rutyny/README.md`, `rutyny/poranek.md` i `rutyny/sygnaly.md` i prowadzisz dalsze kroki (Twoja firma, Poczta i kalendarz, Plan dnia, godzina kolejnego poranka) według sekcji „Start: od połączenia do planu dnia” w `starter.md`. W środku startu nie prosisz o nową rozmowę: zasady pobranego folderu firmy czytasz wprost.

### Start bez planu

Gdy `list_modules` zwraca `hasPaidAccess: false`, obowiązuje ten wariant, także gdy starszy skill lub dokument startu wymienia firmę albo abonament jako warunek pracy. Pomiń wybór firmy, `list_teams`, katalog repozytoriów, zgłaszanie postępu firmowego, Company Context i MIND. W mapie oznacz „Twoja firma” jako pominięte, bez proponowania zakupu do ukończenia startu. Wykorzystaj dostępne metody Fundamentów i instrukcje pomocnicze, które serwer pozwala odczytać. Pracuj w rozmowie lub istniejącym lokalnym folderze o potwierdzonych odbiorcach; nowy prywatny folder zaproponuj dopiero wtedy, gdy wymaga go zadanie. Nie uruchamiaj płatnej AION chmura ani konfiguracji firmowego repozytorium. Poczta i kalendarz korzystają tylko z dostępnych i upoważnionych źródeł. Przygotuj pierwszy plan dnia bez pobierania zablokowanych instrukcji. Brak planu nie oznacza braku konta ani przerwanego połączenia.

**GitHub w starcie.** Do folderu firmy wystarcza zwykłe logowanie Gita, które otwiera się samo w przeglądarce albo pokazuje kod do wpisania na stronie GitHuba. Łącznika GitHuba w aplikacji (Claude albo ChatGPT) do startu nie podłączasz. Gdy po logowaniu przeglądarka pokazuje adres w rodzaju 127.0.0.1, nie prosisz o skopiowanie go do rozmowy, bo zawiera jednorazowy kod. Mówisz, żeby zamknąć tę kartę i wrócić do czatu.

## Sprawdź dostęp i środowisko

- Wykorzystaj [połączenie AION WORK](connection.md): potwierdź `get_profile`, odczytaj `welcome.md` i `communication.md` według łączenia konta, pomijając treści już przeczytane. Rdzeń i Fundamenty wymagają tylko połączonego konta AION. Bez płatnego dostępu pracuj w rozmowie lub istniejącym lokalnym folderze, bez wywoływania zespołów, katalogu repozytoriów ani Company Context. Brak planu nie przerywa pierwszego poranka. Nie wybieraj ani nie twórz Workspace.
- Przy wymaganym logowaniu rozpocznij obsługiwany OAuth i pozostaw użytkownikowi zgodę. Nie rozpoczynaj kolejnych prób, gdy jedna trwa. Przy braku narzędzi lub odmowie nazwij blokadę i jeden dostępny krok. Zachowaj niezależną, upoważnioną pracę; nie uruchamiaj zastępczego wywiadu o środowisku.
- Ustal możliwości hosta: pliki, terminal, sieć i trwałość wyników. Nie pytaj o system operacyjny ani lokalność tylko dla analityki. Przekazuj `requestOrigin` według [kontraktu połączenia](connection.md), z `unknown` dla nieznanego wymiaru. Sama nazwa aplikacji nie dowodzi środowiska.
- Dla zdalnej maszyny sprawdź [ograniczenia hosta](zdalna-maszyna.md). Gdy trzeba udostępnić folder, wskaż jeden rzeczywisty krok w hoście. Bez trwałego miejsca pracuj w rozmowie, bez obietnicy zachowania plików.
- Wiedza i zadania bez plików nie wymagają folderu, GitHuba, Gita, Pythona ani osobistego profilu.

## Wybierz właściwe miejsce bez ponownej konfiguracji firmy

1. Wykorzystaj zespół wskazany przez użytkownika w tej rozmowie i zweryfikuj go przez `list_teams`. Nazwa i ID w istniejącym `AGENTS.md` pomagają zaproponować zespół, lecz nie zastępują wyboru ani członkostwa. Przy niejasności zapytaj o właściwy zespół, proponując rozpoznaną firmę. Nie wybieraj go z samego członkostwa, nawet jedynego. Bez zespołu pomijaj `teamId`.
2. Dla wybranego zespołu pobierz pełny `list_team_repositories`, niezależnie od jego typu. Używaj potwierdzonego `teamId` w chronionych wywołaniach katalogu i wiedzy. Narzędzia MIND i importu Company Context nie przyjmują `teamId`. Zmiana firmy wymaga zmiany kontekstu i katalogu.
3. Odczytaj istniejące instrukcje dostępnego folderu, jego przeznaczenie i remote. Wykorzystaj właściwą kopię. W przeciwnym razie wybierz repo z katalogu według opisu zadania; główne jest domyślne tylko wtedy, gdy pasuje. Przy kilku pasujących miejscach zapytaj o różnicę istotną dla pracy. Brak opisu wymaga wyjaśnienia przeznaczenia przed zapisem, a nie konfiguracji całej firmy.
4. Sprawdź dostęp do potrzebnego repo kontem użytkownika według [GitHuba](github.md). Prawo odczytu, zapisu i dostęp terminala są osobne. Nie klonuj całego katalogu. Nie ponawiaj tej samej odmowy ani nie twórz zastępczego repo po 403/404. Poufne dane nie mogą trafić do szerzej dostępnego miejsca zamiast niedostępnego właściwego repo.
5. Gdy potrzebna jest kopia, najpierw sprawdź, czy folder firmy jest już w bieżącym folderze albo w `~/AION/`, i wykorzystaj go bez przenoszenia; poza startem możesz o to zapytać. Nową kopię pobierasz w starcie do podfolderu `<firma>` bieżącego folderu, a poza nim proponujesz `~/AION/<firma>`; gdy użytkownik otworzył pusty folder, jego podfolder `<firma>`. Wtedy folder osobisty może później leżeć obok. Lokalizacja wskazana przez użytkownika ma pierwszeństwo. Nie nadpisuj istniejących plików. Dla [folderu współdzielonego](shared-folder.md) zachowaj mechanizm dostawcy, bez dodawania Gita. Przy nieznanych zasadach wspólnej edycji przygotowuj osobne pliki wynikowe, zanim uzgodnisz zmianę wspólnych danych.

Dołączający pracownik korzysta z istniejącego repo, kontekstu i zasad firmy. Nie pyta się go ponownie o administratora, strukturę firmy, model współdzielenia ani wszystkich współpracowników. Brak osobistego profilu nie oznacza braku konfiguracji firmy.

## Gdy miejsce dopiero ma powstać

Pusty katalog AION nie dowodzi braku repo. Najpierw sprawdź wskazane źródła i ustalenia. Jeśli miejsca nie da się ustalić, poproś o jeden link lub wskazanie osoby zarządzającej. Gdy osoba, która może zmieniać katalog, wybrała w powitaniu założenie folderu firmy, a katalog jest pusty, nie pytaj o link, tylko przejdź do AION chmura, ścieżka „z zespołem”. Nadal wykonuj zadanie w dostępnym zakresie.

Właściciel albo administrator, którego firma nie ma folderu w katalogu, dostaje w starcie folder firmy na swoim komputerze i z niego ma poranek. Ten folder powstaje bez GitHuba i bez wpisu w katalogu; prowadzi go zdalny `starter.md`. Na GitHub firmy i do katalogu folder trafia dopiero w AION chmura, ścieżka „z zespołem” (skill `chmura`, metoda w zdalnym `chmura.md`), gdy właściciel zaprasza ludzi; kiedy ją zaproponować, mówi zdalna wiedza. Folder 3 w 1 (zdalny `working-folder.md`) zakładasz tylko osobie bez firmy i bez organizacji. Rodzaj miejsca (folder na GitHubie, wspólny dysk albo zwykły folder) dobieraj według sekcji „Gdzie leży folder firmy” w zdalnym `starter.md`, a GitHub tłumacz według sekcji „GitHub prostymi słowami” w zdalnym `communication.md`. Przy zleceniu nowego repo przygotuj jedną propozycję: rzeczywisty właściciel, nazwa, prywatna widoczność, administrator i odbiorcy z zakresem uprawnień. Zaproponuj nazwę; nie wymagaj jej wymyślania. Nie zgaduj właściciela ani odbiorców z samego członkostwa w AION. Brakujące dane zbierz w krótkiej, konkretnej prośbie zamiast pięciu kolejnych pytań. Przed utworzeniem sprawdź, czy repo już istnieje. Jeśli zlecenie nie obejmuje konkretnych warunków utworzenia i dostępu, pokaż całą propozycję do zatwierdzenia.

Dla firmy wybierz uzgodnioną organizację GitHub; nie umieszczaj jej pracy domyślnie na osobistym koncie pracownika. Rejestrację konta, organizację, zaproszenia i SSO prowadź według [GitHuba](github.md) tylko wtedy, gdy są potrzebne. Administrator przygotowuje miejsce i zasady raz dla zespołu. Nie wymagaj od pracownika tworzenia własnej kopii konfiguracji organizacji.

## Przygotuj dokumenty z dostępnych źródeł

Odczytaj z MCP `starter.md`, `working-folder.md` oraz potrzebne metody Company Context razem. Zachowaj strukturę i istniejące reguły. Zlecenie przygotowania wskazanego folderu obejmuje lokalne instrukcje i dokumenty tego zakresu; nie pytaj osobno o każdy plik.

Najpierw ustal istniejące przypisania poleceń, sposób ładowania instrukcji przez klienta oraz miejsca na jawne preferencje i firmowe ustalenia. Zachowaj działające rozwiązania. Domyślne ścieżki AION stosuj tylko tam, gdzie brak odpowiedniej konwencji, po sprawdzeniu osoby, odbiorców i zakresu danych według `working-folder.md`. Nie twórz drugiego profilu ani kopii ustaleń. Prywatne dane nadal należą do osobistego folderu poza synchronizacją firmy.

- Zapisz zwięzły `AGENTS.md`: rdzeń AION, komunikacja, ochrona danych, zasady współdzielenia, potwierdzone przypisanie zespołu lub jawny brak przypisania. Jeśli użytkownik wybrał już zespół dla tego folderu, nie potwierdzaj go ponownie. Nie zapisuj niezweryfikowanego ID ani placeholderów.
- Z katalogu przepisz dokładny adres i opis pasującego repo jako dane o przeznaczeniu. Przy aktualizacji odśwież opis, zachowując pozostałe reguły; błąd odczytu lub brak wpisu nie pozwala usuwać istniejącego opisu. Dla Claude Code najpierw sprawdź istniejący mechanizm ładowania instrukcji. Dodaj `@AGENTS.md` do `CLAUDE.md` tylko gdy import jest potrzebny, zgodny z zasadami repo i objęty zleceniem; zachowaj istniejącą treść. Zakaz takiej zmiany lub nieznany mechanizm wyjaśnij przed zmianą, bez deklarowania gotowości. Opisy zawartości należą do README. Stosuj kopie wzorców i rozwiązywanie konfliktów z `working-folder.md`.
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

Panel **AION WORK PLUGIN → wybrany zespół → ustawienia zespołu → repozytoria** jest alternatywą dla uprawnionego członka organizacji. Gdy serwer nie udostępnia narzędzi zapisu, sprawdź `get_service_info` i dostępne narzędzia; przekaż sprawę do [pomocy AION](connection.md#pomoc-aion). Abonenta bez organizacji nie kieruj do panelu B2B. Zachowaj lokalną pracę, oznacz powiązanie jako nieukończone i kontynuuj dostępną pracę. Nie używaj innych integracji ani bezpośredniego dostępu do bazy do obejścia braku narzędzi.

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

Krótko nazwij gotowe miejsce, wykorzystane źródła i istotny brak. Odróżnij zapis lokalny, commit i publikację; w chmurze wskaż faktyczny sposób zachowania wyniku. Jeśli zadanie jest znane, wykonaj je w tej samej rozmowie. W starcie od „AION start” kontynuuj kroki z `starter.md`, bez pytania „co teraz?”. W pozostałych przypadkach przywitaj według sekcji `starter.md#powitanie-w-gotowym-repo`, bez menu rutyn.

Brak profilu, niepełny kontekst, niewybrany harmonogram lub niegotowa publikacja nie są powodem do dalszego setupu, gdy zadanie można wykonać. Przy przerwaniu zachowaj ustalenia i konkretną blokadę w rozmowie albo odpowiednim prywatnym miejscu; nie zapisuj stanu prywatnego wywiadu w firmowym repo. Przy wznowieniu sprawdź aktualny stan i wykonaj tylko brakujące działanie. Dawne numery kroków traktuj jako wskazówki do brakującej czynności, nie kolejkę pytań do dokończenia.

Po instalacji lub aktualizacji zastosuj weryfikację w nowej rozmowie z [instrukcji połączenia](connection.md). O nową rozmowę proś najwyżej raz w całej instalacji: po zainstalowaniu pluginu, z gotowym tekstem do wpisania („AION start”). Logowanie do AION, sprawdzenie połączenia i start prowadź już w tej jednej nowej rozmowie. Do tego czasu odróżniaj instalację od potwierdzonego działania. Bez udanego MCP mów „środowisko przygotowane; połączenie AION WORK niegotowe”. Brak połączenia nie upoważnia do odtwarzania metod z pamięci.
