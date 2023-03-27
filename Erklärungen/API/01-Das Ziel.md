# Das Ziel einer API
Eine API wird immer dann verwendet, wenn verschiedene Programme miteinander kommunizieren müssen. Möchte eine Windows App z.B. die Aufmerksamkeit des Benutzers, kann es die APIs von Windows verwenden, um einen Ton abzuspielen oder sich hervorheben zu lassen.
Das wird auch aus dem Namen deutlich: Application Programming Interface (Schnittstelle für die Programmierung einer Anwendung)

Wir schauen uns im Labor erstmal nur APIs im Internet an. Der typische Anwendungsfall wäre z.B. das Abrufen von Daten, die dann auf einer Website angezeigt werden. Beispiel wäre z.B. YouTube (Videoempfehlungen werden geladen) oder Twitter (Tweets werden geladen).
Aber mit einer API kann man nicht nur Daten abrufen, sondern auch verschiedenste Aktionen durchführen. Möchtest du z.B. einen Tweet liken, so schickt dein Browser eine Anfrage an den Entpunkt der Twitter API, der für Likes zuständig ist. In dieser Anfrage sind z.B. eine ID (eindeutige Nummer) des Tweets enthalten.
Man kann also auch Daten mittels einer API zum Entpunkt schicken. Dies passiert z.B. auch, wenn du einen Tweet postest (der Text oder Bilder werden per API zu Twitter geschickt).