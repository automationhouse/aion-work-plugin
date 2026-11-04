// AION WORK: odczyt kalendarza (baza kalendarzy macOS) i poczty (Apple Mail) na Macu. Tylko odczyt.
// Nagłówki:  osascript -l JavaScript poczta-mac.js [godziny=24] [limit=50]
// Treść:     osascript -l JavaScript poczta-mac.js tresc <id wiadomości>
// Za pierwszym razem macOS pyta o dostęp do kalendarzy i o sterowanie aplikacją Mail.
ObjC.import("EventKit");
ObjC.import("Foundation");

function czas(d) {
  var p = function (n) {
    return (n < 10 ? "0" : "") + n;
  };
  return (
    d.getFullYear() +
    "-" +
    p(d.getMonth() + 1) +
    "-" +
    p(d.getDate()) +
    " " +
    p(d.getHours()) +
    ":" +
    p(d.getMinutes())
  );
}

function dostepDoKalendarza(store) {
  var status = Number(
    $.EKEventStore.authorizationStatusForEntityType($.EKEntityTypeEvent),
  );
  if (status === 3) return true;
  if (status === 1 || status === 2) return false;
  var gotowe = false;
  store.requestFullAccessToEventsWithCompletion(function () {
    gotowe = true;
  });
  var petla = $.NSRunLoop.currentRunLoop;
  for (var i = 0; i < 60 && !gotowe; i++)
    petla.runUntilDate($.NSDate.dateWithTimeIntervalSinceNow(1));
  return (
    Number(
      $.EKEventStore.authorizationStatusForEntityType($.EKEntityTypeEvent),
    ) === 3
  );
}

function kalendarz() {
  var wynik = ["KALENDARZ (dziś i jutro): czas | wydarzenie | kalendarz"];
  try {
    var store = $.EKEventStore.alloc.init;
    if (!dostepDoKalendarza(store)) {
      return wynik
        .concat([
          "BŁĄD KALENDARZA: brak zgody na odczyt. Ustawienia systemowe, Prywatność i ochrona, Kalendarze: pełny dostęp dla aplikacji, w której pracujesz.",
        ])
        .join("\n");
    }
    var start = $.NSCalendar.currentCalendar.startOfDayForDate($.NSDate.date);
    var koniec = start.dateByAddingTimeInterval(2 * 24 * 3600);
    var zdarzenia = store.eventsMatchingPredicate(
      store.predicateForEventsWithStartDateEndDateCalendars(start, koniec, $()),
    );
    var lista = [];
    for (var i = 0; i < zdarzenia.count; i++) {
      var z = zdarzenia.objectAtIndex(i);
      lista.push({
        t: new Date(z.startDate.timeIntervalSince1970 * 1000),
        n: ObjC.unwrap(z.title) || "(bez tytułu)",
        k: ObjC.unwrap(z.calendar.title) || "",
      });
    }
    lista.sort(function (a, b) {
      return a.t - b.t;
    });
    lista.forEach(function (z) {
      wynik.push(czas(z.t) + " | " + z.n + " | " + z.k);
    });
    if (lista.length === 0) wynik.push("Brak wydarzeń dziś i jutro.");
  } catch (e) {
    wynik.push("BŁĄD KALENDARZA: " + e);
  }
  return wynik.join("\n");
}

function poczta(godziny, limit) {
  var wynik = [
    "POCZTA (ostatnie " + godziny + " h): czas | nadawca | temat | status | id",
  ];
  try {
    var Mail = Application("Mail");
    var od = new Date(Date.now() - godziny * 3600 * 1000);
    var listy = Mail.inbox.messages.whose({
      dateReceived: { _greaterThan: od },
    })();
    var n = 0;
    for (var i = 0; i < listy.length && n < limit; i++) {
      var m = listy[i];
      wynik.push(
        czas(m.dateReceived()) +
          " | " +
          m.sender() +
          " | " +
          m.subject() +
          " | " +
          (m.readStatus() ? "przeczytany" : "nieprzeczytany") +
          " | " +
          m.id(),
      );
      n++;
    }
    if (n === 0)
      wynik.push("Brak nowych wiadomości w skrzynce odbiorczej Apple Mail.");
  } catch (e) {
    wynik.push("BŁĄD POCZTY: " + e);
  }
  return wynik.join("\n");
}

function tresc(id) {
  try {
    var m = Application("Mail").inbox.messages.whose({ id: id })()[0];
    return (
      "OD: " +
      m.sender() +
      "\nTEMAT: " +
      m.subject() +
      "\nDATA: " +
      czas(m.dateReceived()) +
      "\n\n" +
      m.content()
    );
  } catch (e) {
    return "BŁĄD: nie znalazłem wiadomości " + id + ": " + e;
  }
}

function run(argv) {
  if (argv.length > 1 && argv[0] === "tresc")
    return tresc(parseInt(argv[1], 10));
  var godziny = argv.length > 0 ? parseInt(argv[0], 10) : 24;
  var limit = argv.length > 1 ? parseInt(argv[1], 10) : 50;
  return kalendarz() + "\n\n" + poczta(godziny, limit);
}
