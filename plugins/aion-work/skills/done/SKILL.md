---
name: done
description: >-
  Done z AION WORK: zamknij sesję po bloku pracy. Zapisuje wyniki, decyzje i punkt wznowienia, wysyła zmiany sesji na GitHub, a po ustawieniu osobistym dopisuje robotę, która wraca, i przy powtórce proponuje własny skill. Używaj na „done”, „zamknij sesję” albo „kończymy”.
---

Najpierw rozstrzygnij [wybór procedury](../../references/routines.md#wybór-procedury-w-istniejącym-repozytorium). Jawny wybór AION uruchamia ten skill; przy zwykłym poleceniu lokalny plik o tej samej roli jest dopasowaniem, nie zamiennikiem.

Stosuj [wywołanie rutyny](../../references/routines.md): potwierdź dostęp i pobierz rdzeń, a potem `rutyny/README.md` oraz `rutyny/koniec-dnia.md` przez `read_instruction`. Gdy ustawienie osobiste jest ukończone, pobierz osobnym wywołaniem `rutyny/wzorce-plikow.md`; razem z poprzednimi przekracza limit jednej odpowiedzi.

Wykonaj wyłącznie sekcję „Zamknięcie sesji po bloku pracy” z `rutyny/koniec-dnia.md`. Dotyczy bieżącej rozmowy: nie uruchamiaj pełnego końca dnia, przeglądu innych rozmów ani wieczornej retrospektywy. Pliki zatwierdzone w tej sesji wyślij tylko według kroku wysyłki tej sekcji i `repository.md#synchronizacja-z-github`, pobranego osobno; gdy sekcja nie ma kroku wysyłki albo tej części `repository.md` nie da się pobrać, nic nie wysyłaj i powiedz, co zostało lokalnie. Zakończ wynikiem wskazanym w tej sekcji.
