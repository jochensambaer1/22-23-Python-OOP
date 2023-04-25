#Oefening 5: dierentuin
    #Voor de volgende drie oefeningen gaan we een reeks klassen definiëren die
    #alles combineren: klassen, methods, attributen, compositie en overerving
    #Je bent medewerker van een dierentuin. Deze dierentuin bevat verschillende
    #diersoorten, waarvan sommigen met elkaar een kooi delen
    #Elke soort krijgt zijn eigen klasse. Elk object van een bepaalde klasse deelt
    #een soort en aantal_poten attribuut. Als attribuut kan je per dier ook nog een
    #Python programming - Labo 8 3
    #bepaalde kleur meegeven. Je kan dus een bepaalde kleur meegeven: oSchaap1
    #= Schaap('zwart')
    #Je maakt vier dierklassen aan: wolf, schaap, slang en papegaai
    #Deze klassen erven van de klasse Dier waarin je zoveel mogelijk functionaliteit
    #stopt
    #Deze klasse bevat ook een __str__ functie waarmee je de details over het dier
    #kunt rapporteren
    #Soort? self.soort = self.__class__.__name__ binnen de klasse Dier
    



class IceCream:
    def __init__(self, flavor):
        self.flavor = flavor

class Cone:
    def __init__(self):
        self.scoops = []

    def voeg_toe(self, bolletje):
        if len(self.bolletjes) < 3:
            self.bolletjes.append(bolletje)
        else:
            print("Dit hoorntje kan niet meer dan 3 bolletjes ijs aan!")

class Reuzehoorntje(Hoorntje):
    def voeg_toe(self, bolletje):
        if len(self.bolletjes) < 5:
            self.bolletjes.append(bolletje)
        else:
            print("Dit reuzehoorntje kan niet meer dan 5 bolletjes ijs aan!")
