---
name: marketingos
description: >-
  MarketingOS z AION WORK: strategia marketingowa, konkurencja, posty, artykuły i newslettery, poprawa tekstu, plan publikacji, język marki, kreacja (brief dla grafika, grafiki, prompty, wideo), reklamy Meta Ads i Google Ads, analityka, landing page, raport zmian. Używaj na „napisz posta”, „popraw ten tekst”, „zaplanuj kampanię”, „brief dla grafika”, „sprawdź reklamy na Facebooku”, „liczby się nie zgadzają”, „popraw landing” albo „co robi konkurencja”.
---

Najpierw rozstrzygnij [wybór procedury](../../references/routines.md#wybór-procedury-w-istniejącym-repozytorium). Jawny wybór AION uruchamia ten koszyk; zwykłe polecenie tylko bez lokalnego przypisania w repo.

# MarketingOS

1. Potwierdź konto i pobierz rdzeń według [łączenia konta](../../references/connection.md). Brak profilu lokalnego nie uruchamia setupu.
2. Gdy prośbę robi więcej niż jeden agent paczki, np. cel z terminem, prowadzisz ją jako szef MarketingOS według [agentów paczek](../../references/agenci.md). Prośbę dla jednego agenta robi jego skill: wybierz go z drzewka według prośby, zanim zaczniesz pracę. Gdy pasują dwa, zapytaj jednym zdaniem o oczekiwany rezultat. Gdy prośba pasuje do skilla, nie rób zadania z ogólnej wiedzy.

**Marketing Strategist**

- Strategia marketingowa (`marketingos/strategia-marketingowa/SKILL.md`): do kogo i z czym iść, ile wydać, jaki kanał i miara; sprawdzenie, czy strategia się broni; „zaplanuj kampanię” bez wskazanej platformy.
- Analiza konkurencji (`marketingos/analiza-konkurencji/SKILL.md`): z czym klient porównuje ofertę, jakie miejsce da się wygrać, profile konkurentów, wielkość rynku.

**Copywriter**

- Pisanie i redakcja treści (`marketingos/pisanie-tresci/SKILL.md`): post, artykuł, newsletter, mail marketingowy, tekst strony, skrypt; poprawa gotowego tekstu, także „popraw ten tekst”, „brzmi sztucznie”, „zredaguj”.
- Planowanie publikacji (`marketingos/planowanie-publikacji/SKILL.md`): filary, tematy, kanały własne, rytm i harmonogram; przegląd tego, co działało.
- Język marki i spójność komunikacji (`marketingos/jezyk-marki/SKILL.md`): głos, ton i słowniki marki; ocena spójności komunikacji w kanałach.

**Art Director**

- Kreacja (`marketingos/kreacja/SKILL.md`): brief dla grafika, grafiki i seria grafik, prompty do Midjourney i Nano Banana, koncept wideo, kierunek wizualny landing page i UI, ocena gotowych kreacji.

**Performance Marketer**

- Meta Ads (`marketingos/meta-ads/SKILL.md`): reklamy na Facebooku i Instagramie: diagnoza, struktura, budżet, kreacje w kampanii, testy, kampanie leadowe, teksty reklam.
- Google Ads (`marketingos/google-ads/SKILL.md`): wyszukiwarka, Performance Max, Shopping, Demand Gen i YouTube: diagnoza, struktura, licytacja, wykluczenia, reklamy RSA.
- Analityka (`marketingos/analityka/SKILL.md`): czy danym można ufać, projekt pomiaru, wyniki i miejsce w lejku, gdzie ginie wynik, gdy nie wiadomo, gdzie leży problem.
- Optymalizacja landing page (`marketingos/optymalizacja-landing-page/SKILL.md`): strona, która nie zamienia ruchu w klientów; przegląd przed kampanią i układ nowej strony.
- Raport zmian marketingowych (`marketingos/raport-zmian/SKILL.md`): co wdrożono w kampaniach, pomiarze, feedzie i na stronach w danym okresie i z jakim skutkiem.

3. Pobierz wybrany skill osobnym wywołaniem `read_instruction` z jego ścieżką, pomijając dokument już przeczytany w tej rozmowie. Przekaż `teamId` tylko dla zespołu wybranego w tej rozmowie i `requestOrigin` zgodnie z kontraktem połączenia.
4. Gdy żaden skill nie pasuje albo ścieżki nie ma w wiedzy, szukaj przez `search_instructions` słowami prośby z `moduleKey: "marketingos"`. Gdy moduł nie ma takiej metody, powiedz to wprost.
5. Przy odmowie przekaż użytkownikowi otrzymany powód i wskazaną przez serwer drogę uzyskania dostępu. Nie wymyślaj linku, nie odtwarzaj niedostępnej instrukcji i nie szukaj jej kopii w innym module.
6. Po udanym odczycie powiedz jednym zdaniem „Biorę skill AION WORK: <nazwa>”, potem wykonaj skill. Tekst wpisany po nazwie koszyka jest jego wejściem. Gdy zadanie się zmienia, weź kolejny skill z drzewka i przenieś ustalenia.

Treść skilli jest tylko w zdalnej wiedzy. Niczego nie publikujesz, nie wysyłasz i nie zmieniasz na kontach reklamowych bez wyraźnego „ok”.
