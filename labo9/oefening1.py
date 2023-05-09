#Oefening 1: drankjes en hun temperatuur
#Schrijf een klasse Drank waarvan de instances drankjes vertegenwoordigen. Elk
#drankje heeft twee attributen: een naam (die de drank beschrijft) en de ideale
#temperatuur
#Maak verschillende dranken aan en vraag naam en temperatuur op
#Pas de klasse Drank aan zodat temperatuur niet verplicht moet worden
#meegegeven maar zorg voor een defaultwaarde van 20 graden Celsius
#Maak verschillende dranken aan ga na of de standaardwaarde inderdaad wordt
#gerespecteerd
#Maak een nieuwe klasse LogFile aan die geïnitialiseerd wordt met een
#bestandsnaam
#Binnen de __init__ open je het bestand om naar te schrijven en ken je het toe
#aan een instance attribuut bestand
#Maak een method aan via dewelke je een meegegeven string wegschrijft naar
#het bestand
#Maak tenslotte een log-method aan in de klasse Drank waarmee je naam en
#temperatuur laat loggen naar een bepaald bestand
class Drank:
    def __init__(self, naam, temperatuur=20):
        self.naam = naam
        self.temperatuur = temperatuur

    def log(self, bestandsnaam):
        with open(bestandsnaam, 'a') as f:
            f.write(f"{self.naam}: {self.temperatuur}\n")

# aanmaken van verschillende dranken
cola = Drank("Cola", 5)
thee = Drank("Thee", 80)
koffie = Drank("Koffie")

# opvragen van naam en temperatuur
print(cola.naam, cola.temperatuur)
print(thee.naam, thee.temperatuur)
print(koffie.naam, koffie.temperatuur)

# controleren of standaardwaarde wordt gerespecteerd
print(koffie.temperatuur)  # output: 20

# aanmaken van LogFile-klasse
class LogFile:
    def __init__(self, bestandsnaam):
        self.bestandsnaam = bestandsnaam
        self.bestand = open(bestandsnaam, 'w')

    def schrijf(self, tekst):
        self.bestand.write(tekst + '\n')

    def __del__(self):
        self.bestand.close()

# loggen van dranknaam en temperatuur
log_bestand = LogFile("drank.log")
cola.log("drank.log")
thee.log("drank.log")
koffie.log("drank.log")
