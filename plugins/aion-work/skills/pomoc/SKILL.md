---
name: pomoc
description: >-
  Coś nie działa: Pomoc z AION WORK. AI samo sprawdza, co blokuje pracę, i naprawia to z Tobą według odpowiedzi AION. Gdy się nie da, przygotowuje formularz zgłoszenia do pomocy AION z danymi, których potrzebujemy, a Ty go wysyłasz.
---

Najpierw rozstrzygnij [wybór procedury](../../references/routines.md#wybór-procedury-w-istniejącym-repozytorium). Jawny wybór AION uruchamia ten skill; zwykłe polecenie tylko bez lokalnego przypisania w repo.

# Pomoc AION WORK

Stosuj [minimum komunikacji](../../references/communication.md). Zgłoszenie do AION jest ostatnim krokiem.

1. Ustal objaw i krok, na którym wystąpił. Kod błędu i wynik narzędzia odczytaj sam, zamiast pytać użytkownika.
2. Gdy brakuje narzędzi AION WORK albo konto wymaga połączenia, napraw połączenie według [łączenia konta](../../references/connection.md). `connected` nie zastępuje udanego `get_profile`.
3. Po potwierdzeniu dostępu pobierz metodę jednym wywołaniem `read_instruction({"paths":["pomoc.md"]})` i wykonaj ją: rozpoznanie, naprawa według typowych przypadków, sprawdzenie wyniku.
4. Gdy połączenia nie da się naprawić albo metody nie ma w bazie, przejdź od razu do [pomocy AION](../../references/connection.md#pomoc-aion).

Nie wyłączaj zabezpieczeń, nie obchodź odmowy dostępu i nie wysyłaj zgłoszenia bez zgody użytkownika.
