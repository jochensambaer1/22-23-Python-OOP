# Oefening 7: brood
# Beschrijf een klasse Brood (wit brood)
# Zorg voor een method eet_sneetjes waarbij je een integer met het aantal te eten
# sneetjes meegeeft
# Wat krijg je terug van deze method? Een dictionary (dict) waarin je enkele
# voedingsstatistieken (energie, eiwit, koolhydraten, suikers, vet) opslaat en
# uitrekent voor het aantal sneetjes dat werd gegeten
# Je vindt de nodige informatie
# hier: https://www.brood.net/gezondheid/voedingswaarde/
# Maak vervolgens 2 nieuwe klasses aan (via overerving): VolkorenBrood en
# ZuurdesemBrood
# Elke klasse gebruikt dezelfde eet_sneetjes method, maar met aangepaste
# voedingsinformatie
class Brood:
    def eet_sneetjes(self, aantal_sneetjes):
        voedingswaarde_per_sneetje = {
            'energie': 74,
            'eiwit': 2.6,
            'koolhydraten': 13.8,
            'suikers': 0.7,
            'vet': 0.7
        }
        voedingswaarde = {}
        for key in voedingswaarde_per_sneetje:
            voedingswaarde[key] = voedingswaarde_per_sneetje[key] * aantal_sneetjes
        return voedingswaarde
class VolkorenBrood(Brood):
    def eet_sneetjes(self, aantal_sneetjes):
        voedingswaarde_per_sneetje = {
            'energie': 83,
            'eiwit': 3.5,
            'koolhydraten': 13.5,
            'suikers': 1.2,
            'vet': 1.5
        }
        voedingswaarde = {}
        for key in voedingswaarde_per_sneetje:
            voedingswaarde[key] = voedingswaarde_per_sneetje[key] * aantal_sneetjes
        return voedingswaarde

class ZuurdesemBrood(Brood):
    def eet_sneetjes(self, aantal_sneetjes):
        voedingswaarde_per_sneetje = {
            'energie': 78,
            'eiwit': 3.1,
            'koolhydraten': 15.0,
            'suikers': 0.9,
            'vet': 0.8
        }
        voedingswaarde = {}
        for key in voedingswaarde_per_sneetje:
            voedingswaarde[key] = voedingswaarde_per_sneetje[key] * aantal_sneetjes
        return voedingswaarde
