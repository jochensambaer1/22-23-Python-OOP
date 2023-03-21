# Oefening 4
# Maak een programma dat gehele getallen inleest van de gebruiker, tot een lege lijn
# wordt ingegeven. Het programma toont vervolgens eerst de negatieve getallen,
# gevolgd door alle nullen, en tot slot gevolgd door de positieve getallen. Binnen elke
# groepen worden de getallen getoond in de volgorde in dewelke ze werden
# ingegeven door de gebruiker. Een voorbeeld: als de gebruiker de waarden 5, -2, 2 0,
# -1, 0, 3 en -2 ingeeft moet je programma tot volgende output komen: -2, -1, -2, 0, 0,
# 5, 2 en 3. Je programma print elke waarde uit op een eigen regel.
negative_numbers = []
zeros = []
positive_numbers = []
while True:
    number_input = input("Voer een getal in (leeg om te stoppen): ")
    if number_input == "":
        break # Stop de lus
    else:
        number = int(number_input)
    if number < 0:
        negative_numbers.append(number)
    elif number == 0:
        zeros.append(number)
    else:
        positive_numbers.append(number)
        
for number in negative_numbers:
    print(number)
    
for number in zeros:
    print(number)   
    
for number in positive_numbers:
    print(number)