# Oefening 10
# Schrijf een programma dat een bestand met informatie over chemische elementen
# inleest en opslaat in een of meer geschikte datastructuren. Vervolgens zou je
# programma invoer van de gebruiker moeten lezen en verwerken. Als de gebruiker
# een geheel getal invoert, moet je programma het symbool en de naam van het
# element met het aantal ingevoerde protonen weergeven. Als de gebruiker een nietgehele waarde invoert, moet je programma het aantal protonen weergeven voor het
# element met die naam of dat symbool. Je programma zou een passende
# foutmelding moeten weergeven als er geen element bestaat voor de naam, het
# symbool of het aantal ingevoerde protonen. Ga door met het lezen van invoer van
# de gebruiker totdat er een lege regel is ingevoerd.
import csv

# Open het bestand en sla het op in een dictionary
elements = {}
with open('periodic_table.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        symbol = row['Symbol']
        elements[symbol] = row

# Lees invoer van de gebruiker en verwerk deze
while True:
    user_input = input('Voer een atoomnummer, symbool of naam van een element in (druk op Enter om te stoppen): ')
    if not user_input:
        break

    try:
        # Probeer de invoer van de gebruiker te converteren naar een geheel getal (voor atoomnummer)
        atomic_number = int(user_input)
        # Zoek het element met het overeenkomstige atoomnummer en print de informatie
        for element in elements.values():
            if int(element['AtomicNumber']) == atomic_number:
                print(f"Symbool: {element['Symbol']}, Naam: {element['Name']}")
                break
        else:
            print('Geen element gevonden met het opgegeven atoomnummer.')

    except ValueError:
        # Als de invoer van de gebruiker geen geheel getal is, probeer dan het symbool of de naam te vinden
        element = elements.get(user_input.capitalize())
        if element:
            print(f"Atoomnummer: {element['AtomicNumber']}, Naam: {element['Name']}")
        else:
            print('Geen element gevonden met de opgegeven naam of symbool.')
