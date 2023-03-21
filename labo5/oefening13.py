# Oefening 13
# Python Programming - Labo 5 5
# Gebruik de dataset uit oefeningen 11 en 12. Schrijf een programma waarin de
# gebruiker twee jaartallen kan ingeven. Analyseer voor deze tijdspanne (bvb van
# 2002 tot en met 2007) de data en geef de populairste jongens- en meisjesnaam
# terug voor de volledige periode.
# Vraag om de namen van de bestanden met babynamen
boys_filename = input("Geef de naam van het bestand met jongensnamen: ")
girls_filename = input("Geef de naam van het bestand met meisjesnamen: ")

# Vraag om de tijdspanne om te analyseren
start_year = int(input("Geef het startjaar: "))
end_year = int(input("Geef het eindjaar: "))

# Maak twee dictionaries om de namen en hun tellingen bij te houden
boy_names = {}
girl_names = {}

# Loop over elk jaar in de opgegeven tijdspanne
for year in range(start_year, end_year + 1):
    # Open het bestand voor jongensnamen
    with open(boys_filename.format(year), 'r') as boys_file:
        # Loop over de eerste 10 namen in het bestand en hun tellingen
        for i in range(10):
            line = boys_file.readline()
            name, count = line.strip().split(',')
            if name not in boy_names:
                boy_names[name] = 0
            boy_names[name] += int(count)

    # Open het bestand voor meisjesnamen
    with open(girls_filename.format(year), 'r') as girls_file:
        # Loop over de eerste 10 namen in het bestand en hun tellingen
        for i in range(10):
            line = girls_file.readline()
            name, count = line.strip().split(',')
            if name not in girl_names:
                girl_names[name] = 0
            girl_names[name] += int(count)

# Zoek de meest voorkomende naam in elke dictionary
most_popular_boy_name = max(boy_names, key=boy_names.get)
most_popular_girl_name = max(girl_names, key=girl_names.get)

# Geef de resultaten weer
print("De meest populaire jongensnaam tussen {} en {} is {}".format(start_year, end_year, most_popular_boy_name))
print("De meest populaire meisjesnaam tussen {} en {} is {}".format(start_year, end_year, most_popular_girl_name))
