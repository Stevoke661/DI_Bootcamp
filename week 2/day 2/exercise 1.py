#exs1
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# Step 1: Create the Siamese class
class Siamese(Cat):
    pass

# Step 2: Create a list of cat instances
all_cats = [
    Bengal("Tiger", 3),
    Chartreux("Felix", 5),
    Siamese("Cloud", 2)
]

# Step 3: Create a Pets instance
sara_pets = Pets(all_cats)

# Step 4: Take cats for a walk
sara_pets.walk()

#exs2
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        # Formula: weight / age * 10
        return self.weight / self.age * 10

    def fight(self, other_dog):
        my_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight
        
        if my_power > other_power:
            return f"{self.name} won the fight!"
        elif other_power > my_power:
            return f"{other_dog.name} won the fight!"
        else:
            return "It's a draw!"

# Step 2 & 3: Create instances and test
dog1 = Dog("Rex", 5, 20)
dog2 = Dog("Bolt", 3, 15)
dog3 = Dog("Tank", 7, 40)

print(dog1.bark())
print(f"{dog2.name}'s speed: {dog2.run_speed()}")
print(dog3.fight(dog1))

#exs3
import random
# Assuming Dog class is in the same file or imported
# from dog_file import Dog

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *dog_names):
        # *dog_names collects all arguments into a tuple
        names_str = ", ".join(dog_names)
        print(f"{self.name}, {names_str} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                "does a barrel roll", 
                "stands on his back legs", 
                "shakes your hand", 
                "plays dead"
            ]
            print(f"{self.name} {random.choice(tricks)}")
        else:
            print(f"{self.name} is not trained yet!")

# Testing
my_pet = PetDog("Buddy", 4, 12)
my_pet.train()
my_pet.play("Rex", "Max", "Lucifer")
my_pet.do_a_trick()

#exs4
class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""

    def is_18(self):
        return self.age >= 18

class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        new_person = Person(first_name, age)
        new_person.last_name = self.last_name
        self.members.append(new_person)
        print(f"Congratulations! {first_name} {self.last_name} was born.")

    def check_majority(self, first_name):
        for person in self.members:
            if person.first_name == first_name:
                if person.is_18():
                    print(f"You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print(f"Sorry, {first_name}, you are not allowed to go out with your friends.")
                return
        print("Member not found.")

    def family_presentation(self):
        print(f"\nFamily: {self.last_name}")
        for member in self.members:
            print(f"Name: {member.first_name}, Age: {member.age}")

# Testing the Family class
my_family = Family("Smith")
my_family.born("Alice", 25)
my_family.born("Bob", 12)

my_family.family_presentation()
my_family.check_majority("Alice")
my_family.check_majority("Bob")