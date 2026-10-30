---
name: poranek
description: >-
  Poranek z AION WORK: ważne zmiany, priorytet dnia i pierwszy gotowy szkic. Używaj na „poranek”, „zaplanuj mi dzień” albo „od czego dziś zacząć”.
  Jawny wybór AION uruchamia ten skill; zwykłe polecenie tylko bez lokalnego
  przypisania w repo. Przy niejednoznaczności zapytaj, którą procedurę wykonać.
---

Najpierw rozstrzygnij [wybór procedury](../../references/routines.md#wybór-procedury-w-istniejącym-repozytorium). Dalsze kroki dotyczą wyłącznie wybranego skilla AION.

Stosuj [wywołanie rutyny](../../references/routines.md): potwierdź dostęp i pobierz rdzeń razem z `rutyny/README.md`, `rutyny/poranek.md` oraz `rutyny/sygnaly.md` przez `read_instruction`.

Wykonaj metodę `rutyny/poranek.md` dla zakresu podanego przez użytkownika. Przygotowanie planu i pierwszego materiału nie uruchamia automatycznie dalszej pracy ani harmonogramu. Prośbę wyłącznie o ustawienie lub zmianę godziny obsłuż sekcją „Ustawienie kolejnego poranka” tej metody, bez wykonywania dzisiejszego poranka i pełnego ustawienia osobistego. W ścieżce startu zaproszonego pracownika propozycję kolejnego poranka prowadzi `starter.md`; samo wywołanie rutyny jej nie dodaje.
