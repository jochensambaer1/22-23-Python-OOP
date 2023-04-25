#Oefening 4: reuzehoorntje
    #Je werkt verder op de vorige oefening en gebruikt overerving om een nieuwe
    #klasse Reuzehoorntje aan te maken
    #Het enige verschil met hoorntje: dit hoorntje kan tot 5 bolletjes ijs aan
    #Eventuele minimale aanpassingen in Bolletje() en of Hoorntje() zijn toegelaten
    
class Bolletje:
    def __init__(self, smaak):
        self.smaak = smaak

class Hoorntje:
    def __init__(self):
        self.bolletjes = []

    def voeg_toe(self, bolletje):
        if len(self.bolletjes) < 3:
            self.bolletjes.append(bolletje)
        else:
            print("Dit hoorntje kan maximaal 3 bolletjes bevatten!")

class Reuzehoorntje(Hoorntje):
    def __init__(self):
        super().__init__()
    
    def voeg_toe(self, bolletje):
        if len(self.bolletjes) < 5:
            self.bolletjes.append(bolletje)
        else:
            print("Dit reuzehoorntje kan maximaal 5 bolletjes bevatten!")
