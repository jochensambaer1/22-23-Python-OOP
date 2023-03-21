# Oefening 8
# Python gebruikt een hashtag om het begin van een commentaarregel aan te geven.
# Deze regel bestaat vervolgens volledig uit commentaar. In deze oefening maak je
# een programma dat alle opmerkingen uit een Python-bestand verwijdert. Controleer
# elke regel in het bestand om te bepalen of een #-teken aanwezig is. Als dit het geval
# is verwijdert het programma alle tekens van het #-teken tot het einde van de regel
# (we negeren de situatie waarin het commentaarteken ergens in het midden van een
# regel voorkomt). Sla het gewijzigde bestand op met een nieuwe naam. Zowel de
# naam van het invoerbestand als de naam van het uitvoerbestand moeten aan de
# gebruiker worden gevraagd. Zorg ervoor dat er een passend foutbericht wordt
# weergegeven als zich een probleem voordoet bij het openen van één van de
# bestanden.
import os

# Vraag de namen van het invoer- en uitvoerbestand aan de gebruiker
input_file = input("Geef de naam van het invoerbestand: ")
output_file = input("Geef de naam van het uitvoerbestand: ")

# Controleer of het invoerbestand bestaat
if not os.path.exists(input_file):
    print(f"Kan het invoerbestand '{input_file}' niet vinden.")
    exit()

# Open de bestanden
try:
    with open(input_file, "r") as f_in, open(output_file, "w") as f_out:
        # Verwijder alle commentaarregels en schrijf de andere regels naar het uitvoerbestand
        for line in f_in:
            # Controleer of de regel een commentaarregel is
            if "#" in line:
                comment_index = line.index("#")
                line = line[:comment_index] + "\n"
            # Schrijf de regel (zonder commentaar) naar het uitvoerbestand
            f_out.write(line)
except Exception as e:
    print(f"Er is een fout opgetreden: {e}")
