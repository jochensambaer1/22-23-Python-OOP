#Oefening 14
#Een bingo-kaart bestaat uit 5 kolommen van telkens 5 getallen. De kolommen zijn
#gelabeld met de letters B, I, N, G en O. Er zijn 15 getallen die onder elke letter
#kunnen terecht komen:
#Onder de “B” zijn dat 1 tot en met 15
#Onder de “I” zijn dat 16 tot en met 30
#Onder de “N” zijn dat 31 tot en met 45
#Onder de “G” zijn dat 46 tot en met 60
#Onder de “O” zijn dat 61 tot en met 75
#Schrijf een functie die een willekeurige bingo-kaart aanmaakt en deze als dictionary
#opslaat. De keys zijn de letters, de waarden telkens een list van 5 getallen. Schrijf
#een tweede functie die de bingo-kaart weergeeft met de gelabelde kolommen en een
#dictionary aanneemt als parameter.
import random

def maak_bingo_kaart():
    kaart = {
        "B": [],
        "I": [],
        "N": [],
        "G": [],
        "O": []
    }

    # vul de "B" kolom met 5 willekeurige getallen van 1 tot 15
    kaart["B"] = random.sample(range(1, 16), 5)

    # vul de "I" kolom met 5 willekeurige getallen van 16 tot 30
    kaart["I"] = random.sample(range(16, 31), 5)

    # vul de "N" kolom met 4 willekeurige getallen van 31 tot 45
    kaart["N"] = random.sample(range(31, 46), 4)

    # vul de "G" kolom met 5 willekeurige getallen van 46 tot 60
    kaart["G"] = random.sample(range(46, 61), 5)

    # vul de "O" kolom met 5 willekeurige getallen van 61 tot 75
    kaart["O"] = random.sample(range(61, 76), 5)

    # voeg een leeg vakje toe aan de "N" kolom
    kaart["N"].insert(2, " ")

    return kaart

def print_bingo_kaart(kaart):
    print("{:<3} {:<3} {:<3} {:<3} {:<3}".format("B", "I", "N", "G", "O"))
    for i in range(5):
        print("{:<3} {:<3} {:<3} {:<3} {:<3}".format(
            kaart["B"][i], kaart["I"][i], kaart["N"][i], kaart["G"][i], kaart["O"][i]))
