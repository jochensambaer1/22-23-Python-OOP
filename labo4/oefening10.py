#Oefening 10
#In deze oefening simuleer je 1000 worpen van twee dobbelstenen. Je schrijft een
#functie die geen parameters aanneemt en de worp van twee dobbelstenen simuleert.
#Deze functie geeft het totaal van de worpen terug. Schrijf een programma dat deze
#functie 1000 keer uitvoert. Het programma telt het aantal keer dat een bepaalde
#waarde voorkomt. Je gebruikt een dictionary om de data bij te houden. Na afloop
#toont het programma een tabel die de data samenvat op de volgende manier:
#Totaal Gesimuleerd Percentage Verwacht Percentage
#2 2.90 2.78
#3 6.90 5.56
#4 9.40 8.33
#5 11.90 11.11
#6 14.20 13.89
#7 14.20 16.67
#8 15.00 13.89
#9 10.50 11.11
#10 7.90 8.33
#11 4.50 5.56
#12 2.60 2.78
import random

def dobbelsteen_worp():
    return random.randint(1, 6) + random.randint(1, 6)

frequentie = {}
for i in range(1000):
    worp = dobbelsteen_worp()
    if worp in frequentie:
        frequentie[worp] += 1
    else:
        frequentie[worp] = 1

totaal_gesimuleerd = sum(frequentie.values())

verwacht_percentages = [0] * 11
for i in range(2, 13):
    verwacht_percentages[i-2] = (i == 7 and 6 or abs(7-i)) / 36 * 100

print("Totaal\tGesimuleerd\tPercentage\tVerwacht Percentage")
for i in range(2, 13):
    gesimuleerd = frequentie.get(i, 0)
    percentage = gesimuleerd / totaal_gesimuleerd * 100
    verwacht_percentage = verwacht_percentages[i-2]
    print(f"{i}\t{gesimuleerd}\t\t{percentage:.2f}\t\t{verwacht_percentage:.2f}")
