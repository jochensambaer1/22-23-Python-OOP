#Oefening 1
#Schrijf een functie waaraan de lengtes van de twee rechthoekszijden van een
#rechthoekige driehoek moeten meegegeven worden. Geef als resultaat van de
#functie de lengte van de hypotenusa (dit is de schuine zijde) van de driehoek terug,
#berekend met de stelling van Pythagoras. Voeg binnen een main-functie een
#programma toe dat de lengtes van de kortere zijden van een rechthoekige driehoek
#aan de gebruiker vraagt, en de eerste functie gebruikt om de lengte van de
#hypotenusa te berekenen, en het resultaat weergeeft.
import math

def hypotenusa(a,b):

  a2 = a**2
  b2 = b**2

  
  som = a2 + b2

 
  c = math.sqrt(som)

  
  return c

def main():
  
  print("Geef de lengtes van de kortere zijden van een rechthoekige driehoek:")
  a = float(input("a: "))
  b = float(input("b: "))

  
  c = hypotenusa(a,b)

  
  print(f"De lengte van de hypotenusa is {c:.2f}")


if __name__ == "__main__":
    main()