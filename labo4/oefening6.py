#Oefening 6
#Om de hoofdprijs in een bepaalde loterij te winnen, moet men alle 6 nummers op
#een loterijbriefje matchen met de 6 nummers tussen 1 en 49 die zijn getrokken door
#de organisator van de loterij. Schrijf een programma dat een willekeurige selectie
#van 6 nummers genereert voor een loterijbriefje. Zorg ervoor dat de 6 geselecteerde
#nummers geen dubbele nummers bevatten.
#Geef de nummers in oplopende volgorde weer.
lottery_numbers = random.sample(range(1, 50), 6)
lottery_numbers.sort()

print("De winnende loterijnummers zijn:")
for num in lottery_numbers:
    print(num)