# Oefening 4
# Schrijf een functie waaraan drie getallen als parameters meegegeven worden die als
# resultaat de mediaan (het midden) van die parameters teruggeeft. Voeg een
# programma toe dat drie waarden leest van de gebruiker en hun mediaan weergeeft.
# Hoe bereken je de mediaan of midden? Met midden wordt het middelste element in
# de verdeling of de geordende verzameling bedoeld: bvb de mediaan van 4, 3 en 8 is
# 4.

import statistics


def mediaanberekenen(a, b, c):

    lijst = [a, b, c]

    return statistics.median(lijst)


getal1 = float(input("Voer het eerste getal in: "))
getal2 = float(input("Voer het tweede getal in: "))
getal3 = float(input("Voer het derde getal in: "))


mediangetal = mediaanberekenen(getal1, getal2, getal3)
print(f"De mediaan van {getal1}, {getal2} en {getal3} is {mediangetal}.")
