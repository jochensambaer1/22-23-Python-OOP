# Oefening 1
# Schrijf een programma dat gehele getallen van de gebruiker leest en opslaat in een
# list. Je programma gaat door met het lezen van waarden totdat de gebruiker 0
# invoert. Dan zou het alle waarden moeten weergeven die door de gebruiker zijn
# ingevoerd (behalve de 0) in oplopende volgorde, met één waarde op elke regel.
# Gebruik ofwel de sort method of de sorted-functie om de list te ordenen.
# A list with 3 integers
numbers = []
getal = int(input('geef een getal  '))


while getal != 0:
    numbers.append('geef een numer in on te testen ')
    getal = int(input('geef een getal  '))
    numbers.sort()
    print(numbers)

print(numbers)
# Maak een lege list
numbers = []

# Lees getallen van de gebruiker totdat 0 wordt ingevoerd
while True:
    number = int(input("Voer een getal in (0 om te stoppen): "))
    if number == 0:
        break  # Stop de lus
    else:
        numbers.append(number)  # Voeg het getal toe aan de list

# Sorteer de list in oplopende volgorde
numbers.sort()

# Druk de gesorteerde getallen af
for number in numbers:
    print(number)
