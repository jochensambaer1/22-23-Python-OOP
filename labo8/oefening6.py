#Oefening 6: dierenkooien
    #We moeten onze dieren nog van kooien voorzien. Je werkt verder op de vorige
    #oefening en voorziet nu ook een klasse Kooi
    #Een kooi heeft een identificatienummer en je kan er zoveel dieren in stoppen als
    #nodig (denk aan de ijsbolletjes en de splat operator)
    #Maak een voeg_dieren_toe method aan waarmee je dierobjecten kunt
    #toevoegen (compositie)
    #Zorg ook voor een __str__ method
    
class Dier:
    def __init__(self, naam, leeftijd):
        self.naam = naam
        self.leeftijd = leeftijd

    def __str__(self):
        return f"{self.naam} ({self.leeftijd})"

class Kooi:
    def __init__(self, identificatienummer):
        self.identificatienummer = identificatienummer
        self.dieren = []

    def voeg_dieren_toe(self, *dieren):
        print(f"Kooi {self.identificatienummer}: {dieren}")
        for dier in dieren:
            self.dieren.append(dier)

    def __str__(self):
        dieren_str = ', '.join(str(dier) for dier in self.dieren)
        return f"Kooi {self.identificatienummer}: {dieren_str}"

class Dierentuin:
    def __init__(self, naam):
        self.naam = naam
        self.kooien = []

    def voeg_kooi_toe(self, kooi):
        self.kooien.append(kooi)

    def __str__(self):
        return f"{self.naam}:\n" + '\n'.join(str(kooi) for kooi in self.kooien)

dierentuin = Dierentuin("Zoo van Antwerpen")
print(dierentuin)  # Zoo van Antwerpen:
    



kooi1 = Kooi(1)
kooi1.voeg_dieren_toe(Dier("Leeuw"), Dier("Tijger"), Dier("Jaguar"))
print(kooi1)  # Kooi 1: Leeuw, Tijger, Jaguar

kooi2 = Kooi(2)
kooi2.voeg_dieren_toe(Dier("Aap"), Dier("Olifant"))
print(kooi2)  # Kooi 2: Aap, Olifant
