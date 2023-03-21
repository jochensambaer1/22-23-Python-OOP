#Oefening 8
#Gebruik makend van de definitie van een sublist uit de vorige oefening schrijf je een
#functie die een list teruggeeft met daarin alle mogelijke sublists van een list die aan
#de functie als argument wordt meegegeven. Bijvoorbeeld: de sublists van [1,2,3] zijn
#[], [1], [2], [3], [1, 2], [2, 3] en [1, 2, 3]. Merk op dat je functie altijd een list teruggeeft
#die minstens een lege list teruggeeft omdat een lege list een sublist is van elke list.
#Voeg een programma toe die de werking van de functie illustreert door de functie
#verschillende keren aan te roepen met verschillende lists.
def get_sublists(lst):
    sublists = [[]]
    for i in range(len(lst)):
        for j in range(i+1, len(lst)+1):
            sublists.append(lst[i:j])
    return sublists
lst1 = [1, 2, 3]
lst2 = ["a", "b", "c", "d"]
lst3 = []

print(get_sublists(lst1))  # [[], [1], [1, 2], [1, 2, 3], [2], [2, 3], [3]]
print(get_sublists(lst2))  # [[], ['a'], ['a', 'b'], ['a', 'b', 'c'], ['a', 'b', 'c', 'd'], ['b'], ['b', 'c'], ['b', 'c', 'd'], ['c'], ['c', 'd'], ['d']]
print(get_sublists(lst3))  # [[]]
