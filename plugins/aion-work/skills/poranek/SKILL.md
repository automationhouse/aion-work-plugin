---
name: poranek
description: >-
  Poranek z AION WORK: ważne zmiany, priorytet dnia i pierwszy gotowy szkic. Używaj na „poranek”, „zaplanuj mi dzień” albo „od czego dziś zacząć”.
---

Najpierw rozstrzygnij [wybór procedury](../../references/routines.md#wybór-procedury-w-istniejącym-repozytorium). Jawny wybór AION uruchamia ten skill; zwykłe polecenie tylko bez lokalnego przypisania w repo.

Stosuj [wywołanie rutyny](../../references/routines.md): potwierdź dostęp i pobierz rdzeń, a potem `rutyny/README.md`, `rutyny/poranek.md` oraz `rutyny/sygnaly.md` przez `read_instruction`.

Wykonaj metodę `rutyny/poranek.md` dla zakresu podanego przez użytkownika. Przygotowanie planu i pierwszego materiału nie uruchamia automatycznie dalszej pracy ani harmonogramu. Prośbę wyłącznie o ustawienie lub zmianę godziny obsłuż sekcją „Ustawienie kolejnego poranka” tej metody, bez wykonywania dzisiejszego poranka i pełnego ustawienia osobistego. W starcie propozycję kolejnego poranka prowadzi `starter.md`; samo wywołanie rutyny jej nie dodaje.

Po pokazaniu rzeczywistego wyniku (priorytet, plan dnia i pierwszy użyteczny szkic) zgłoś `report_basic_completion` z `basic: "morning"`. Przekaż `teamId` tylko potwierdzonej firmy; przy pracy bez wskazanej firmy pomiń go, także gdy osoba należy do kilku firm. Taki wynik liczy się do każdej jej firmy. Nie zgłaszaj samego pobrania instrukcji, konfiguracji ani harmonogramu. Zgłaszaj każde nowe wykonanie, także gdy instrukcja była już odczytana i gdy zmieniła się firma, ale nie ponawiaj zgłoszenia tego samego wyniku. Nie przekazuj treści wyniku. Po błędzie zachowaj wynik i nie obiecuj zaliczenia w panelu.
