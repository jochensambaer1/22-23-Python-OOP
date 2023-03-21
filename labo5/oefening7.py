# Oefening 7
# Maak een programma dat alle door de gebruiker ingevoerde getallen bij elkaar
# optelt. Het negeert daarbij alle invoer die niet uit een geldig getal bestaat (bvb een
# woord). Je programma geeft de som weer nadat elk nummer is ingevoerd. Het geeft
# een passend bericht weer telkens de gebruiker iets anders dan een getal heeft
# ingevoerd. Verlaat het programma wanneer de gebruiker een lege regel invoert.
# Zorg ervoor dat je programma correct werkt voor zowel integers als floats.
total = 0

while True:
    user_input = input("Voer een getal in: ")
    if user_input == "":
        break
    try:
        num = float(user_input)
        total += num
        print(f"Huidige som: {total}")
    except ValueError:
        print("Ongeldige invoer. Voer een geldig getal in.")
        
print(f"Eindtotaal: {total}")
