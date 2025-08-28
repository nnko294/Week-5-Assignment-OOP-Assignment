# Assignment 1: Design Your Own Class

class Movie:
    def __init__(self, title, genre, release_year, rating):
        self.title = title
        self.genre = genre
        self.release_year = release_year
        self.rating = rating

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Genre: {self.genre}")
        print(f"Release Year: {self.release_year}")
        print(f"Rating: {self.rating}/10")

    def update_rating(self, new_rating):
        self.rating = new_rating
        print(f"Updated rating for {self.title}: {self.rating}/10")

class Blockbuster(Movie):
    def __init__(self, title, genre, release_year, rating, box_office):
        super().__init__(title, genre, release_year, rating)
        self.box_office = box_office

    def display_box_office(self):
        print(f"Box Office: {self.box_office}")

# Create a movie object
avengers = Blockbuster("Avengers: Endgame", "Action", 2019, 9.5, "2.79 billion")
avengers.display_details()
avengers.display_box_office()
avengers.update_rating(9.8)


# Activity 2: Polymorphism Challenge
# Let's create a program with animals that have a move() method:
class Animal:
    def move(self):
        pass

class Dog(Animal):
    def move(self):
        print("Running")

class Bird(Animal):
    def move(self):
        print("Flying")

class Fish(Animal):
    def move(self):
        print("Swimming")

# Create a list of animals
animals = [Dog(), Bird(), Fish()]

# Make each animal move
for animal in animals:
    animal.move()