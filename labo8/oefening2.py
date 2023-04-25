#Oefening 2: bolletjes ijs op een hoorntje
    #We herbruiken onze klasse Bolletje, die één bol ijs vertegenwoordigt en maken
    #een nieuwe klasse: Hoorntje, waarin we de bollen kunnen onderbrengen. We
    #zullen dit doen met object compositie
    #Maak in Hoorntje een attribuut bolletjes aan, met een lege list
    #Maak in Hoorntje een method bolletjes_toevoegen waarmee je - tegelijk - één of
    #meerdere instances van Bolletje kan toevoegen aan Hoorntje (dus geen string
    #met de smaak ;-))
    #Dat betekent gebruik van de splat operator (nieuwe_bolletjes) ⇒ zie
    #theorieles dictionaries, laatste slides
    #Python programming - Labo 8 2
    #We kunnen dan itereren (in een for loop) over elk element van
    #*nieuwe_bolletjes en het telkens met list.append toevoegen aan
    #self.bolletjes.
    #Tot slot print je de smaken af en je definieert hiervoor de __str__ method met
    #daarin gebruik van een for loop door de smaken met str.join (we gaan dieper in
    #op deze “magic method” in de theorieles later deze week). Voorbeeld:
    #https://www.delftstack.com/howto/python/__str__-vs-__repr__-in-python/
 
class Bolletje:
    def __init__(self, smaak):
        self.smaak = smaak

    def __str__(self):
        return self.smaak

class Hoorntje:
    def __init__(self):
        self.bolletjes = []

    def bolletjes_toevoegen(self, *nieuwe_bolletjes):
        for bol in nieuwe_bolletjes:
            self.bolletjes.append(bol)

    def __str__(self):
        smaken = [str(bol) for bol in self.bolletjes]
        return " en ".join(smaken) + " op een hoorntje"
