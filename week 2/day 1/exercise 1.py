#exs1
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Step 1: Create cat objects
cat1 = Cat("Whiskers", 3)
cat2 = Cat("Luna", 7)
cat3 = Cat("Oliver", 5)

# Step 2: Create a function to find the oldest cat
def find_oldest_cat(*cats):
    # Using the max() function with a 'key' to find the cat with the highest age
    return max(cats, key=lambda cat: cat.age)

# Step 3: Print the oldest cat's details
oldest_cat = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")

#exs2
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        jump_height = self.height * 2
        print(f"{self.name} jumps {jump_height} cm high!")

# Step 2 & 3: Instantiate and call methods
davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Teacup", 20)

for dog in [davids_dog, sarahs_dog]:
    print(f"Dog: {dog.name}, Height: {dog.height}cm")
    dog.bark()
    dog.jump()
    print("-" * 10)

# Step 4: Compare Dog Sizes
if davids_dog.height > sarahs_dog.height:
    print(f"The bigger dog is {davids_dog.name}.")
elif sarahs_dog.height > davids_dog.height:
    print(f"The bigger dog is {sarahs_dog.name}.")
else:
    print("Both dogs are the same height!")
    
    #exs3
    class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

stairway = Song([
    "There’s a lady who's sure", 
    "all that glitters is gold", 
    "and she’s buying a stairway to heaven"
])

stairway.sing_me_a_song()

#exs4
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
        self.grouped_animals = {}

    def add_animal(self, *new_animals): # Bonus: using *args
        for animal in new_animals:
            if animal not in self.animals:
                self.animals.append(animal)

    def get_animals(self):
        print(f"Animals in {self.name}: {', '.join(self.animals)}")

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"Goodbye {animal_sold}!")
        else:
            print(f"{animal_sold} is not in this zoo.")

    def sort_animals(self):
        self.animals.sort()
        self.grouped_animals = {}
        
        for animal in self.animals:
            first_letter = animal[0].upper()
            if first_letter not in self.grouped_animals:
                self.grouped_animals[first_letter] = [animal]
            else:
                self.grouped_animals[first_letter].append(animal)

    def get_groups(self):
        for letter, names in self.grouped_animals.items():
            print(f"{letter}: {names}")

# Testing the Zoo
ramat_gan_safari = Zoo("Ramat Gan Safari")
ramat_gan_safari.add_animal("Giraffe", "Bear", "Baboon", "Cougar", "Cat", "Zebra", "Lion")
ramat_gan_safari.get_animals()

ramat_gan_safari.sell_animal("Bear")
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()