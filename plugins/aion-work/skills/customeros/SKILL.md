---
name: customeros
description: Start współpracy, prowadzenie relacji, rozwój i utrzymanie klientów. Używaj, gdy użytkownik chce wdrożyć nowego klienta, przygotować status lub raport, rozwinąć relację albo ograniczyć ryzyko odejścia.
---

# CustomerOS

Przed pracą potwierdź konto według [łączenia konta](../../references/connection.md) i odczytaj rdzeń jednym wywołaniem `read_instruction({"paths":["welcome.md","communication.md","repository.md"]})`, pomijając dokumenty już przeczytane w tej rozmowie. Brak profilu lokalnego nie uruchamia setupu.

1. Wyszukaj właściwą procedurę przez MCP `search_instructions`, przekazując krótką frazę opisującą zadanie i `moduleKey: "customeros"`. Przekaż `teamId` tylko dla potwierdzonego zespołu oraz `requestOrigin` zgodnie z kontraktem połączenia.
2. Pobierz wybrany dokument przez `read_instruction`. Serwer sprawdza dostęp; nie wyciągaj wniosków o uprawnieniach z samego wyniku wyszukiwania.
3. Przy odmowie przekaż powód i sposób uzyskania dostępu zwrócony przez serwer. Nie wymyślaj adresu zakupu ani treści zablokowanej procedury.
4. Po udanym odczycie wykonaj procedurę i pobieraj tylko potrzebne materiały. Kontekst firmy odczytuj wyłącznie z niezależnie uprawnionych źródeł.
5. Pracuj jako AION w tej samej rozmowie; kolejne zadanie oznacza dobór kolejnej procedury.
