#Op Unix gebaseerde besturingssystemen bevatten doorgaans ook een tool met de
#naam tail. Het toont de laatste 10 regels van een bestand waarvan de naam is
#opgegeven als een command-line argument. Schrijf een Python-programma met
#hetzelfde gedrag. Geef een passend foutbericht weer als het door de gebruiker
#gevraagde bestand niet bestaat of als het command-line argument wordt
#weggelaten. Er zijn verschillende benaderingen die kunnen worden gevolgd om dit
#probleem op te lossen.
#Een optie is om de volledige inhoud van het bestand in een lijst te laden en
#vervolgens de laatste 10 elementen weer te geven. Een andere optie is om de
#inhoud van het bestand twee keer te lezen, een keer om de regels te tellen en een
#tweede keer om de laatste 10 regels weer te geven. Beide oplossingen zijn echter
#ongewenst bij het werken met grote bestanden. Er bestaat een andere oplossing
#Python Programming - Labo 5 2
#waarbij u het bestand slechts één keer hoeft te lezen en slechts 10 regels uit het
#bestand tegelijk hoeft op te slaan. Voor een extra uitdaging, ontwikkel een dergelijke
#oplossing.






import sys

if len(sys.argv) < 2:
    print("Usage: python program_name.py file_name")
    sys.exit(1)

file_name = sys.argv[1]

try:
    with open(file_name, 'r') as file:
        lines = file.readlines()
        last_lines = lines[-10:]
        for line in last_lines:
            print(line, end='')
except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
    sys.exit(1)
