# Oefening 11
# De babynamen-set bevat meer dan 200 bestanden. Elk bestand bevat een lijst met
# 100 namen, alsook het aantal keer dat de naam voor komt voor elk jaar. De lijnen in
# de bestanden zijn gerangschikt van meest naar minst vaak gebruikt. Er zijn twee
# bestanden voor elk jaar: een met namen voor meisjes en de andere met namen voor
# jongens. De dataset bevat gegevens voor elk jaar van 1900 tot 2012. Schrijf een
# programma dat elk bestand in de dataset leest en alle namen identificeert die het
# meest populair waren in ten minste één jaar. Je programma dient twee lijsten weer
# te geven: een met de meest populaire namen voor jongens en de andere met de
# meest populaire namen voor meisjes. Geen van de lijsten mag tweemaal dezelfde
# waarde bevatten.
import os

popular_boys_names = []
popular_girls_names = []

# Stap 2
directory = "babynames"
files = os.listdir(directory)

for file in files:
    # Stap 3
    with open(os.path.join(directory, file), "r") as f:
        # Stap 4
        boys_names = []
        girls_names = []
        for line in f:
            # Stap 5
            name, count = line.strip().split(",")
            count = int(count)
            if name in boys_names:
                if count > boys_names.count(name):
                    boys_names.remove(name)
                    boys_names.append(name)
            elif len(boys_names) < 10:
                boys_names.append(name)
            
            if name in girls_names:
                if count > girls_names.count(name):
                    girls_names.remove(name)
                    girls_names.append(name)
            elif len(girls_names) < 10:
                girls_names.append(name)

        # Stap 6
        popular_boys_names.extend(boys_names)
        popular_girls_names.extend(girls_names)

# Stap 7
print("Most popular boys' names:")
print(list(set(popular_boys_names)))

print("Most popular girls' names:")
print(list(set(popular_girls_names)))
