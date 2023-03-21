# Oefening 5
# Als we een lijst met elementen in een tekst weergeven scheiden we de elementen
# doorgaans met een komma. Voor het laatste element komt dan een “en”.
# rozen
# rozen en kranten
# rozen, kranten en ketels
# functie geeft een string terug die alle alle elementen van de list geformatteerd
# teruggeeft op de manier die je hierboven ziet. Je test de functie in je programma uit
# met lists van verschillende lengtes.
def format_list(items):
    if len(items) == 0:
        return ""
    elif len(items) == 1:

        return items[0]
    elif len(items) == 2:
        return f"{items[0]} en {items[1]}"
    else:
        formatted = ", ".join(items[:-1])
        return f"{formatted} en {items[-1]}"

print(format_list([])) # ""
print(format_list(["rozen"])) # "rozen"
print(format_list(["rozen", "kranten"])) # "rozen en kranten"
print(format_list(["rozen", "kranten", "ketels"])) # "rozen, kranten en ketels"
print(format_list(["a", "b", "c", "d", "e"])) # "a, b, c, d en e"