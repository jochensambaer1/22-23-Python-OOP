#Oefening 5
#In deze oefening maak je een Python-programma dat de langste woorden in een
#bestand identificeert. Jouw programma moet een passend bericht weergeven dat de
#lengte van het langste woord bevat, samen met alle woorden van die lengte die in
#het bestand voorkwamen. Behandel elke groep karakters die geen witruimte zijn als
#een woord, zelfs als deze cijfers of leestekens bevat.

import re

# Vraag de bestandsnaam aan de gebruiker
filename = input("Geef de bestandsnaam op: ")

# Open het bestand en lees de inhoud in
with open(filename, 'r') as file:
    content = file.read()

# Vind alle woorden in de inhoud van het bestand
words = re.findall(r'\S+', content)

# Bepaal de lengte van het langste woord
max_length = max(len(word) for word in words)

# Vind alle woorden met dezelfde lengte als het langste woord
longest_words = [word for word in words if len(word) == max_length]

# Geef het resultaat weer
if longest_words:
    print(f"Het langste woord heeft lengte {max_length}:")
    for word in longest_words:
        print(word)
else:
    print("Er zijn geen woorden gevonden in het bestand.")
