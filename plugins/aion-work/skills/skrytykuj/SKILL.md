---
name: skrytykuj
description: >-
  Masz plan, ofertę albo tekst przed decyzją lub wysyłką: Skrytykuj z trzech
  stron z AION WORK. Trzech niezależnych recenzentów szuka najsłabszych miejsc,
  każdy z innego punktu widzenia, a Ty dostajesz jedną listę zmian od
  najważniejszej. Dopisz „szybko”, „na ślepo” albo „porażka”, gdy chcesz jednego
  recenzenta, oceny obcego klienta albo sprawdzenia, co zatopi Twój cel. Za
  pierwszym razem poprosi o zalogowanie do konta AION.
---

Skill AION WORK. Tytuł, sytuacja i opis pochodzą z `description`; jedną listę nazw prowadzi wiedza w `skille/README.md`. Stosuj [minimum komunikacji](../../references/communication.md).

1. Gdy konto wymaga połączenia, zanim zaczniesz logowanie, powiedz jednym zdaniem, co ten skill zrobi, prostymi słowami z jego opisu, i że najpierw połączysz konto AION, a potem zaczynacie. Potem wykorzystaj potwierdzony dostęp do konta albo połącz konto tak jak [AION start](../start/SKILL.md), według [łączenia konta](../../references/connection.md). `connected` nie zastępuje udanego `get_profile`.
2. Po potwierdzeniu dostępu pobierz rdzeń i metodę jednym wywołaniem `read_instruction({"paths":["welcome.md","communication.md","repository.md","skille/skrytykuj.md","skille/README.md"]})`. Pomijaj dokumenty już przeczytane w tej rozmowie.
3. Wykonaj metodę w tej rozmowie, zaczynając od jej pierwszego zdania. Tekst wpisany po nazwie skilla jest wejściem metody. Dalsze dokumenty, które wskazuje metoda, czytaj razem.

Treść metody jest tylko w zdalnej wiedzy. Gdy dokumentu nie ma albo MCP jest niedostępne, powiedz to wprost, zachowaj pracę i nie odtwarzaj metody z pamięci. Niczego nie wysyłasz ludziom ani nie publikujesz bez wyraźnego „ok”. Operacje repo wykonuj zwykłym Gitem zgodnie z [zasadami i bezpiecznikiem](../../references/repository.md).
