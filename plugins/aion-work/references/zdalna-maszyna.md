# Praca na tymczasowej maszynie w chmurze

Czytaj przed pobieraniem repozytorium lub instalowaniem narzędzi w chmurze. Wykryj możliwości według `references/setup.md`; pytaj tylko o brak blokujący bieżącą czynność.

1. Sprawdź możliwości bieżącej sesji: obsługę skilli i MCP, terminal, system plików, istniejącą kopię repozytorium, Git/Python, zasady sieci, uprawnienia GitHub oraz sposób zachowania wyników. Sama nazwa Codex lub Claude Code niczego tu nie gwarantuje; rozmowa w chmurze i zadanie programistyczne mogą mieć różne możliwości.
2. Podstawą jest wyłącznie zdalna wiedza AION, i to dopiero po rzeczywistym połączeniu AION WORK MCP. Nie wymaga repozytorium i nie daje trwałego magazynu dokumentów w AION. Jeśli klient nie obsługuje pluginu lub MCP, jasno zgłoś brak tej możliwości.
3. Wykorzystaj kopię repozytorium przygotowaną przez hosta, jeśli odpowiada wpisowi katalogu właściwej firmy, przeznaczeniu zadania i aktualnym uprawnieniom. Widoczność całego katalogu nie oznacza dostępu hosta do wszystkich repozytoriów; nie klonuj ich na zapas. Jeżeli host wymaga wskazania repozytorium przed rozpoczęciem zadania, poprowadź przez jego interfejs; nie zakładaj, że dowolne `git clone` i logowanie interaktywne działają w izolowanym środowisku.
4. Przed dodatkowym klonowaniem potwierdź dozwolone repozytorium, sieć i uwierzytelnienie. Konektor GitHub może udostępniać API bez danych uwierzytelniających dla terminala. Dozwolona domena nie gwarantuje wszystkich metod HTTP ani dostępu do każdego repozytorium. Po błędzie ustal ograniczenie; nie ponawiaj zabronionej operacji ani nie proś o token w rozmowie.
5. Przed edycją ustal dostępny sposób zachowania wyników: autoryzowany push/PR, eksport artefaktu hosta albo obsługiwane pobranie. Dopiero udany wynik potwierdza zapis poza maszyną tymczasową. Lokalny commit nie wystarcza. Bez takiej drogi ogranicz pracę do odczytu i omówienia albo uzgodnionego wyniku wyłącznie w rozmowie. Nie obiecuj zachowania kopii po wygaśnięciu sesji.
6. Instaluj tylko potrzebne narzędzia, w aktualnym środowisku i w granicach jego uprawnień. Ograniczenie może oznaczać powrót do wiedzy zdalnej lub konfiguracji lokalnej; nie uzasadnia wyłączania zabezpieczeń hosta.
7. Kontynuuj z informacją, co można czytać, edytować i zachować oraz jaki jeden krok pozostał użytkownikowi.

Przed podaniem ustawień hosta sprawdź aktualną oficjalną dokumentację właściwego produktu i wersji. Dokumentacja nie zastępuje potwierdzenia działania w bieżącym kliencie.

- [Środowisko chmurowe Codex](https://learn.chatgpt.com/docs/environments/cloud-environment) i [dostęp do internetu](https://learn.chatgpt.com/docs/cloud/internet-access) — mogą dotyczyć starszego środowiska; dobierz instrukcję do używanego hosta.
- [Claude Code w chmurze](https://code.claude.com/docs/en/claude-code-on-the-web).
