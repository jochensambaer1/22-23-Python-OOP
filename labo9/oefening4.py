#Oefening 4: transacties
#Python Programming - Labo 9 3
#Maak een klasse Transactie, waarbij elke object instance een storting of een
#opname van een bankrekening vertegenwoordigt
#Wanneer je een Transactie-instance creëert geef je een positief getal voor een
#storting en een negatief getal voor een opname
#Maak een klasse attribuut balans aan om de balans in de gaten te houden van
#alle transacties
#De balans zou op elk moment de som van stortingen en opnames moeten
#bevatten
class Transactie:
    balans = 0  # class attribute to keep track of balance

    def __init__(self, bedrag):
        self.bedrag = bedrag  # instance attribute for transaction amount
        Transactie.balans += bedrag  # update the balance with the transaction amount

    def __str__(self):
        if self.bedrag > 0:
            return f"Storting van {self.bedrag} EUR"
        else:
            return f"Opname van {-self.bedrag} EUR"
