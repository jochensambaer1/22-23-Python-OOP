#Oefening 12
#We noemen twee woorden anagrammen als ze dezelfde letters bevatten, maar in
#een verschillende volgorde. Schrijf een programma dat twee strings van een
#gebruiker inleest en bepaalt en teruggeeft of beide strings anagrammen zijn. Gebruik
#een dictionary om dit probleem op te lossen.
def is_anagram(word1, word2):
    """Controleert of twee woorden anagrammen zijn."""
    # Verwijder spaties en zet alle letters in kleine letters om
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()
    
    # Controleer of de woorden even lang zijn
    if len(word1) != len(word2):
        return False
    
    # Maak dictionaries van de letters in de woorden
    dict1 = {}
    dict2 = {}
    for letter in word1:
        dict1[letter] = dict1.get(letter, 0) + 1
    for letter in word2:
        dict2[letter] = dict2.get(letter, 0) + 1
    
    # Controleer of de dictionaries gelijk zijn
    if dict1 == dict2:
        return True
    else:
        return False

# Voorbeeldgebruik:
woord1 = input("Geef het eerste woord: ")
woord2 = input("Geef het tweede woord: ")
if is_anagram(woord1, woord2):
    print("De woorden zijn anagrammen van elkaar.")
else:
    print("De woorden zijn geen anagrammen van elkaar.")
