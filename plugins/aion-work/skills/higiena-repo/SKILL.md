---
name: higiena-repo
description: >-
  Higiena repo z AION WORK: krótka lista poprawek w repo albo folderze, w którym pracujesz (duże pliki, rozrośnięte Markdowny i zepsute linki, układ folderów, AGENTS.md i opis repo, wersja wtyczki), a dla właściciela i admina skan, kto w firmie i jak korzysta z metod AION WORK. Niczego nie zmienia bez zlecenia. Używaj na „zrób higienę repo”, „posprzątaj repo”, „sprawdź pliki w folderze”, „zepsute linki” albo „kto u nas korzysta z AION”.
  Jawny wybór AION uruchamia ten skill; zwykłe polecenie tylko bez lokalnego
  przypisania w repo. Przy niejednoznaczności zapytaj, którą procedurę wykonać.
---

Najpierw rozstrzygnij [wybór procedury](../../references/routines.md#wybór-procedury-w-istniejącym-repozytorium). Dalsze kroki dotyczą wyłącznie wybranego skilla AION.

Stosuj [wywołanie rutyny](../../references/routines.md): potwierdź dostęp i pobierz rdzeń, a potem `rutyny/README.md` oraz `rutyny/higiena-repo.md` przez `read_instruction`.

Wykonaj metodę `rutyny/higiena-repo.md` dla jednego repo albo folderu, który wskazuje użytkownik. Kontrolę plików wykonuj dołączonym skryptem według [kontraktu kontroli plików](../../references/health.md); działa także w folderze bez Gita. Samo wywołanie skilla niczego nie przenosi, nie usuwa ani nie wysyła i nie ustawia stałej pory; poprawki wprowadzasz dopiero po zleceniu.
