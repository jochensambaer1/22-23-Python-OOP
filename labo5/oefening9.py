# Oefening 9
# Schrijf een programma dat een bestand leest dat een lijst met woorden bevat, er
# willekeurig twee selecteert en ze samenvoegt om een wachtwoord te produceren.
# Zorg er bij het maken van het wachtwoord voor dat de totale lengte tussen 12 en 15
# tekens is en dat elk gebruikt woord ten minste drie letters lang is. Zet elk woord in
# het wachtwoord met een hoofdletter, zodat de gebruiker gemakkelijk kan zien waar
# het ene woord eindigt en het volgende begint. Tot slot geeft je programma het
#  wachtwoord weer.
import random

def read_words(filename):
    """
    Leest alle woorden uit het bestand en retourneert een lijst met woorden.
    """
    with open(filename, 'r') as file:
        words = [word.strip() for word in file.readlines()]
    return words

def generate_password(words):
    """
    Selecteert willekeurig twee woorden en voegt ze samen om een wachtwoord te maken.
    Zorgt ervoor dat de totale lengte tussen 12 en 15 tekens is en elk woord ten minste
    drie letters lang is.
    """
    while True:
        first_word, second_word = random.sample(words, 2)
        password = first_word.capitalize() + second_word.capitalize()
        if len(password) >= 12 and len(password) <= 15 and len(first_word) >= 3 and len(second_word) >= 3:
            return password

# Vraag de naam van het bestand aan de gebruiker
filename = input("Geef de naam van het bestand met woorden: ")

# Lees alle woorden uit het bestand
words = read_words(filename)

# Genereer een wachtwoord en geef het weer
password = generate_password(words)
print("Uw wachtwoord is:", password)
