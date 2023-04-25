#Oefening 3: maximum aantal bolletjes
    #We werken verder op de vorige oefening
    #Je voegt hier een attribuut toe op het niveau van de klasse
    #Hoorntje, maximum_bolletjes, zodat maximum drie bolletjes ijs aan een hoorntje
    #kunnen worden toegevoegd
    #Je zorgt ervoor dat in bolletjes_toevoegen eens er drie bolletjes zijn toegevoegd
    #elk volgend bolletje wordt genegeerd. We doen dat met een if statement waarin
    #we het huidige aantal bolletjes vergelijken met ons eerder aangemaakte klasse
    #attribuut

class Hoorntje:
    def __init__(self):
        self.bolletjes = []
        self.maximum_bolletjes = 3
        
    def bolletjes_toevoegen(self, smaak):
        if len(self.bolletjes) < self.maximum_bolletjes:
            self.bolletjes.append(smaak)
            print(f"{smaak} bolletje toegevoegd!")
        else:
            print("Sorry, er kunnen niet meer bolletjes worden toegevoegd.")
            
hoorntje = Hoorntje()
hoorntje.bolletjes_toevoegen("chocolade")
hoorntje.bolletjes_toevoegen("vanille")
hoorntje.bolletjes_toevoegen("aardbei")
hoorntje.bolletjes_toevoegen("pistache")
