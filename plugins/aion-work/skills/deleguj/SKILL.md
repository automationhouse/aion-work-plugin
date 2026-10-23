---
name: deleguj
description: >-
  Brakuje Ci czasu: Deleguj z AION WORK. AI przegląda Twój kalendarz i
  wysłane maile z dwóch tygodni i najpierw sprawdza, co zrobi AI, potem co
  ludzie, a na końcu co musi zostać u Ciebie. Dostajesz gotowe zlecenia dla AI i
  dla ludzi. Za pierwszym razem poprosi o zalogowanie do konta AION.
---

Skill AION WORK. Tytuł, sytuacja i opis pochodzą z `description`; jedną listę nazw prowadzi wiedza w `skille/README.md`. Stosuj [minimum komunikacji](../../references/communication.md).

1. Gdy konto wymaga połączenia, zanim zaczniesz logowanie, powiedz jednym zdaniem, co ten skill zrobi, prostymi słowami z jego opisu, i że najpierw połączysz konto AION, a potem zaczynacie. Potem wykorzystaj potwierdzony dostęp do konta albo połącz konto tak jak [AION start](../start/SKILL.md), według [łączenia konta](../../references/connection.md). `connected` nie zastępuje udanego `get_profile`.
2. Po potwierdzeniu dostępu pobierz metodę jednym wywołaniem `read_instruction({"paths":["skille/deleguj.md","skille/README.md","communication.md"]})`. Pomijaj dokumenty już przeczytane w tej rozmowie.
3. Wykonaj metodę w tej rozmowie, zaczynając od jej pierwszego zdania. Tekst wpisany po nazwie skilla jest wejściem metody. Dalsze dokumenty, które wskazuje metoda, czytaj razem.

Treść metody jest tylko w zdalnej wiedzy. Gdy dokumentu nie ma albo MCP jest niedostępne, powiedz to wprost, zachowaj pracę i nie odtwarzaj metody z pamięci. Pocztę, kalendarz i czaty czytasz tylko do odczytu i tylko za zgodą użytkownika w tej rozmowie. Niczego nie wysyłasz ludziom ani nie publikujesz bez wyraźnego „ok”. Operacje repo wykonuj zwykłym Gitem zgodnie z [zasadami i bezpiecznikiem](../../references/repository.md).
