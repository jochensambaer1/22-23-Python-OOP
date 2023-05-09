#Oefening 2: boeken, kasten en schappen
#Schrijf een Boek klasse die je boeken laat aanmaken met een titel, auteur en
#prijs
#Python Programming - Labo 9 2
#Maak daarna een Kast klasse, waarin je één of meerdere boeken kan plaatsen
#met een voeg_boek_toe method
#Tenslotte voeg je een totale_prijs method toe die de totaalprijs van alle boeken in
#de kast zal teruggeven
#Schrijf een method bevat_boek, die een string als argument neemt en True of
#False teruggeeft, afhankelijk van of een boek met deze titel ergens in de kast
#aanwezig is
#Pas je Boek klasse aan met een attribuut dikte, waarin je opslaat hoe veel ruimte
#een boek inneemt
#Pas de klasse Kast aan met een attribuut ruimte
#Zorg ervoor dat als een boek wordt toegevoegd en de kast vol zit (dus totale
#diktes van de boeken de ruimte overschrijdt) dit niet meer lukt. De gebruiker
#wordt hiervan op de hoogte gebracht
#Pas het geheel nog aan zodat een Kast kan bestaan uit één of meer schappen
#(klasse Schap)
#Je voegt boeken dan toe aan een schap
#Introduceer ruimte op schapniveau zodat een schap kan vol zitten en je de
#ruimte van een kast bepaalt als de som van die van de schappen
class Book:
    def __init__(self, title, author, price, thickness):
        self.title = title
        self.author = author
        self.price = price
        self.thickness = thickness

class Shelf:
    def __init__(self, space):
        self.space = space
        self.books = []

    def add_book(self, book):
        if self.get_remaining_space() >= book.thickness:
            self.books.append(book)
            return True
        else:
            return False

    def get_total_price(self):
        return sum(book.price for book in self.books)

    def contains_book(self, title):
        for book in self.books:
            if book.title == title:
                return True
        return False

    def get_remaining_space(self):
        return self.space - sum(book.thickness for book in self.books)

class Cabinet:
    def __init__(self, space):
        self.space = space
        self.shelves = [Shelf(space)]

    def add_book(self, book):
        for shelf in self.shelves:
            if shelf.add_book(book):
                return True
        new_shelf = Shelf(self.space)
        if new_shelf.add_book(book):
            self.shelves.append(new_shelf)
            return True
        else:
            return False

    def get_total_price(self):
        return sum(shelf.get_total_price() for shelf in self.shelves)

    def contains_book(self, title):
        for shelf in self.shelves:
            if shelf.contains_book(title):
                return True
        return False

    def get_remaining_space(self):
        return self.space - sum(shelf.space for shelf in self.shelves)
