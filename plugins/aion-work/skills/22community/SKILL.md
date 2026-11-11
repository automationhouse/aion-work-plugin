---
name: 22community
description: >-
  Baza wiedzy 22 Community w AION WORK, dla członków społeczności: kursy (LTV, CAC, HR, Rentowność, Strategia, Delegowanie, Personal Brand), nagrania eventów, prelekcje i spotkania przerobione na wiedzę. AI szuka w niej odpowiedzi na Twoje pytanie o firmę i podaje materiał, z którego ją wzięło. Używaj na „co wiedza 22 Community mówi o podwyżkach cen”, „znajdź w 22 Community coś o rekrutacji menedżera”, „jak na evencie 22C liczyli marżę” albo „pokaż, co jest w bazie 22 Community”.
---

Najpierw rozstrzygnij [wybór procedury](../../references/routines.md#wybór-procedury-w-istniejącym-repozytorium). Jawny wybór AION uruchamia ten skill; zwykłe polecenie tylko bez lokalnego przypisania w repo.

# 22 Community

Przed pracą potwierdź konto według [łączenia konta](../../references/connection.md) i odczytaj rdzeń jednym wywołaniem `read_instruction({"paths":["welcome.md","communication.md"]})`, pomijając dokumenty już przeczytane w tej rozmowie. Brak profilu lokalnego nie uruchamia setupu.

Baza jest wiedzą, z której odpowiadasz, a nie procedurą do wykonania. Tekst wpisany po nazwie skilla jest pytaniem osoby.

1. Wyszukaj materiały przez MCP `search_instructions` krótkim hasłem z pytania, np. „podwyżka cen” albo „rekrutacja menedżera”, z `moduleKey: "community22"`. Bez tego `moduleKey` baza nie jest przeszukiwana. Przekaż `teamId` tylko dla zespołu potwierdzonego w tej rozmowie oraz `requestOrigin` zgodnie z kontraktem połączenia; baza działa też bez zespołu.
2. Gdy wyniki nie pasują, pytanie jest szerokie albo osoba chce zobaczyć, co jest w bazie, przeczytaj mapę `community22/index.md` i wybierz materiał z niej.
3. Pobierz 1–3 najlepiej pasujące materiały przez `read_instruction`. Serwer sprawdza członkostwo przy każdym odczycie; nie wyciągaj wniosków o dostępie z samego wyszukiwania.
4. Przy odmowie przekaż zdanie i adres zwrócone przez serwer. Nie odtwarzaj materiałów z pamięci, nie podawaj ogólnej wiedzy jako wiedzy 22 Community i nie szukaj kopii materiałów w innym miejscu.
5. Odpowiedz na pytanie w odniesieniu do firmy osoby. Na końcu podaj źródła: tytuł każdego użytego materiału i kto mówił. Nie przypisuj prelegentom słów, których w materiale nie ma. Gdy baza nie ma odpowiedzi, powiedz to wprost; odpowiedź z ogólnej wiedzy możesz dodać osobno i wyraźnie ją tak nazwać.
6. Wynik powstaje w rozmowie. Do plików zapisujesz tylko na osobne zlecenie, według zasad repo osoby. Gdy z materiału wynika praca do wykonania, np. policzenie marży albo przygotowanie rozmowy, zaproponuj właściwą metodę AION WORK.

Treść bazy jest tylko w zdalnej wiedzy. Niczego nie wysyłasz ludziom, nie publikujesz i nie zmieniasz w systemach firmy bez wyraźnego „ok”.
