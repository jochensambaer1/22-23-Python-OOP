#Oefening 13
#Python Programming - Labo 4 5
#Anagrammen kunnen ook uit meerdere woorden bestaan. Bijvoorbeeld: “Marten
#Asmodom Vilijn” en “Mijn naam is Voldemort” als je hoofdletters en spaties niet
#meerekent. Breid oefening 12 uit zodat je programma kan checken of twee zinnen
#anagrammen zijn. Je negeert hierbij hoofdletters, punctuatie en spaties.
import string

def anagram_zinnen(zin1, zin2):
    # Normaliseer de zinnen door hoofdletters, leestekens en spaties te negeren
    zin1_norm = zin1.lower().translate(str.maketrans('', '', string.punctuation + ' '))
    zin2_norm = zin2.lower().translate(str.maketrans('', '', string.punctuation + ' '))

    # Maak dictionaries van de frequenties van de karakters in de genormaliseerde zinnen
    freq1 = {}
    freq2 = {}
    for c in zin1_norm:
        freq1[c] = freq1.get(c, 0) + 1
    for c in zin2_norm:
        freq2[c] = freq2.get(c, 0) + 1

    # Controleer of de dictionaries gelijk zijn
    return freq1 == freq2
