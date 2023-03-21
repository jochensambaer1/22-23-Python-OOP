# Oefening 2
# Schrijf een functie die een list en een niet-negatief geheel getal n als parameters
# aanneemt. De functie geeft een nieuwe kopie van de list terug met de n-aantal
# grootste en kleinste elementen uit de oorspronkelijke list weggefilterd. De
# oorspronkelijke volgorde van de elementen in de list moet niet worden behouden.
# Schrijf een programma dat de werking van de functie demonstreert. Je functie geeft
# een “foutmelding” terug als het aantal elementen in de lijst niet voldoende blijkt om
# het aantal grootste en kleinste elementen te doen verdwijnen. Zo bevat een lijst van
# 4 elementen onvoldoende elementen om de grootste en kleinste 2 elementen te
# doen verdwijnen. Er moet minstens 1 kunnen overblijven
def filter_list(lst, n):
    # kopieer de lijst om de oorspronkelijke lijst niet te wijzigen
    lst_copy = lst.copy()
    # controleer of de lijst lang genoeg is
    if len(lst_copy) > 2 * n:
        # initialiseer een teller
        count = 0
        # verwijder de grootste en kleinste elementen tot de teller n bereikt
        while count < n:
            lst_copy.remove(max(lst_copy))
            lst_copy.remove(min(lst_copy))
            count += 1
        # geef de gefilterde lijst terug
        return lst_copy
    else:
        # geef een foutmelding terug
        return "Fout: de lijst bevat onvoldoende elementen om te filteren."
