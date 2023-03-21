# Oefening 12
# Sommige van de namen die voorkomen in de lijsten werden zowel aan jongens als
# aan meisjes gegeven. Schrijf een programma dat voor een - door de gebruiker
# ingegeven - specifiek jaar aan meisjes én aan jongens werden gegeven. Je
# programma geeft een boodschap als je voor dat bepaald jaar geen namen hebt
# gevonden. Geef een gepaste foutmelding terug als je voor het aangevraagde jaar
# geen data hebt. Maak gebruik van de babynamen dataset uit oefening 11
def find_names(year):
    # Open het bestand met de namen voor jongens en meisjes voor het opgegeven jaar
    try:
        boys_file = open("names/yob{}.txt".format(year))
        girls_file = open("names/yob{}-f.txt".format(year))
    except IOError:
        print("Er is geen data gevonden voor het opgegeven jaar.")
        return

    # Lees de lijsten met namen voor jongens en meisjes in
    boys_names = set()
    girls_names = set()

    for line in boys_file:
        name, _, _ = line.split(",")
        boys_names.add(name)

    for line in girls_file:
        name, _, _ = line.split(",")
        girls_names.add(name)

    # Maak een lijst van namen die zowel voor jongens als meisjes voorkomen
    gender_neutral_names = list(boys_names.intersection(girls_names))

    # Toon de lijst aan de gebruiker
    if len(gender_neutral_names) == 0:
        print("Er zijn geen namen gevonden die aan zowel jongens als meisjes werden gegeven in het opgegeven jaar.")
    else:
        print("De volgende namen werden aan zowel jongens als meisjes gegeven in {}:".format(year))
        for name in gender_neutral_names:
            print(name)

    # Sluit de bestanden
    boys_file.close()
    girls_file.close()
