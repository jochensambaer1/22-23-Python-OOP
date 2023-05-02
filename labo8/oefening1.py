#Oefening 1: Bolletjes ijs
    #In deze oefening maak je een klasse aan en noemt ze Bolletje. Bolletje vertegenwoordigt één enkel bolletje ijs
    #Elke bol heeft één enkel attribuut, smaak, een string die je kan initialiseren
    #wanneer je een instance van Bolletje initialiseert
    #Als je de klasse hebt gemaakt schrijf je een functie - maak_bolletjes - die drie
    #instances van de Bolletje klasse aanmaakt. Elk met een verschillende smaak
    #Deze drie instances stop je - binnen de functie - in een lijst met als naam
    #bolletjes
    #Vervolgens loop je - binnen de functie - door deze lijst en print je de smaak van
    #elke bol ijs die je hebt gemaakt af
    #Tot slot roep je deze functie aan

class IceCream:
    def __init__(self, flavour):
        self.flavour = flavour

def make_ice_creams():
    ice_creams = [IceCream("chocolate"), IceCream("vanilla"), IceCream("strawberry")]
    for ice_cream in ice_creams:
        print(ice_cream.flavour)

make_ice_creams()