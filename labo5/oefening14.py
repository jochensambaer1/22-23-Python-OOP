# Oefening 14
# Gebruik de dataset uit oefeningen 11, 12 en 13. Schrijf een programma dat elk
# bestand in de dataset uitleest. Terwijl je programma de bestanden uitleest houdt het
# elke verschillende naam die voorkomt bij (doe dit voor jongens en voor meisjes
# afzonderlijk). Na afloop rapporteert je programma beide naamlijsten. Deze lijsten
# bevatten geen dubbele namen.
boys_names = set()
girls_names = set()

for year in range(1900, 2013):
    with open(f"yob{year}.txt") as file:
        for line in file:
            name, gender, count = line.split(",")
            if gender == "M":
                boys_names.add(name)
            else:
                girls_names.add(name)

print("Populaire jongensnamen:")
for name in boys_names:
    print(name)

print("\nPopulaire meisjesnamen:")
for name in girls_names:
    print(name)
