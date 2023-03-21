#Oefening 3
#Python Programming - Labo 3 2
#Een bedrijf biedt verzending voor zijn artikelen tegen een tarief van 8,5 euro voor het
#eerste artikel in een bestelling en 3 euro voor elk volgend artikel in dezelfde
#bestelling. Schrijf een functie die het aantal artikelen in de bestelling als enige
#parameter heeft. Geef als resultaat de verzendkosten terug voor de bestelling. Voeg
#binnen een main-functie een programma toe dat het aantal artikelen leest dat door
#de gebruiker is gekocht en toon de verzendkosten.def verzendkosten(aantal_artikelen):
  # Bereken de verzendkosten voor een bestelling
  # Tarief: 8,5 euro voor het eerste artikel en 3 euro voor elk volgend artikel
  if aantal_artikelen == 0:
    return 0 # Geen verzendkosten voor een lege bestelling
  else:
    return 8.5 + (aantal_artikelen - 1) * 3 # Verzendkosten volgens het tarief

def main():
  # Lees het aantal artikelen dat door de gebruiker is gekocht
  aantal_artikelen = int(input("Hoeveel artikelen heeft u gekocht? "))
  
  # Toon de verzendkosten voor de bestelling
  print("De verzendkosten zijn:", verzendkosten(aantal_artikelen), "euro")

# Roep de main-functie aan
main()