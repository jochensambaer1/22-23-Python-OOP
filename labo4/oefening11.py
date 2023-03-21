#Oefening 11
#Maak een programma die het aantal unieke karakters bepaalt en weergeeft in een
#string die door de gebruiker werd ingegeven. Bijvoorbeeld: “Ik hou van Python!”
#heeft 13 unieke karakters. Gebruik een dictionary om dit probleem op te lossen.
def aantal_unieke_karakters(string):
    unieke_karakters = {}
    for karakter in string:
        if karakter not in unieke_karakters:
            unieke_karakters[karakter] = 1
    return len(unieke_karakters)

# Voorbeeldgebruik
string = "Ik hou van Python!"
aantal = aantal_unieke_karakters(string)
print(f"De string '{string}' heeft {aantal} unieke karakters.")
