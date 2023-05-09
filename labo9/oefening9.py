# Oefening 9: De dierentuin 2.0 - kooien
# Bestudeer de oefeningen uit het vorige labo mbt de dieren in de dierentuin
# Er zijn momenteel geen beperkingen qua aantal dieren per kooi
# Je beperkt het aantal dieren per kooi en maakt een GroteKooi klasse aan (zoals
# bij de hoorntjes)
# Je gebruikt hierbij hoeveel ruimte een dier nodig heeft en zorgt dat dat niet
# groter (voor het totaal aantal dieren dat in de kooi zit) is dan een bepaalde kooi
# ruimte biedt
# Gebruik hiervoor een ruimte_nodig attribuut bij elk dier en een
# ruimte_beschikbaar attribuut bij Kooi/GroteKooi
# Definieer een dictionary waarin je beschrijft welke dieren bij welke andere dieren
# mogen zitten. Keys: klasses en values: list van klasses die compatibel zijn met
# dat bepaalde dier
# Wanneer je een dier toevoegt aan een kooi check je voor compatibiliteit.
# Wanneer dat niet het geval is, zorg je ervoor dat het dier niet wordt toegevoegd
class Dier:
    def __init__(self, naam, ruimte_nodig):
        self.naam = naam
        self.ruimte_nodig = ruimte_nodig

class Kooi:
    def __init__(self, naam, ruimte_beschikbaar):
        self.naam = naam
        self.ruimte_beschikbaar = ruimte_beschikbaar
        self.dieren = []

    def voeg_dier_toe(self, dier):
        if self.ruimte_beschikbaar >= dier.ruimte_nodig:
            self.dieren.append(dier)
            self.ruimte_beschikbaar -= dier.ruimte_nodig
            return True
        else:
            return False

class GroteKooi(Kooi):
    def __init__(self, naam, ruimte_beschikbaar):
        super().__init__(naam, ruimte_beschikbaar)

    def voeg_dier_toe(self, dier):
        if isinstance(dier, Hoorntje):
            return super().voeg_dier_toe(dier)
        else:
            return False

class Leeuw(Dier):
    def __init__(self):
        super().__init__('Leeuw', 4)

class Olifant(Dier):
    def __init__(self):
        super().__init__('Olifant', 10)

class Hoorntje(Dier):
    def __init__(self):
        super().__init__('Hoorntje', 1)

# Define dictionary of compatible animals
compatibel = {
    Leeuw: [Hoorntje],
    Olifant: [],
    Hoorntje: [Leeuw, GroteKooi]
}

# Create a lion and a small cage
leeuw = Leeuw()
kleine_kooi = Kooi('Kleine kooi', 5)

# Attempt to add lion to small cage
if kleine_kooi.voeg_dier_toe(leeuw):
    print(f'{leeuw.naam} added to {kleine_kooi.naam}')
else:
    print(f'{leeuw.naam} could not be added to {kleine_kooi.naam}')

# Create a horned animal and a large cage
hoorntje = Hoorntje()
grote_kooi = GroteKooi('Grote kooi', 20)

# Attempt to add horned animal to large cage
if grote_kooi.voeg_dier_toe(hoorntje):
    print(f'{hoorntje.naam} added to {grote_kooi.naam}')
else:
    print(f'{hoorntje.naam} could not be added to {grote_kooi.naam}')

# Attempt to add lion to large cage
if grote_kooi.voeg_dier_toe(leeuw):
    print(f'{leeuw.naam} added to {grote_kooi.naam}')
else:
    print(f'{leeuw.naam} could not be added to {grote_kooi.naam}')
