#Is een string een palindroom? https://nl.wikipedia.org/wiki/Palindroom. Een string is
#een palindroom als het identiek is gelezen van links en rechts en van rechts naar
#links. Zo zijn “meetsysteem” en “stormrots” voorbeelden van palindromen. Schrijf
#een programma dat een string vraagt aan een gebruiker en een loop gebruikt om te
#bepalen of het woord al dan niet een palindroom is. Gebruik print om met een
#betekenisvol bericht eventueel te bevestigen of dat het geval is.
#Tip:
#Je kunt bvb positie 5 van een string opvragen met mijnstring[4]...
#De aantal karakters in een string krijg je met len(mijnstring)...
woord = input("Voer een woord in: ")

omgekeerd = woord[::-1]

if woord == omgekeerd:
    print(woord, "is een palindroom!")
else:
    print(woord, "is geen palindroom.")
