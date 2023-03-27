# APIs im Internet
Will man Resourcen über das Internet (bzw. in unserem Fall das eigene Heimnetz) erreichen, kann man sich diese leider nicht einfach per Import ins Programm holen.
Das Internet funktioniert über bestimmte Protokolle.

Das wohl verbreiteste ist HTTP (Hypertext Transfer Protokoll), welches ursprünglich und auch heute noch für die Übertragung von Websitedaten konzipiert wurde, heute aber auch häufig für APIs und mehr verwendet wird. Du verwendest dieses Protokoll gerade, um dir diese Seite anzusehen (s.h. https://... oben im Browser).

Das "s" in https steht dabei für die verschlüsselte Variante des Protokolls (secure=sicher). Beim "normalen" HTTP wird alles offen/im Klartext versendet, daher sieht man heutzutage fast ausschließlich https statt http.

Das HTTP Protokoll ist zustandslos (stateless). D.h., dass sich weder des Server noch der Client (=das Gerät, dass die Anfragen schickt) etwas übereinander merken - nach jeder Anfrage werden alle Daten sofort wieder vergessen (zumindest seitens des Protokolls - man kann natürlich z.B. eine Speicherung selbst programmieren).
Das hat zur Folge, dass man bei jeder Anfrage von null beginnen muss. Beispiel: Fragt man einen Datensatz an, der mehrere Seiten hat (weil er für eine Anfrage zu groß ist), kann man nicht einfach "die nächste Seite" bei der API anfragen. Dieses Problem wird häufig durch die Anforderung bestimmter Seitennummern oder über einen "Startwert" (man fragt die Daten ab dem Wert an, den mal als letztes hat) gelößt.

# Wie funktioniert die Kommunikation? (Das HTTP Protokoll)
Wie oben schon angeschnitten gibt es bei APIs über HTTP eine klare Ordnung.

Es gibt einen Server, der die Endpunkte bereitstellt (diesen Programmieren wir über Flask).
Und es gibt einen Client, der Daten vom Server abruft bzw. dessen Entpunkte anspricht.

Eine Kommunikation geht dabei IMMER vom Client aus. Dieser muss eine Anfrage (wie diese aussieht kommt später) an den Server schicken, erst dann kann der Server dem Client antworten. Jede Anfrage eines Client muss vom Server innerhalb einer bestimmten Zeit beantwortet werden, sonst wirft der Client einen Fehler oder stürzt sogar ab.

Nach dieser Antwort des Servers ist die Kommunikation beendet und "alles ist vergessen" (=Zustandslos). Z.B. kann der Server auch keine zweite Antwort mehr "nachschicken".

Eine typische Reihenfolge für einen API Call (heißt anfragen/abrufen der API) ist z.B.:

1. Der Client (eine Website wie Twitter) benötgt Daten, weil der User so weit gescrollt hat, dass neue Tweets geladen werden müssen.
2. Der Client bereitet seine Anfrage vor (fügt z.B. seine Zugangsdaten in die Anfrage ein, setzt den "Startwert", ab dem Daten geholt werden sollen etc.).
3. Der Client schickt seine Anfrage über das Protokoll HTTP(S) an die API und erwartet eine Antwort.
4. Der Server erhält die Anfrage - Anhand des Pfads der Anfrage kann der Server der Anfrage dem entsprechenden Endpunkt zuordnen.
5. Die entsprechende Logik des Entpunkts wird ausgeführt (bei uns eine Python Funktion mit @app.route)
6. Die Logik/der Programmcode resultiert in einer Antwort für den Client, diese wird dem Client auf seine Anfrage geantwortet.
7. Der Client erhält die Antwort und damit die Daten, die er angefordert hat.

## Aufbau einer Anfrage
Zuerst muss man wissen, dass es verschiedene Fälle für Anfragen gibt, die in den sog. "Methoden" wiedergespiegelt sind. Z.B.:

* `GET` ruft Daten ab
* `POST` schickt Daten
* `PUT` erstellt neue Elemente auf dem Server (oft aber auch über POST gelöst)
* `DELETE` löscht Elemente auf dem Server

Eine HTTP Anfrage an sich besteht aus mehreren Komponenten:

1. Die Anfrage selbst bestehend aus der Methode (s.h. oben), dem Ziel der Anfrage (z.B. `/api/text/get`) und dem verwendeten Protokoll (bei uns meist `HTTP/1.1`) (`1.1` gibt hier die Version des Protokolls an, es gibt auch `HTTP/1.0` oder `h2`). Je nach Methode auch der sog. Querystring (z.B. `?text=TEST&farbe=green`)
2. HEADER/Kopfzeilen der Anfrage. Diese enthalten allgemeine Informationen über die Anfrage. Z.B. was für ein Browser verwendet wird, welche Daten gesendet werden (z.B. Bilder, PDF oder json) etc. Im Fall von Twitter und co. werden so auch die Zugangsdaten mitgeschickt.
3. BODY/Körper der Anfrage. Hier folgen alle Daten, die mit der Anfrage versendet werden sollen. In unserem Fall Daten im JSON Format. Beispiel Twitter: Inhalt eines Tweets.

Die meisten Komponenten einer Anfrage werden von deinem Browser beim Aufruf der API automatisch erzeugt. Du musst nur die Adresse der API angeben (wird in der Flask Konsole angezeigt), das Ziel der Anfrage eingeben und ggf. auch einen Querystring. Das Protokoll, die Methode (beim Aufruf über den Browser immer `GET`), die HEADER und der BODY wird vom Browser automatisch erzeugt und zur API geschickt. Auch werden diese von Flask automatisch verarbeitet, sodass wir z.B. Daten aus dem Querystring sofort über die Variable `request` abrufen können.

## Aufbau eines Querystring
Über den Querystring werden Daten bei Calls (Abrufen/Anfragen) der Methode `GET` zum Server geschickt. Man gibt z.B. an, zu welchem Tweet genau Daten abgerufen werden sollen.

Der Querystring beginnt optional direkt nach dem Ziel/Pfad der Anfrage. Er beginnt mit `?`. Der Querystring enthält Schlüssel/Wert Paare im folgenden Format: `schlüssel=wert`.

Wenn mehrere Paare übergeben werden sollen, werden diese mit `&` getrennt. Das sieht dann insgesamt so aus:

_`http://api-adresse/ziel/der/anfrage`_**`?schlüssel1=wert1&schlüssel2=wert2&schlüssel3=wert3`**

## Aufbau einer Antwort
1. Der Status der Antwort bestehend aus Protokollversion, Status Code, Status Text (Z.B. `HTTP/1.1 404 Not Found`).
2. HEADER: Allgemeine Informationen wie bei einer Anfrage z.B. Art der Daten (Bild, PDF, JSON etc.); Spezifische Informationen über die Antwort z.B. verwendeter Server etc.
3. BODY: Enthält alles weitere, was der Server antworten möchte. In der Regel sind das die angeforderten Daten, oder ggf. Fehlermeldungen. Je nach Statuscode ist der BODY optional. Z.B. enthalten Antworten mit dem Status `201 Created` oder `204 Not Content` meist keinen BODY.

Eine Liste der HTTP Statuscode ist hier zu finden: <https://de.wikipedia.org/wiki/HTTP-Statuscode>