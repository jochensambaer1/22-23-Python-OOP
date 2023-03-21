# Schrijf een programma dat de gebruiker naar zijn of haar naam vraagt. Daarna
# vraagt het programma naar de interesses van de gebruiker. Het programma
# antwoordt vervolgens met een hallo-boodschap waarin de gevraagde gegevens
# verwerkt zitten.
familienaam = input("Naam ? ")
voornaam = input("voorNaam ? ")
interesses = input("wat is je interesses? ")
volledige_naam = f"{voornaam} {familienaam}"
boodschap = f"hallo , {volledige_naam.title()}! met een interesen in  {interesses}"
print(boodschap)
