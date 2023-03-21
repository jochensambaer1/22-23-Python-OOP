#Een pretpark baseert zijn toegangsprijs op de leeftijd van de bezoeker. Kinderen
#jonger dan 3 betalen niets. Tussen 3 en 12 jaar betalen kinderen 15eur. Mensen van
#65 of ouder betalen 20eur. Alle anderen betalen 30eur. Maak een programma dat
#alle leeftijden van een bepaalde groep mensen één voor één kan inlezen. Een
#blanco lijn als invoer markeert het einde. Het programma toont daarop de totaalprijs
#voor deze groep en gaat vergezeld van een toepasselijke boodschap: je vermeldt
#ook met hoeveel ze zijn en en de totaalprijs per categorie. Je toont de prijzen met 2
#cijfers na de komma.

def calculate_admission_price():
  total_price = 0
  num_people = 0
  price_3_12 = 0
  price_65_plus = 0
  price_others = 0

  age = input("Please enter the age of the person: ")
  while age != "":
    age = int(age)
    if age < 3:
      total_price += 0
    elif age >= 3 and age <= 12:
      total_price += 15
      price_3_12 += 15
    elif age >= 65:
      total_price += 20
      price_65_plus += 20
    else:
      total_price += 30
      price_others += 30
    num_people += 1
    age = input("Please enter the age of the person: ")
  
  print("The total admission price for the group is", round(total_price, 2), "euros.")
  print("The number of people in the group is", num_people, ".")
  print("The total price for 3-12 years old is", round(price_3_12, 2), "euros.")
  print("The total price for 65+ years old is", round(price_65_plus, 2), "euros.")
  print("The total price for the others is", round(price_others, 2), "euros.")
  
calculate_admission_price()