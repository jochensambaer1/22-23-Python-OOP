#Oefening 3
#Op Unix gebaseerde besturingssystemen bevatten doorgaans ook een tool
#genaamd cat, een afkorting voor concatenate of samenvoegen. Het doel is om de
#aaneenschakeling van een of meer bestanden weer te geven waarvan de namen
#worden meegegeven als command-line argumenten. De bestanden worden
#weergegeven in dezelfde volgorde als waarin ze zijn meegegeven. Maak een
#Python-programma dat deze taak uitvoert. Je programma genereert ook een
#passende foutmelding voor elk bestand dat niet kan worden weergegeven en gaat
#vervolgens verder naar het volgende bestand. Geef een passend foutbericht weer
#als het programma wordt gestart zonder het command-line argument(en).
import sys

if len(sys.argv) < 2:
    print("Usage: python program_name.py file1 file2 ...")
    sys.exit(1)


for file_name in sys.argv[1:]:
    try:
        with open(file_name, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
