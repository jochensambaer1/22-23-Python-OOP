# Oefening 4
# Maak een programma dat regels uit een bestand leest, er regelnummers aan
# toevoegt en de genummerde regels vervolgens opslaat in een nieuw bestand. De
# naam van het input-bestand wordt gevraagd aan de gebruiker, evenals de naam van
# het nieuwe bestand dat je programma zal aanmaken. Elke regel in het outputbestand moet beginnen met het regelnummer, gevolgd door een dubbele punt en
# een spatie, gevolgd door de regel uit het input-bestand.

input_file_name = input("Enter the name of the input file: ")
output_file_name = input("Enter the name of the output file: ")

with open(input_file_name, 'r') as input_file, open(output_file_name, 'w') as output_file:
    line_num = 1
    for line in input_file:
        output_file.write(f"{line_num}: {line}")
        line_num += 1
