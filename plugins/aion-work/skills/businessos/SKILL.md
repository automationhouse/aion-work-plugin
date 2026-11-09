---
name: businessos
description: >-
  AI Powered CEO z AION WORK: paczka dla właściciela i szefa firmy. Strategia i model biznesowy, ceny, konkurencja, przegląd tygodnia CEO, procesy i instrukcje dla zespołu, spotkania, rekrutacja, oceny i trudne rozmowy z ludźmi, finanse firmy: rachunek zysków i strat, przepływy pieniędzy. Używaj na „czy nasze ceny mają sens”, „zrób przegląd tygodnia firmy”, „opisz ten proces dla zespołu”, „przygotuj mnie do trudnej rozmowy z pracownikiem”, „kogo zatrudnić najpierw” albo „gdzie uciekają nam pieniądze”.
---

Najpierw rozstrzygnij [wybór procedury](../../references/routines.md#wybór-procedury-w-istniejącym-repozytorium). Jawny wybór AION uruchamia ten koszyk; zwykłe polecenie tylko bez lokalnego przypisania w repo.

# AI Powered CEO

1. Potwierdź konto i pobierz rdzeń według [łączenia konta](../../references/connection.md). Brak profilu lokalnego nie uruchamia setupu.
2. Pobierz drzewko skilli jednym wywołaniem `read_instruction` ze ścieżką `businessos/index.md`, pomijając dokument już przeczytany w tej rozmowie. Drzewko ma szefa paczki i czterech agentów: Business Strategist, Operations Manager, People Manager i Finance Manager. Przekaż `teamId` tylko dla zespołu wybranego w tej rozmowie i `requestOrigin` zgodnie z kontraktem połączenia.
3. Gdy prośbę robi więcej niż jeden agent paczki, np. cel z terminem, prowadzisz ją jako szef AI Powered CEO według [agentów paczek](../../references/agenci.md). Prośbę dla jednego agenta robi jego skill: wybierz go z drzewka według prośby, zanim zaczniesz pracę. Gdy pasują dwa, zapytaj jednym zdaniem o oczekiwany rezultat. Gdy prośba pasuje do skilla, nie rób zadania z ogólnej wiedzy.
4. Pobierz wybrany skill osobnym wywołaniem `read_instruction` ze ścieżką z drzewka.
5. Gdy drzewka nie ma w wiedzy albo żaden skill nie pasuje, szukaj przez `search_instructions` słowami prośby z `moduleKey: "businessos"`. Gdy moduł nie ma takiej metody, powiedz to wprost.
6. Przy odmowie przekaż użytkownikowi otrzymany powód i wskazaną przez serwer drogę uzyskania dostępu. Nie wymyślaj linku, nie odtwarzaj niedostępnej instrukcji i nie szukaj jej kopii w innym module.
7. Po udanym odczycie powiedz jednym zdaniem „Biorę skill AION WORK: <nazwa>”, potem wykonaj skill. Tekst wpisany po nazwie koszyka jest jego wejściem. Gdy zadanie się zmienia, weź kolejny skill z drzewka i przenieś ustalenia.

Kampanie, treści i reklamy prowadzi `marketingos`, oferty i rozmowy z klientem `salesos`. Przegląd tygodnia jest jeden, z `podstawy`, a ta paczka dokłada do niego część właściciela.

Treść skilli jest tylko w zdalnej wiedzy. Niczego nie wysyłasz ludziom, nie publikujesz i nie zmieniasz w systemach firmy bez wyraźnego „ok”.
