#Oefening 7
#Een sublist is een list die deel is van een grotere list. Een sublist kan een list zijn die
#bestaat uit een enkel element, meerdere element of zelfs geen enkel element.
#Bijvoorbeeld: [1], [2], [3] en [4] zijn allen sublists van de list [1, 2, 3, 4]. De list [2, 3] is
#eveneens een sublist van [1, 2, 3, 4], maar [2, 4] is geen sublist van [1, 2, 3, 4]
#omdat elementen 2 en 4 niet aangrenzend zijn. Een lege list is een sublist van elke
#list. Dus [] is een sublist van [1, 2, 3, 4]. Een list is ook een sublist van zichzelf, dus
#[1, 2, 3, 4] is ook een sublist van [1, 2, 3, 4].
#Schrijf een functie is_sublist die twee lists (een kleinere en een grotere) als
#parameters aanneemt en bepaalt of de ene list een sublist is van de andere. De
#functie geeft True terug als de kleinere list een sublist is van de grotere. In je
#programma demonstreer je de werking van de functie.
def is_sublist(sublist, larger_list):
    if len(sublist) == 0:
        return True
    elif len(sublist) > len(larger_list):
        return False
    else:
        for i in range(len(larger_list) - len(sublist) + 1):
            if larger_list[i:i+len(sublist)] == sublist:
                return True
        return False

# Voorbeeld gebruik van de functie
print(is_sublist([], [1, 2, 3, 4]))  # True
print(is_sublist([1, 2], [1, 2, 3, 4]))  # True
print(is_sublist([2, 4], [1, 2, 3, 4]))  # False
print(is_sublist([1, 2, 3, 4], [1, 2, 3, 4]))  # True
print(is_sublist([1, 2, 3, 4], [1, 2, 3]))  # False
