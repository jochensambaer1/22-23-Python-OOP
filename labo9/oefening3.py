#Oefening 3: personen in een populatie
#Maak een klasse Persoon aan
#Voorzie ze van een klasse attribuut populatie die toeneemt elke keer je een
#nieuwe persoon instantieert
#Maak 5 personen aan en check dan of populatie op 5 staat
#Gebruik de __del__ method om de populatie met eentje te laten afnemen
#wanneer een instance van Persoon wordt verwijderd
#Zoek op en test uit hoe je een object instance kunt verwijderen
#Zoek op en ga na wat garbage collection is in Python en hoe het
#werkt: http://mng.bz/nP2a
class Person:
    population = 0  # class attribute

    def __init__(self):
        Person.population += 1  # increase population count
        print("A new person has been added to the population.")
    
    def __del__(self):
        Person.population -= 1  # decrease population count
        print("A person has been removed from the population.")
        
# create 5 persons
for i in range(5):
    p = Person()

# check population count
print(f"Population count: {Person.population}")

# delete an instance of Person
p1 = Person()
del p1

# check population count after deleting an instance of Person
print(f"Population count: {Person.population}")
