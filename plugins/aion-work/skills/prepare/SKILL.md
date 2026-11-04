---
name: prepare
description: >-
  Przygotuj firmę z AION WORK, raz, przed startem zespołu: dla właściciela albo
  administratora, na „AION prepare”, „/aion-prepare”, „przygotuj firmę” albo
  jawny wybór tego skilla. Prowadzi sześcioma krokami (Połącz, Organizacja,
  Folder firmy, Wiedza firmy, Zespół, Poczta firmy) i kończy pierwszym planem
  dnia. Pracownik zaproszony do firmy robi tylko „AION start”.
---

Twoja pierwsza wiadomość w rozmowie, napisana do osoby jako tekst, zanim przeczytasz jakikolwiek plik albo wywołasz narzędzie, także gdy konto jest już połączone:

> Przygotujemy firmę tak, żeby każda osoba z zespołu po „AION start” od razu dostała folder firmy i plan dnia. Najpierw połączę Twoje konto.

Pod nią mapa:

```
Przygotowanie firmy w AION WORK
→ Połącz
  Organizacja
  Folder firmy
  Wiedza firmy
  Zespół
  Poczta firmy
```

Najpierw rozstrzygnij [wybór procedury](../../references/routines.md#wybór-procedury-w-istniejącym-repozytorium). Dalsze kroki dotyczą wyłącznie wybranego skilla AION.

Stosuj [minimum komunikacji](../../references/communication.md).

1. Połącz konto według kroku **Połącz** ze [startu od „AION start”](../../references/setup.md#start-od-aion-start-początek-mapa-i-logowanie) i [łączenia konta](../../references/connection.md), z tym samym zdaniem o adresie app.aionwork.com i sprawdzeniem wersji wtyczki.
2. Po udanym `get_profile` pobierz rdzeń według [łączenia konta](../../references/connection.md), a potem osobnym wywołaniem sam `przygotuj-firme.md`, pomijając dokumenty już przeczytane. Przy każdym kroku pobieraj sekcje, do których krok odsyła, ścieżką `plik.md#kotwica`, np. `working-folder.md#standard-repo`; gdy serwer nie zwróci sekcji, pobierz cały plik. Metody na dalsze kroki, np. import kontekstu, pocztę albo poranek, dobieraj według odesłań w `przygotuj-firme.md`.
3. Prowadź kroki według `przygotuj-firme.md`. Organizację i folder firmy na GitHubie prowadź według [GitHuba](../../references/github.md), a zapis i wysyłkę według [bezpiecznika](../../references/guard.md). Katalog repo zmieniaj przez `save_team_repository` i potwierdzaj odczytem `list_team_repositories`.

Folder firmy, import kontekstu i wysyłkę na GitHub wykonujesz dopiero po „tak” na konkretną propozycję. Zaproszenia do firmy w AION i do organizacji na GitHubie wysyła właściciel; Ty podajesz listę i miejsca. Nie prosisz o hasła, kody ani tokeny. Płace, oceny ludzi i umowy z ludźmi nie trafiają do folderu firmy.

Gdy zdalna wiedza nie zawiera `przygotuj-firme.md`, nazwij brak aktualnej instrukcji i zaproponuj „AION start”. Nie odtwarzaj metody z pamięci.
