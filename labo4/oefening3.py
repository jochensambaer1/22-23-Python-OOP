# Oefening 3
# Schrijf een programma dat woorden aan de gebruiker als input vraagt zolang de
# gebruiker geen lege lijn teruggeeft. Nadat dit laatste gebeurd is geeft het programma
# elk woord dat is ingevoerd exact één keer terug. De woorden moeten weergegeven
# worden in dezelfde volgorde als ze werden ingevoerd. Bvb als de gebruiker
# volgende woorden heeft ingegeven:
# Python Programming - Labo 4 2
# Python
# Rust
# Ruby
# Python
# JavaScript
# Rust
# Dan geeft het programma het volgende terug:
# Python
# Rust
# Ruby
# JavaScript
# Maak een lege lijst om de unieke woorden op te slaan
unique_words = []

# Gebruik een while-lus om de invoer van de gebruiker te krijgen
while True:
    # Vraag een woord aan de gebruiker
    word = input("Geef een woord: ")

    # Controleer of de invoer leeg is
    if word == "":
        # Stop de lus
        break
    else:
        # Controleer of het woord al in de lijst staat
        if word not in unique_words:
            # Voeg het woord toe aan de lijst
            unique_words.append(word)

# Druk de lijst met unieke woorden af
print("De unieke woorden zijn:", unique_words)
