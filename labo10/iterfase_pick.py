import json
import datetime
import pickle

with open("user1.pickle", "wb") as f:
    pickle.dump(user1, f)
with open("user1.pickle", "rb") as f:
    user1_unpickled = pickle.load(f)    
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
        if user in self.attendees and self.movie_title not in user.has_rated:
            self.ratings.append((user, rating, datetime.datetime.now()))
            user.has_rated.append(self.movie_title)
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

# Define objects
user1 = User("Alice")
user2 = User("Bob")
movie1 = Movie("The Matrix")
movie2 = Movie("Inception")
cinema1 = Cinema("Cinema City", "New York")
show1 = Show("The Matrix", "Cinema City", datetime.datetime(2023, 6, 5, 15, 30))
show2 = Show("Inception", "Cinema City", datetime.datetime(2023, 6, 5, 18, 0))

def main():
    # Prompt the user for input.
    print("Welcome to the movie rating app!")
    print("What would you like to do?")
    print("1. Buy a ticket for a show")
    print("2. Create a rating for a movie")
    choice = input("Enter your choice (1 or 2): ")

    # Handle the user's choice.
    if choice == "1":
        # Display the available shows.
        print("Available shows:")
        for show in sorted([show1, show2], key=lambda s: s.show_time):
            print(f"{show.movie_title} at {show.cinema_name} on {show.show_time}")
        # Prompt the user for input.
        show_title = input("Enter the title of the show you would like to attend: ")
        user_name = input("Enter your name: ")
        # Find the selected show and user.
        show = next((s for s in [show1, show2] if s.movie_title == show_title), None)
        user = next((u for u in [user1, user2] if u.name == user_name), None)
        if show and user:
            show.buy_ticket(user)
            print(f"Ticket purchased for {show.movie_title} at {show.cinema_name} on {show.show_time}.")
        else:
            print("Error: Invalid show or user.")
    elif choice == "2":
        # Display the available movies.
        print("Available movies:")
        for movie in [movie1, movie2]:
            print(movie.title)
        # Prompt the user for input.
        movie_title = input("Enter the title of the movie you would like to rate: ")
        user_name = input("Enter your name: ")
        
        # Find the selected movie and user.
        movie = next((s for s in [movie1, movie2] if s.movie_title == movie_title), None)
        user = next((u for u in [user1, user2] if u.name == user_name), None)
        if movie and user:
            movie.buy_ticket(user)
            print(f"Ticket purchased for {movie.movie_title} at {movie.cinema_name} on {movie.show_time}.")
        else:
            print("Error: Invalid movie or user.")