#Schrijf een programma dat de gebruiker vraagt om een lengte en breedte van een
#kamer in te geven (twee afzonderlijke variabelen). Eens deze waarden ingelezen zijn
#berekent je programma de oppervlakte van de kamer. De lengte en de breedte
#zullen ingegeven worden als komma-getallen. Voeg eenheden toe in de output-
#Python Programming - Labo 1 2
#boodschap (meter). Gebruik de float()-functie om de ingegeven waarden om te
#zetten van string naar float.
lenkte = input("lengte ? ")
breete  = input("breete  ? ")
opervlakte = int(lenkte)*int(breete)
boodschap = f"de opervlakte is {opervlakte}"
print(boodschap) 