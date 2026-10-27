---
name: health
description: >-
  Znajdź potencjalne problemy w wybranym folderze — duże binaria, rozrośnięte Markdowny i uszkodzone linki do lokalnych plików — bez modyfikacji danych.
  Jawny wybór AION uruchamia ten skill; zwykłe polecenie tylko bez lokalnego
  przypisania w repo. Przy niejednoznaczności zapytaj, którą procedurę wykonać.
---

Najpierw rozstrzygnij [wybór procedury](../../references/routines.md#wybór-procedury-w-istniejącym-repozytorium). Dalsze kroki dotyczą wyłącznie wybranego skilla AION.

# Diagnostyka folderu AION WORK

1. Ustal wybrany folder i dostęp agenta. Wykorzystaj znaną ścieżkę; przy kilku możliwych folderach zapytaj, który sprawdzić. Katalog firmy nie oznacza dostępu do wszystkich wymienionych repozytoriów. Nie przeglądaj całego katalogu automatycznie; potwierdź dostęp do wybranej kopii zgodnie z [instrukcją GitHub](../../references/github.md). Bez dostępu do plików wyjaśnij ograniczenie; sama wiedza MCP nie udostępnia folderu użytkownika.
2. Przeczytaj [kontrakt health](../../references/health.md). Użyj istniejącego Pythona 3.10+ w środowisku, które widzi folder. Jeśli brakuje interpretera, poprowadź przygotowanie według `references/setup.md`, bez inicjalizacji Git ani instalacji hooków.
3. Uruchom dołączony skrypt tylko dla wybranego folderu. Jeśli użytkownik wskazał wcześniejszy raport tego samego folderu, wykorzystaj go jako `--baseline`. Nie wyszukuj raportów po całym komputerze i nie zapisuj automatycznie stanu w folderze zespołu.
4. Odczytaj JSON. Oddziel znalezione problemy od zakresu niesprawdzonego. Duży plik i powtarzające się wiersze to sygnały do przeglądu, a nie dowód błędu. Jednorazowy pomiar nie dowodzi ciągłego wzrostu.
5. Przedstaw najważniejsze problemy z konkretnymi ścieżkami i rozmiarami. Przy uszkodzonym linku podaj dokument, numer wiersza i oczekiwaną ścieżkę pliku. Nie wklejaj treści dokumentów ani sekretów.
6. Zaproponuj odpowiednią dalszą czynność, np. wydzielenie osobnych tematów Markdown, przeniesienie ciężkich źródeł do właściwego magazynu lub poprawę linku. Sam przegląd nie upoważnia do usuwania, przenoszenia ani przepisywania plików. Nie wykonuj operacji Git, publikacji ani automatycznej naprawy.

Jeśli `complete` jest fałszywe, napisz, czego nie udało się sprawdzić. Jeśli lista wyników została skrócona, wykorzystaj liczniki zamiast twierdzić, że pokazano wszystkie problemy. Brak wyników oznacza tylko brak problemów rozpoznanych w sprawdzonym zakresie, nie certyfikat poprawności folderu.
