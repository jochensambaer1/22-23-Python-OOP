#Schrijf een programma dat een integer getal vraagt aan de gebruiker. Jouw
#programma geeft dan een boodschap terug met of het hier om een even of oneven
#getal gaat. Tip: gebruik de modulus operator (%) om te bepalen of een getal even of
#oneven is.
getal=int(input("geef een getal in "))
if getal % 2 == 0: 
    print(f"Het getal {getal} is deelbaar door 2") 
else:
    print(f"Het getal {getal} is niet deelbaar door 2") 