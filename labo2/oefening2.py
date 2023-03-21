#Een mensenjaar, zo wordt gezegd, komt overeen met 7 hondenjaren. Honden
#bereiken evenwel de volwassenheid in gemiddeld 2 jaar. Soms wordt gedacht dat
#het beter is de eerste 2 mensenjaren als 10,5 hondenjaar te beschouwen en elk
#volgend jaar als 4 hondenjaren. Schrijf een programma dat deze berekening maakt
#voor een hond, van mensenjaren naar hondenjaren. Zorg dat het werkt voor honden
#die jonger zijn dan drie en geef een bericht terug als de gebruiker een negatief getal
#invoert.
mensenjaaren=int(input("geef een hoeveelhijt mensenjaaren in"))
if mensenjaaren >= 2:
     hondenjaaren  = mensenjaaren * 10.5
elif mensenjaaren <0:
    print("het is niet mogelij dat je een egatief numer in geefet  ")     
else :
    hondenjaaren  = mensenjaaren * 4
    
    print(f"de hont is {mensenjaaren}en is{hondenjaaren}honden jaaren  ")
