class Mensch:
    haarfarbe = ""
    groese = 0
    name = ""
    alter = 0

    def __init__(self, name, alter, groesse, haarfarbe):
        self.name = name
        self.alter = alter
        self.groese = groesse
        self.haarfarbe = haarfarbe

    def vorstellen(self):
        print("Hi, ich bin", self.name)

    def name_aendern(self, neuer_name):
        self.name = neuer_name

    def altern(self):
        self.alter += 1


gustav = Mensch("Gustav", 27, 181, "grün")
gustav.vorstellen()


class Lehrer(Mensch):
    faecher = []
    klassen = []

    def __init__(self, faecher, klassen, name, alter, groesse, haarfarbe):
        super().__init__(name, alter, groesse, haarfarbe)
        self.faecher = faecher
        self.klassen = klassen

    def sage_faecher(self):
        print("Ich unterrichte folgende Fächer:", self.faecher)


schmidt = Lehrer(["Mathe", "Deutsch"], ["10c", "7b"], "Schmidt", 60, 180, "grau")
schmidt.sage_faecher()
schmidt.vorstellen()
