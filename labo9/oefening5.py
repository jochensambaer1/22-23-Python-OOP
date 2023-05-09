# Oefening 5: enveloppen
# Schrijf een klasse Envelop, met twee attributen: gewicht (een float, in gram) en
# is_verstuurd (een boolean, met False als default)
# Je maakt drie methods:
# verstuur, die is_verstuurd op True zet. Maar enkel indien de envelop
# voldoende gefrankeerd is
# frankeer, die portokosten als argument heeft
# portokosten_nodig, die meegeeft hoeveel portokosten de envelop nodig
# heeft. Je zorgt ervoor dat dit automatisch resulteert in gewicht van de
# enveloppe x 10. Deze method moet worden uitgevoerd voor de envelop kan
# gefrankeerd worden. Maak hiervoor een instance variabele aan.
# Schrijf een klasse GroteEnvelop die op dezelfde manier werkt als Envelop (!
# overerving). Enkel is de portokost hier 15 x het gewicht

class Envelop:
    def __init__(self, gewicht):
        self.gewicht = gewicht
        self.is_verstuurd = False
        self.portokosten = None
    
    def portokosten_nodig(self):
        self.portokosten = self.gewicht * 10
        
    def frankeer(self, betaald):
        if self.portokosten is None:
            self.portokosten_nodig()
        if betaald >= self.portokosten:
            return True
        else:
            return False
        
    def verstuur(self, betaald):
        if self.frankeer(betaald):
            self.is_verstuurd = True
            return True
        else:
            return False

class GroteEnvelop(Envelop):
    def portokosten_nodig(self):
        self.portokosten = self.gewicht * 15
