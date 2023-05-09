# Oefening 10: De dierentuin 2.0 -
# dierentuinen
# We blijven bij de dieren in de dierentuin en passen nu Dierentuin aan
# Pas dieren_per_kleur aan zodat het verschillende kleuren tegelijk als argument
# kan nemen
# Dieren die voldoen aan één van de kleuren worden teruggegeven.
# Zorg voor twee instances van de Dierentuin klasse die elk een afzonderlijke
# dierentuin vertegenwoordigen
# Zorg voor een manier om dieren te transfereren van de ene dierentuin naar de
# andere. Implementeer hiervoor een verhuis_dier method met als attributen
# ontvangende_dierentuin en een subklasse van Dier als argumenten
# Python Programming - Labo 9 6
# Het eerste dier van het meegegeven type wordt verwijderd uit de dierentuin
# waarop we de method hebben aangeroepen en toegevoegd aan de eerste kooi
# van de ontvangende dierentuin
# Combineer de dieren_met_kleur en dieren_met_aantal_poten methods tot een
# enkele method geef_dieren. Maak gebruik van keyword argumenten (kleur,
# poten) zodat de method zelf kan uitmaken welke query moet gemaakt worden

class Dierentuin:
    def __init__(self, naam):
        self.naam = naam
        self.dieren = []

    def dieren_per_kleur(self, *colors):
        return [dier for dier in self.dieren if dier.kleur in colors]

    def verhuis_dier(self, ontvangende_dierentuin, dier):
        self.dieren.remove(dier)
        ontvangende_dierentuin.dieren.append(dier)
    def geef_dieren(self, **kwargs):
        if 'kleur' in kwargs:
            return self.dieren_per_kleur(kwargs['kleur'])
        elif 'poten' in kwargs:
            return [dier for dier in self.dieren if dier.aantal_poten == kwargs['poten']]
        else:
            return self.dieren


dierentuin1 = Dierentuin("Dierentuin 1")
leeuw = Leeuw("Simba", 4, "geel")
olifant = Olifant("Dumbo", 4, "grijs")
pinguin = Pinguin("Tux", 2, "zwart-wit")
dierentuin1.dieren.extend([leeuw, olifant, pinguin])

# get all animals with 4 legs
vierpoten = dierentuin1.geef_dieren(poten=4)

# get all yellow animals
gele_dieren = dierentuin1.geef_dieren(kleur="geel")
