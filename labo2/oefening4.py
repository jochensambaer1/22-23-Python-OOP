#Schrijf een programma die het aantal zijden van een veelhoek opvraagt. Geef dan
#de naam van de veelhoek terug (bvb een zeshoek). Je programma ondersteunt
#vormen van 3 tot en met 10 zijden. Als de gebruiker een waarde invoert die buiten
#deze range valt dan reageer je met een gepaste melding
aantalzijden =input("geef een aantal vvor de zijden ")
match (aantalzijden): 
    case 3: print("het is een driehoek") 
    case 4: print("het is een vierkant ") 
    case 5: print(f"het is een pentagon ") 
    case 6: print(f"het is een heksagon ") 
    case 7: print(f"het is een heptagoon ") 
    case 8: print(f"het is een octagun") 
    case 9: print(f"het is een nonagoon ") 
    
    case 10: print(f"het is een decagoon") 
    case _: print(f"een veel hoek") 