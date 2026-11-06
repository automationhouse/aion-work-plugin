---
name: aion
description: >-
  AION: jedno wejście AION WORK. Na „/aion”, „AION”, „co dalej”, „od czego
  zacząć”, „nie wiem, co wpisać” i z każdym zadaniem po „/aion”, np. „/aion
  skrytykuj tę ofertę”. Rozpoznaje, gdzie jesteś: logowanie, pomoc, start
  albo jego wznowienie, folder dla zespołu, godzina poranka. Z zadaniem od
  razu dobiera metodę AION WORK.
---

Najpierw rozstrzygnij [wybór procedury](../../references/routines.md#wybór-procedury-w-istniejącym-repozytorium). Dalsze kroki dotyczą wyłącznie wybranego skilla AION.

Stosuj [minimum komunikacji](../../references/communication.md).

1. **Logowanie.** Wykorzystaj potwierdzony dostęp do konta albo zastosuj [łączenie konta](../../references/connection.md). Przy braku narzędzi AION WORK, `needs_auth`, HTTP 401 albo prośbie o ponowne logowanie („sign in again”) uruchom logowanie od razu, w tej rozmowie, według [uruchomienia OAuth](../../references/connection.md#uruchomienie-oauth). Gdy aplikacja nie pozwala go uruchomić z rozmowy, powiedz jednym zdaniem, jak się zalogować; w Claude Code: „Wpisz /mcp, wybierz aion-work i zaloguj się.” Nie wymyślaj przycisków innych aplikacji. Gdy odpowiadasz albo proponujesz odpowiedź bez metody, nie wspominasz o metodzie AION ani o jej braku. `connected` nie zastępuje udanego `get_profile`.
2. **Rdzeń i metoda.** Po potwierdzeniu dostępu pobierz rdzeń jednym wywołaniem `read_instruction({"paths":["welcome.md","communication.md"]})`, a osobnym wywołaniem `aion-wejscie.md`. Pomijaj dokumenty już przeczytane w tej rozmowie.
3. **Prowadzenie.** Wykonaj `aion-wejscie.md`: z zadaniem od razu dobierasz metodę według `welcome.md`, bez zadania rozpoznajesz stan i prowadzisz do pomocy, startu, AION chmura, ustawienia poranka albo propozycji metody. Dalsze dokumenty czytaj według wskazań metody, bez czytania całej bazy.

Gdy `aion-wejscie.md` nie ma jeszcze w bazie, pracuj według `welcome.md`: zadanie wykonaj od razu, a bez zadania zastosuj sekcje `starter.md#rozpoznaj-stan-przy-powitaniu` i `starter.md#powitanie-w-gotowym-repo`. Problem prowadź [pomocą](../pomoc/SKILL.md). Nie odtwarzaj metody z pamięci.

Do pracy firmy przekazuj potwierdzony `teamId`. Nie uruchamiaj poranka, przeglądu, ustawienia osobistego ani AION chmura bez prośby albo „tak” na konkretną propozycję. Harmonogram poranka ustawiaj tylko według odczytanej metody i dostępnym mechanizmem hosta.
