import datetime

class User:
    def __init__(self, name):
        self.name = name
        self.attended_shows = []
        self.has_rated = []

class Movie:
    def __init__(self, title):
        self.title = title
        self.reviews = []

class Show:
    def __init__(self, movie_title, cinema_name, show_time):
        self.movie_title = movie_title
        self.cinema_name = cinema_name
        self.show_time = show_time
        self.tickets_sold = 0
        self.attendees = []
        self.ratings = []

    def buy_ticket(self, user):
        self.tickets_sold += 1
        self.attendees.append(user)
        user.attended_shows.append(self)

    def add_rating(self, user, rating):
        if user in self.attendees and user not in self.has_rated:
            self.ratings.append((user, rating, datetime.datetime.now()))
            user.has_rated.append(self)
        else:
            print("Error: User has not attended this show or has already rated it.")

class Review:
    def __init__(self, user, movie_title, rating, text):
        self.user = user
        self.movie_title = movie_title
        self.rating = rating
        self.text = text

class Cinema:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.shows = []

# Create some users, movies, shows, reviews, and cinemas.
user1 = User("Alice")
user2 = User("Bob")
user3 = User("Charlie")
user4 = User("David")
user5 = User("Eve")

movie1 = Movie("The Matrix")
movie2 = Movie("Inception")
movie3 = Movie("Interstellar")
movie4 = Movie("The Dark Knight")
movie5 = Movie("Pulp Fiction")

cinema1 = Cinema("Cineplex", "123 Main St")
cinema2 = Cinema("AMC", "456 Elm St")
cinema3 = Cinema("Regal", "789 Oak St")

show1 = Show(movie1.title, cinema1.name, datetime.datetime(2023, 6, 5, 10, 30))
show2 = Show(movie2.title, cinema1.name, datetime.datetime(2023, 6, 5, 12, 30))
show3 = Show(movie3.title, cinema2.name, datetime.datetime(2023, 6, 5, 14, 30))
show4 = Show(movie4.title, cinema2.name, datetime.datetime(2023, 6, 5, 16, 30))
show5 = Show(movie5.title, cinema3.name, datetime.datetime(2023, 6, 5, 18, 30))

review1 = Review(user1, movie1.title, 1, "Terrible movie!")
review2 = Review(user2, movie2.title, 1, "Waste of time.")
review3 = Review(user3, movie3.title, 1, "Boring.")
review4 = Review(user4, movie4.title, 1, "Overrated.")
review5 = Review(user5, movie5.title, 1, "Not my cup of tea.")
import json
