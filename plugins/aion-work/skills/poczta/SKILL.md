---
name: poczta
description: >-
  Poczta i kalendarz w porannym planie z AION WORK, gdy aplikacja nie ma łącznika: Apple Mail i Kalendarz na Macu albo klasyczny Outlook na Windows, tylko do odczytu. Używaj na „poczta”, „podłącz pocztę”, „mam pocztę w Apple Mail” albo „w Outlooku”.
  Jawny wybór AION uruchamia ten skill; zwykłe polecenie tylko bez lokalnego
  przypisania w repo. Przy niejednoznaczności zapytaj, którą procedurę wykonać.
---

Najpierw rozstrzygnij [wybór procedury](../../references/routines.md#wybór-procedury-w-istniejącym-repozytorium). Dalsze kroki dotyczą wyłącznie wybranego skilla AION.

Stosuj [wywołanie rutyny](../../references/routines.md): potwierdź dostęp i pobierz rdzeń razem z `rutyny/poczta.md` i `rutyny/sygnaly.md` przez `read_instruction`.

Wykonaj metodę `rutyny/poczta.md`. Skrypty leżą w tej wtyczce: `../../scripts/poczta/poczta-mac.js` (Mac) i `../../scripts/poczta/poczta-outlook.ps1` (Windows). Ustal ich pełną ścieżkę z położenia tego pliku. Skrypty tylko czytają. Nie wysyłasz, nie przenosisz i nie usuwasz wiadomości, nie zmieniasz ustawień zabezpieczeń poczty ani systemu, a hasła do poczty nigdy nie trafiają do rozmowy.
