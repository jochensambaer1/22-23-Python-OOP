#Oefening 2
#Ziehier de taxi-tarieven voor de stad Antwerpen:
#https://www.taxibedrijfantwerpen.be/prijs-taxi-antwerpen-kost-taxi-antwerpen/. Schrijf
#een functie die de afgelegde afstand (in kilometers) als parameter neemt, alsook ook
#andere nodige parameters (weekend, nacht, luchthaven) om de juiste prijs zoals je
#die op de site geafficheerd ziet te kunnen berekenen. Als resultaat geeft de functie
#de kostprijs van de rit terug. Schrijf binnen een main-functie een programma dat de
#functie demonstreert. Gebruik constanten om de tariefonderdelen weer te geven.# Definieer constanten voor de tariefonderdelen

STARTTARIEF = 5.00 # euro
KILOMETERTARIEF = 2.50 # euro per km
WEEKENDTOESLAG = 0.00 # euro per km
NACHTTOESLAG = 2.50 # euro per rit
LUCHTHAVENTOESLAG = 85.00 # euro per rit

# Definieer een functie die de taxiprijs berekent op basis van de afstand en andere parameters
def bereken_taxiprijs(afstand, weekend=False, nacht=False, luchthaven=False):
    # Bereken het basistarief als het starttarief plus het kilometertarief maal de afstand
    basistarief = STARTTARIEF + KILOMETERTARIEF * afstand
    
    # Voeg eventuele toeslagen toe aan het basistarief
    if weekend: # Als het weekend is, voeg dan de weekendtoeslag toe per km
         basistarief  += 2.50
         basistarief  += WEEKENDTOESLAG * afstand
       
        
    if nacht: # Als het nacht is, voeg dan de nachttoeslag toe per rit
        basistarief += NACHTTOESLAG
        
    if luchthaven: # Als het een luchthavenrit is, voeg dan de luchthaventoeslag toe per rit
        basistarief += LUCHTHAVENTOESLAG
        
    # Rond het eindtarief af op twee decimalen en geef het terug als resultaat
    eindtarief = round(basistarief, 2)
    return eindtarief

# Definieer een main-functie om de bereken_taxiprijs functie te demonstreren met verschillende voorbeelden
def main():
    # Voorbeeld 1: Een rit van 5 km op een doordeweekse dag overdag (geen toeslagen)
    prijs1 = bereken_taxiprijs(5) 
    print(f"Een rit van 5 km kost {prijs1} euro.")
    
    # Voorbeeld 2: Een rit van 10 km op een zaterdagavond (weekend- en nachttoeslag)
    prijs2 = bereken_taxiprijs(10, weekend=True, nacht=True) 
    print(f"Een rit van 10 km kost {prijs2} euro.")
    
    # Voorbeeld 3: Een rit van 15 km naar de luchthaven op een zondagochtend (weekend- en luchthaventoeslag)
    prijs3 = bereken_taxiprijs(15, weekend=True, luchthaven=True) 
    print(f"Een rit van 15 km kost {prijs3} euro.")

# Roep de main-functie aan om het programma te starten    
main()