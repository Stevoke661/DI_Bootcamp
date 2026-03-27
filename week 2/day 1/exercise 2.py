#exs1.py
import math

class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def get_area(self):
        return math.pi * (self.radius ** 2)

    def definition(self):
        print("A circle is the set of all points in a plane that are at a given distance from a given point, the center.")

# Example usage:
my_circle = Circle(5)
print(f"Area: {my_circle.get_area():.2f}")
my_circle.definition()

#exs2.py
import random

class MyList:
    def __init__(self, letters):
        self.letters = letters

    def get_reversed(self):
        return self.letters[::-1]

    def get_sorted(self):
        return sorted(self.letters)

    def generate_random_list(self):
        # List comprehension to generate random numbers between 1 and 100
        return [random.randint(1, 100) for _ in range(len(self.letters))]

# Example usage:
my_list_obj = MyList(['d', 'a', 'c', 'b'])
print(f"Reversed: {my_list_obj.get_reversed()}")
print(f"Random List: {my_list_obj.generate_random_list()}")

#exs3.py
class MenuManager:
    def __init__(self):
        # Initializing with the provided dishes
        self.menu = [
            {"name": "Soup", "price": 10, "spice": "B", "gluten": False},
            {"name": "Hamburger", "price": 15, "spice": "A", "gluten": True},
            {"name": "Salad", "price": 18, "spice": "A", "gluten": False},
            {"name": "French Fries", "price": 5, "spice": "C", "gluten": False},
            {"name": "Beef bourguignon", "price": 25, "spice": "B", "gluten": True}
        ]

    def add_item(self, name, price, spice, gluten):
        new_dish = {
            "name": name,
            "price": price,
            "spice": spice,
            "gluten": gluten
        }
        self.menu.append(new_dish)
        print(f"Added {name} to the menu.")

    def update_item(self, name, price, spice, gluten):
        for dish in self.menu:
            if dish["name"] == name:
                dish.update({"price": price, "spice": spice, "gluten": gluten})
                print(f"Updated {name} successfully.")
                return
        print(f"Error: {name} was not found in the menu.")

    def remove_item(self, name):
        for i, dish in enumerate(self.menu):
            if dish["name"] == name:
                del self.menu[i]
                print(f"Removed {name}. Updated menu:")
                for item in self.menu:
                    print(item)
                return
        print(f"Error: {name} is not in the menu.")

# Testing the Manager
manager = MenuManager()
manager.add_item("Taco", 12, "C", False)
manager.update_item("Salad", 20, "A", False)
manager.remove_item("French Fries")