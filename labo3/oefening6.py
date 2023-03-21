#Oefening 6
#Maak een functie die een string als enige parameter heeft en een nieuwe string
#teruggeeft die de oorspronkelijke correct van hoofdletters heeft voorzien. Je functie
#maakt een hoofdletter van de eerste letter in de string (eventuele witruimte niet
#meegerekend). Je gaat daarnaast van de eerste letter na een punt, uitroepteken of
#vraagteken ook een hoofdletter maken. Schrijf een programma dat de functie een
#aantal keer demonstreert.
def capitalize_string(string):
  # Maak een lijst van leestekens waarop je wilt splitsen
  punctuation = [".", "!", "?"]
  # Maak een lege lijst om de stukken van de string op te slaan
  pieces = []
  # Houd bij waar het vorige leesteken was
  prev = 0
  # Loop door elke karakter in de string
  for i in range(len(string)):
    # Als het karakter een leesteken is
    if string[i] in punctuation:
      # Voeg het stuk tussen het vorige en het huidige leesteken toe aan de lijst
      pieces.append(string[prev:i+1])
      # Update het vorige leesteken naar het huidige
      prev = i+1
  # Voeg het laatste stuk toe aan de lijst als er nog iets over is
  if prev < len(string):
    pieces.append(string[prev:])
  # Maak een nieuwe string door elk stuk te kapitaliseren en samen te voegen met spaties
  new_string = " ".join(piece.strip().capitalize() for piece in pieces)
  # Geef de nieuwe string terug
  return new_string

# Schrijf een programma dat de functie demonstreert

# Vraag de gebruiker om een string in te voeren
string = input("Voer een string in: ")

# Roep de functie aan met de ingevoerde string als argument
new_string = capitalize_string(string)

# Print de nieuwe string uit
print("De nieuwe string is:", new_string)