# Grundlagen zur Verwendung von Discord Bots - APIs
Immer wenn verschiedene Programme oder Programmteile miteinander kommunizieren müssen, verwendet man eine Form von API.

Dies kann in der Programmierung z.B. eine festgelegte Menge an Operationen sein, die der Programmierer benutzen kann.

Im Fall der Discord API werden Daten allerding über das Internet verschickt, dass keine Klassen und Funktionen kennt. Daher müssen die Daten als normaler Text verschickt werden. Es gibt viele Standards, die einem das Übertragen von Datensätzen erleichtern. Discord verwendet eine REST-API, deren Aufbau auch bei vielen anderen Seiten zum Einsatz kommt.
Eine REST-API (Representational State Transfer = repräsentative Zustandsübertragung) ist ähnlich aufgebaut wie eine Website. Sie hat verschiedene Unterseiten, die über die URL erreichbar sind.

Als Beispiel ein Büchergeschäft mit einer Seite für alle Bücher ("/bücher") und eine Liste mit ihren Autoren ("/autoren") und auch einzelnen Autoren ("/autoren/schiller").

Die entsprechende API könnte dann z.B. so aussehen:
* "/api/bücher" - Gibt alle verfügbaren Bücher zurück
* "/api/autoren" - Gibt alle geführten Autoren zurück
* "/api/autoren/\<Autor Name\>" - Gibt die verfügbaren Bücher eines Autor zurück

Diese "Endpunkte" können Daten zurückgeben. Man kann natürlich auch Endpunkte verwenden, die Daten annehmen können, z.B. um eine Bestellung aufzugeben. 
Z.B.: `/api/bestellen?buch=<Name>&anzahl=<Zahl>`

Hier werden Daten mit einem Bezeichner (Buch und Anzahl) und dem entsprechenden Wert übergeben.
Wie das genau funktioniert, ist erstmal nicht so wichtig.

Bei Discord sieht die API ähnlich aus, natürlich dient sie nicht mehr dem Verkauf von Büchern, sondern z.B. der Verwaltung von Server und dem Verschicken von Nachrichten, aber das Prinzip bleibt.

Der Abruf der Details eines Servers sieht z.B. so aus:

`/api/v10/guilds/<id>`

und liefert folgende Daten (Beispiel, muss man nicht alles lesen 😊 ):

```json
{
  "id": "2909267986263572999",
  "name": "Mason's Test Server",
  "icon": "389030ec9db118cb5b85a732333b7c98",
  "description": null,
  "splash": "75610b05a0dd09ec2c3c7df9f6975ea0",
  "discovery_splash": null,
  "approximate_member_count": 2,
  "approximate_presence_count": 2,
  "features": [
    "INVITE_SPLASH",
    "VANITY_URL",
    "COMMERCE",
    "BANNER",
    "NEWS",
    "VERIFIED",
    "VIP_REGIONS"
  ],
  "emojis": [
    {
      "name": "ultrafastparrot",
      "roles": [],
      "id": "393564762228785161",
      "require_colons": true,
      "managed": false,
      "animated": true,
      "available": true
    }
  ],
  "banner": "5c3cb8d1bc159937fffe7e641ec96ca7",
  "owner_id": "53908232506183680",
  "application_id": null,
  "region": null,
  "afk_channel_id": null,
  "afk_timeout": 300,
  "system_channel_id": null,
  "widget_enabled": true,
  "widget_channel_id": "639513352485470208",
  "verification_level": 0,
  "roles": [
    {
      "id": "2909267986263572999",
      "name": "@everyone",
      "permissions": "49794752",
      "position": 0,
      "color": 0,
      "hoist": false,
      "managed": false,
      "mentionable": false
    }
  ],
  "default_message_notifications": 1,
  "mfa_level": 0,
  "explicit_content_filter": 0,
  "max_presences": null,
  "max_members": 250000,
  "max_video_channel_users": 25,
  "vanity_url_code": "no",
  "premium_tier": 0,
  "premium_subscription_count": 0,
  "system_channel_flags": 0,
  "preferred_locale": "en-US",
  "rules_channel_id": null,
  "public_updates_channel_id": null
}
```

Man sieht, dass viel über eine REST-API möglich ist, jedoch kann die Integration in ein Programm manchmal schwer sein, da es sich um reine Daten handelt, die im Programm nicht so leicht verwendbar sind wie z.B. Klassen. Zudem muss man die URL für eine Anfrage manuell zu einem String zusammenbauen und sich ständig um die Authentifizierung kümmern. Das ist alles möglich, jedoch sehr umständlich und unnötig kompliziert.

Aus diesem Grund gibt es sog. "API-Wrapper", die - wie der Name sagt - die API in eine im Programm leicht verwendbare Struktur "einpacken". Im Hintergrund werden dann vom API Wrapper die Anfragen zu Discord verschickt und empfangene Daten aufbereitet, sodass man sie im Programm einfach verwenden kann.
