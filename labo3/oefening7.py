#Oefening 7
#Python Programming - Labo 3 3
#Je maakt een functie is_integer() die nagaat of de karakters in een string een integer
#vertegenwoordigen. Je verwijdert alle eventuele witruimte voor en na de ingevoerde
#string. Je geeft True terug als de lengte na verwijderen van witruimte minstens 1
#bedraagt en enkel uit getallen bestaat, of als het eerste karakter een + of een - is en
#de rest allemaal getallen. Schrijf in een mai-functie een programma dat een string
#vraagt aan de gebruiker en teruggeeft of het hier al dan niet om een integer gaat.
#Zorg ervoor dat het programma niet loopt als deze oplossing wordt ge�mporteerd
#binnen een ander programma.
def is_integer(string):
   
    string = string.strip()
    
    if len(string) == 0:
        return False
   
    string = string.lstrip('+-')
    
    return string.isdigit()

if __name__ == '__main__':
    
    s = input("Geef een string: ")
    
    if is_integer(s):
        print("Dit is een integer.")
    else:
        print("Dit is geen integer.")