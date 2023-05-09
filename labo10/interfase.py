import json
import datetime
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
user = User.objects.get(id=1)
json_data = {'name': user.name}
user = User.objects.get(id=1)
serializer = UserSerializer(user)
json_data = serializer.data


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
        for show in [show1, show2, show3, show4, show5]:
            print(f"{show.movie_title} at {show.cinema_name} on {show.show_time}")
        # Prompt the user for input.
        show_title = input("Enter the title of the show you would like to attend: ")
        user_name = input("Enter your name: ")
        # Find the selected show and user.
        show = next((s for s in [show1, show2, show3, show4, show5] if s.movie_title == show_title), None)
        user = next((u for u in [user1, user2, user3, user4, user5] if u.name == user_name), None)
        if show and user:
            show.buy_ticket(user)
            print(f"Ticket purchased for {show.movie_title} at {show.cinema_name} on {show.show_time}.")
        else:
            print("Error: Invalid show or user.")
    elif choice == "2":
        # Display the available movies.
        print("Available movies:")
        for movie in [movie1, movie2, movie3, movie4, movie5]:
            print(movie.title)
        # Prompt the user for input.
        movie_title = input("Enter the title of the movie you would like to rate: ")
        user_name = input("Enter your name: ")
        # Find the selected movie and user.
        movie = next((m for m in [movie1, movie2, movie3, movie4, movie5] if m.title == movie_title), None)
        user = next((u for u in [user1, user2, user3, user4, user5] if u.name == user_name), None)
        if movie and user:
            if user.attended_shows:
                attended_show = max(user.attended_shows, key=lambda s: s.show_time)
                attended_show.add_rating(user, 1)
                review = Review(user, movie.title, 1, "")
                movie.reviews.append(review)
                print(f"Rating created for {movie.title}.")
            else:
                print("Error: User has not attended any shows.")
        else:
            print("Error: Invalid movie or user.")
    else:
        print("Error: Invalid choice.")

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        return json.JSONEncoder.default(self, obj)

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

with open("data.json", "w") as f:
    data = {
        "users": [user.__dict__ for user in [user1, user2, user3, user4, user5]],
        "movies": [movie.__dict__ for movie in [movie1, movie2, movie3, movie4, movie5]],
        "shows": [show.__dict__ for show in [show1, show2, show3, show4, show5]],
        "reviews": [review.__dict__ for review in [review1, review2, review3, review4, review5]],
    }
    json.dump(data, f, cls=CustomEncoder, indent=4)
