#Oefening 1
#Op Unix gebaseerde besturingssystemen bevatten een tool met de naam head. Het
#toont de eerste 10 regels van een bestand waarvan de naam is opgegeven als een
#command-line argument. Schrijf een Python-programma met hetzelfde gedrag. Geef
#een passend foutbericht weer als het door de gebruiker gevraagde bestand niet
#bestaat, of als het command-line
#argument wordt weggelaten.
import sys

if len(sys.argv) != 2:
    print("Usage: python program_name.py file_name")
    quit()

file_name = sys.argv[1]

try:
    with open(file_name, 'r') as file:
        for i in range(10):
            line = file.readline()
            if not line:
                break
            print(line, end='')
except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
    sys.exit(1)
