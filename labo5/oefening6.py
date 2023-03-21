# Oefening 6
# Schrijf een programma dat het woord (of de woorden) weergeeft die het vaakst in
# een bestand voorkomen. Je programma begint met het vragen van de naam van het
# bestand dat moet ingelezen worden aan de gebruiker. Dan zou het elke regel in het
# Python Programming - Labo 5 3
# bestand moeten verwerken. Elke regel moet worden opgesplitst in woorden en alle
# leestekens vóór of achter moeten uit elk woord worden verwijderd. Je programma
# negeert ook de hoofdletters bij het tellen hoe vaak elk woord voorkomt: ‘Favoriet’ en
# ‘favoriet’ bvb zijn dus hetzelfde woord.
import string

# Vraag de gebruiker om de bestandsnaam
filename = input("Geef de bestandsnaam op: ")

# Open het bestand en lees elke regel
with open(filename, 'r') as file:
    wordcount = {}
    for line in file:
        # Maak de regel schoon
        line = line.strip()
        line = line.translate(line.maketrans('', '', string.punctuation))
        line = line.lower()

        # Split de regel in woorden
        words = line.split()

        # Tellen van woord frequenties
        for word in words:
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1

# Zoek de meest voorkomende woorden
max_count = max(wordcount.values())
most_common_words = [word for word, count in wordcount.items() if count == max_count]

# Print de meest voorkomende woorden
print("Het meest voorkomende woord is/zijn:")
for word in most_common_words:
    print(word)
