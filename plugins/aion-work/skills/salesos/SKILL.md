---
name: salesos
description: >-
  Chcesz pozyskać klienta albo sprzedawać więcej: przygotować kontakt, rozmowę lub ofertę, obsłużyć obiekcję albo rozwinąć sprzedaż. Skill AION WORK SalesOS: AI dobiera do zadania procedurę sprzedażową i prowadzi je według niej. Używaj na „przygotuj mnie do rozmowy z klientem”, „klient mówi, że za drogo”, „napisz ofertę” albo „napisz do leadów, które milczą”.
---

Najpierw rozstrzygnij [wybór procedury](../../references/routines.md#wybór-procedury-w-istniejącym-repozytorium). Jawny wybór AION uruchamia ten skill; zwykłe polecenie tylko bez lokalnego przypisania w repo.

# SalesOS

Przed pracą potwierdź konto według [łączenia konta](../../references/connection.md) i odczytaj rdzeń jednym wywołaniem `read_instruction({"paths":["welcome.md","communication.md"]})`, pomijając dokumenty już przeczytane w tej rozmowie. Brak profilu lokalnego nie uruchamia setupu.

1. Wyszukaj właściwą procedurę przez MCP `search_instructions`, przekazując krótką frazę opisującą zadanie i `moduleKey: "salesos"`. Przekaż `teamId` tylko dla potwierdzonego zespołu oraz `requestOrigin` zgodnie z kontraktem połączenia.
2. Pobierz wybrany dokument przez `read_instruction`. Serwer sprawdza dostęp; nie wyciągaj wniosków o uprawnieniach z samego wyniku wyszukiwania.
3. Przy odmowie przekaż powód i sposób uzyskania dostępu zwrócony przez serwer. Nie wymyślaj adresu zakupu ani treści zablokowanej procedury.
4. Po udanym odczycie powiedz jednym zdaniem „Biorę skill AION WORK: <tytuł procedury>”, potem wykonaj procedurę i pobieraj tylko potrzebne materiały. Kontekst firmy odczytuj wyłącznie z niezależnie uprawnionych źródeł.
5. Pracuj jako AION w tej samej rozmowie; kolejne zadanie oznacza dobór kolejnej procedury.
