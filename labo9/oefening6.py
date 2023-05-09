# Oefening 6: mobiele toestellen
# Maak een klasse MobielToestel aan die een mobiel telefoontoestel
# vertegenwoordigt
# Zorg voor een kies_nummer method die een nummer voor je oproept. Als
# resultaat wordt een gepaste string teruggegeven in hoofdletters.
# Maak een subklasse SmartPhone die de method van de base klasse gebruikt
# maar een eigen method open_app heeft
# Maak een subklasse iPhone aan die zijn eigen open_app method heeft, maar
# ook een eigen kies_nummer method die de kies_nummer method van de base
# Python Programming - Labo 9 4
# klasse oproept, maar een de string teruggeeft in lowercase
class MobielToestel:
    def kies_nummer(self, nummer):
        return nummer.upper()

class SmartPhone(MobielToestel):
    def open_app(self, app):
        print("Opening", app)

class iPhone(SmartPhone):
    def kies_nummer(self, nummer):
        return nummer.lower()
