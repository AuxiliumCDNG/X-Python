# Klassen in Python

## Klassen im Allgemeinen
Eine Klasse in der Programmierung kann man als kleines und unabhängiges Unterprogramm ansehen, dass eine bestimmte Aufgabe hat.
Dazu besitzt eine Klasse sog. Attribute und Methoden. Diese ähneln den bekannten Prinzipien von Variablen(=Attribute) und Funktionen(=Methoden), nur, dass die Attribute und Methoden in einer Klasse auch nur innerhalb dieser funktionieren.

Eine Klasse kann in einem Programm mehrmals verwendet werden, dabei können die Attribute der Klasse verschiedene Werte haben.

Damit man eine Klasse in seinem Programm verwenden kann, muss man diese "instanziieren". Das bedeutet, dass du aus der Klasse, ein sog. Objekt erstellst. Erst dieses Objekt hat tatsächlich funktionierende Attribute/Variablen und erst dann kann man die Methoden/Funktionen der Klasse ausführen.

Da du aus einer Klasse, die selbst noch nicht viel kann, mehrere Objekte erzeugen kannst, die unterschiedliche Werte beinhalten, nennt man eine Klase auch häufig den "Bauplan". Du baust dir also aus einer Klasse, die beschreibt, wie etwas funktioniert, ein Objekt, dass diese Dinge dann auch kann.

## Klassen in Python

In Python sieht das dann so aus:

```python
class Mensch:  # Klasse wird erstellt und Name wird vergeben
    # Attribute, die jedes Objekt von Anfang an haben soll, werden hier notiert:
    ist_menschlich = True

    # Die __init__ Methode wird bei der Instanziierung ausgeführt
    def __init__(self): 
        print("Guten Tag!")
        # Weitere Attribute können hier festgelegt werden
        self.name = input("Wie soll ich heißen?")
    
    # Weitere Methoden werden hier erstellt:
    def vorstellen(self):
        print("Hallo, ich bin", self.name)


# Die Klasse Mensch instanziieren und in der Variable "mensch1" speichern
mensch1 = Mensch()

#  ...eine weitere Instanz/ein weiteres Objekt wird erstellt.
mensch2 = Mensch()

# ... ein dritter Mensch wird geboren.
mensch3 = Mensch()
```

## Parameter für Konstruktor

Möchte man einige Werte - in diesem Beispiel vielleicht der Name und das Alter - kann man diese Werte bei der Instanziierung der __init__ Methode übergeben.
Da diese solche Werte annehmen kann und dabei ein neues Objekt aus den Werten konstruieren kann, nennt man die __init__ Methode auch den Konstruktor. Diese Methode konstruiert also ein Objekt bei seiner Erstellung nach unseren Wünschen.

```python
class Mensch:
    # ...
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
    # ...

# Die Parameter des Konstruktors (hier name und alter) müssen in der selben Reihenfolge bei der Instanziierung gegeben sein:
mensch1 = Mensch("Dieter", 41)
```

Bei der Instanziierung wird der Konstruktor automatisch mit den gegebenen Parametern gestartet...

## Zugriff auf Klassen Methoden und Attribute
Möchtest du Methoden oder Attribute einer Klasse verwenden, musst du die sog. Punktnotation verwenden. Diese funktioniert folgendermaßen:
Zuerst muss du den Namen der Variable verwenden, in der du die Instanz der Klasse gespeichert hast. Dann greifst du über einen Punkt auf dessen Inhalt zu:

```python
print("Du bist ", mensch1.alter, "Jahre alt!")
```

Im folgenden Beispiel enthält ein Attribut der Klasse Mensch ein Objekt der Klasse TShirt:

```python
class TShirt:
    def __init__(farbe, groesse):
        self.farbe = farbe
        self.groesse = groesse


class Mensch:
    def __init__():
        kleidung = TShirt("blau", "M")
        ...

mensch1 = Mensch()
farbe_tshirt = mensch1.kleidung.farbe
```

Man kann also über die Punktnotation auch gleich mehrere Ebenen in eine Klasse bzw. ein Objekt einer Klasse betrachten. Stelle dir die Namen der Attribute und Methoden wie die Namen von Ordnern auf deinem Computer vor. In diese kannst du jeweils über einen "."(Punkt) zugreifen bzw. in diesen hinein gehen.

## Vererbung
Manchmal möchtest du für bestimmte Fälle eine Sache in einer Klasse anpassen oder eine neue Methode haben. Damit die ganze Klassen nicht neu programmiert werden muss, kannst du Attribute und Methoden in neue Klassen "vererben", sie also übernehmen, ohne diese neu zu erstellen.

Die Klasse, die ihre Eigenschaften vererbt nennt man die Superklasse, die, die diese bekommt, die Unterklasse.

Auf Attribute und Methoden der Superklasse kannst du in der Unterklasse mit super().\<bezeichner\> zugreifen.

In Python kannst du eine Klasse so etwas erben lassen:

```python
class Lehrer(Mensch):  # Klasse Leherer erhält alles aus der Klasse Mensch
    # Sowohl neue Parameter als auch jene der vererbten Klasse, müssen dem Konstruktor vorliegen
    def __init__(self, klasse, fach, name, alter):
        # Konstruktor der Superklasse wird ausgeführt:
        # Die Parameter werden aus dem Konstruktor der Unterklasse an den der Superklasse weitergegeben.
        super().__init__(name, alter)
```
