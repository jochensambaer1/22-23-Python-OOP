#De lengte van een maand varieert van 28 tot 31 dagen. Je schrijft een programma
#die de naam van een maand opvraagt als string. Je geeft een getal terug met het
#aantal dagen. Voor februari geeft je “28 of 29 dagen” terug.
maand=input("geef een maand in" )
match (maand ): 
    case "januari"|"maart"|"mei"|"juni"|"augustus"|"oktober"|"december": print("31") 
    case "februari": print("28 of 29 dagen ") 
    
    case "april"|"juni"|"september"|"november": print(f"30 ") 
    
    
    
    case _: print(f" is geen maand ") 