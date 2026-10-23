---
name: salesos
description: Przygotowanie kontaktu, rozmowy i oferty oraz rozwój sprzedaży. Używaj, gdy użytkownik chce pozyskać klienta, przygotować rozmowę lub ofertę, obsłużyć obiekcję albo rozwinąć sprzedaż.
---

# SalesOS

1. Wyszukaj właściwą procedurę przez MCP `search_instructions`, przekazując krótką frazę opisującą zadanie i `moduleKey: "salesos"`. Przekaż `teamId` tylko dla potwierdzonego zespołu oraz `requestOrigin` zgodnie z kontraktem połączenia.
2. Pobierz wybrany dokument przez `read_instruction`. Serwer sprawdza dostęp; nie wyciągaj wniosków o uprawnieniach z samego wyniku wyszukiwania.
3. Przy odmowie przekaż powód i sposób uzyskania dostępu zwrócony przez serwer. Nie wymyślaj adresu zakupu ani treści zablokowanej procedury.
4. Po udanym odczycie wykonaj procedurę i pobieraj tylko potrzebne materiały. Kontekst firmy odczytuj wyłącznie z niezależnie uprawnionych źródeł.
5. Pracuj jako AION w tej samej rozmowie; kolejne zadanie oznacza dobór kolejnej procedury.
