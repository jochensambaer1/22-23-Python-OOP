#Oefening 15
#In het spel Scrabble heeft elke letter een bepaalde waarde. De totale score van een
#woord is de som van de scores van elke letter. Schrijf een programma dat de
#Scrabble-score voor een woord weergeeft. Maak een dictionary die de letters mapt
#op een letterwaarde. Gebruik vervolgens deze dictionary om de score te berekenen.
#Alle letterwaarden op een rij van scrabble zijn: A=1, B=3, C=5, D=2, E=1, F=4, G=3,
#H=4, I=1, J=4, K=3, L=3, M=3, N=1, O=1, P=3, Q=10, R=2, S=2, T=2, U=4, V=4,
#W=5, X=8, Y=8, Z=4.
letterwaarden = {
    'A': 1, 'B': 3, 'C': 5, 'D': 2, 'E': 1, 'F': 4, 'G': 3,
    'H': 4, 'I': 1, 'J': 4, 'K': 3, 'L': 3, 'M': 3, 'N': 1,
    'O': 1, 'P': 3, 'Q': 10, 'R': 2, 'S': 2, 'T': 2, 'U': 4,
    'V': 4, 'W': 5, 'X': 8, 'Y': 8, 'Z': 4
}

woord = input("Voer een woord in: ").upper()

score = 0

for letter in woord:
    score += letterwaarden.get(letter, 0)

print("De Scrabble-score voor", woord, "is", score)
