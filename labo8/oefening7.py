#Oefening 7: dierentuin extended
    #We werken verder op de vorige oefening en voegen nu ook een Dierentuin
    #klasse toe. Deze klasse zal de volgende functionaliteiten ondersteunen:
    #Een voeg_kooien_toe method via dewelke je kooien kunt toevoegen aan de
    #dierentuin (compositie). Je gebruikt hiervoor een attribuut kooien (zoals in de
    #voorgaande oefeningen)
    #Een __str__ method via dewelke je de kooien kunt afdrukken en de dieren
    #die erin zitten
    #Een dieren_met_kleur method via dewelke je op basis van een kleurkeuze
    #alle dieren met een bepaalde kleur terugkrijgt
    #Een dieren_met_aantal_poten method via dewelke je op basis van een
    #aantal poten alle dieren met dit aantal poten terugkrijgt
    #Een totaal_aantal_poten method via dewelke je het totaal aantal poten van
    #alle dieren in je dierentuin terugkrijgt
    
class Dier:
    def __init__(self, naam, kleur, aantal_poten):
        self.naam = naam
        self.kleur = kleur
        self.aantal_poten = aantal_poten

class Dier:
    def __init__(self, naam, kleur, aantal_poten):
        self.naam = naam
        self.kleur = kleur
        self.aantal_poten = aantal_poten

    def __str__(self):
        return f"{self.naam}, kleur: {self.kleur}, aantal poten: {self.aantal_poten}"


class Kooi:
    def __init__(self, naam, dieren=None):
        self.naam = naam
        if dieren is None:
            dieren = []
        self.dieren = dieren

    def voeg_dier_toe(self, dier):
        self.dieren.append(dier)

    def __str__(self):
        output = f"{self.naam}:"
        for dier in self.dieren:
            output += f"\n- {dier}"
        return output


class Dierentuin:
    def __init__(self, naam, kooien=None):
        self.naam = naam
        if kooien is None:
            kooien = []
        self.kooien = kooien

    def voeg_kooi_toe(self, kooi):
        self.kooien.append(kooi)

    def __str__(self):
        output = f"{self.naam}:"
        for kooi in self.kooien:
            output += f"\n{kooi}"
        return output

    def dieren_met_kleur(self, kleur):
        dieren = []
        for kooi in self.kooien:
            for dier in kooi.dieren:
                if dier.kleur == kleur:
                    dieren.append(dier)
        return dieren

    def dieren_met_aantal_poten(self, aantal_poten):
        dieren = []
        for kooi in self.kooien:
            for dier in kooi.dieren:
                if dier.aantal_poten == aantal_poten:
                    dieren.append(dier)
        return dieren

    def totaal_aantal_poten(self):
        totaal = 0
        for kooi in self.kooien:
            for dier in kooi.dieren:
                totaal += dier.aantal_poten
        return totaal
