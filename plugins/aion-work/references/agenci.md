# Agenci paczek w aplikacji

Przebieg szefa paczki stoi w zdalnej wiedzy, w `agenci.md`: cel, rozdział pracy i kolejności, zlecenia, złożenie, sprawdzenie i akceptacja. Ten plik mówi tylko, jak w danej aplikacji uruchomić agenta. Gdy prośbę robi więcej niż jeden agent paczki, pobierz `agenci.md` razem z indeksem paczki jednym `read_instruction` i prowadź według nich.

## Agenci

- MarketingOS: [Marketing Strategist](../agents/marketing-strategist.md), [Copywriter](../agents/copywriter.md), [Art Director](../agents/art-director.md), [Performance Marketer](../agents/performance-marketer.md).
- SalesOS: [Business Developer](../agents/business-developer.md), [Closer](../agents/closer.md), [Offer Specialist](../agents/offer-specialist.md), [Sales Manager](../agents/sales-manager.md).
- CustomerOS: [Onboarding Manager](../agents/onboarding-manager.md), [Account Manager](../agents/account-manager.md), [Expansion Manager](../agents/expansion-manager.md), [Retention Manager](../agents/retention-manager.md).
- AI Powered CEO: [Business Strategist](../agents/business-strategist.md), [Operations Manager](../agents/operations-manager.md), [People Manager](../agents/people-manager.md), [Finance Manager](../agents/finance-manager.md).

## Uruchomienie

- **Claude Code:** agent to podagent wtyczki o nazwie `aion-work:<plik bez .md>`, np. `aion-work:copywriter`. Zlecenie przekazujesz jako jego polecenie. Zlecenia, które od siebie nie zależą, uruchamiasz w jednej odpowiedzi, żeby pracowały naraz.
- **Codex:** wtyczka nie dostarcza nazwanych agentów. Uruchamiasz podagenta i dajesz mu treść pliku agenta z listy wyżej razem ze zleceniem. Niezależne zlecenia uruchamiasz naraz.
- **Bez podagentów:** wykonujesz zlecenia po kolei w tej rozmowie, według pliku agenta, i przed każdym mówisz, który agent pracuje.

Podagent nie widzi tej rozmowy. Zlecenie zawiera wszystko, czego potrzebuje: cel i miarę, ustalenia, wymagania od agentów przed nim, ścieżkę skilla, `teamId` i `requestOrigin`. Wynik podagenta to materiał dla szefa: zapis w folderze, wysyłka i publikacja idą dopiero po „ok” osoby, według wiedzy.
