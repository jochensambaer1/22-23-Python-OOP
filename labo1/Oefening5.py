#Je schrijft een programma dat berekent hoeveel statiegeld moet worden uitbetaald
#aan iemand die flessen komt inleveren. Er kunnen kleine flesjes worden
#teruggegeven en grote flessen. De kleine leveren 0,12eur statiegeld op, de grote
#0,25eur. Je maakt van deze waarden constanten. Het programma vraagt hoeveel
#kleine en grote flessen worden ingeleverd en berekent dan hoeveel de gebruiker zal
#ontvangen. Je werkt met floats en rondt het eindgetal af tot op 2 cijfers na de
#komma.
#Tip: Voor floating point getallen is het in de praktijk handig om de round() functie te
#gebruiken. De round() functie zorgt ervoor dat de ingevoerde getallen afgerond
#worden naar de door jouw gedefinieerde positie achter de komma. De functie vereist
#twee ingevulde parameters:  round(getal, aantal decimalen) . De standaard waarde
#voor een lege bijgevoegde waarde is een compleet afgerond getal. Dit houdt in dat
#wanneer de tweede parameter leeg blijft dan gaat de functie er van uit dat er
#afgerond dient te worden op hele getallen.
kleineflesjes = 0.12
groteflessen =  0.25
aantalgroot = input("hoeveel groote feesen bren je in")
prijsgroot = groteflessen * aantalgroot
aantalklien = input("hoeveel klijne flesen ben je in ")
prijsklein = kleineflesjes* aantalklien
totaal = prijsgroot + prijsklein
boodschap = f"je hebt {aantalklien}kleine en {aantalgroot}groote flesen da is {totaal}"
print(boodschap) 
