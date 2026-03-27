#exs1
import re
import json

def validate_valentine_item(name, price):
    # Rule: Starts with V, no numbers, at least two 'e's
    # This is easier to split: check "no numbers" and "two e's" separately from the pattern
    if len(re.findall(r'e', name, re.IGNORECASE)) < 2 or re.search(r'\d', name):
        return False
    
    # Pattern: Starts with V, Title Case words, or lowercase connection words
    # Example: Vegetable Soup of Valentines-day
    name_pattern = r'^V[a-z]+(\s([A-Z][a-z]+|[a-z]+))*$'
    
    # Price pattern: Two digits followed by ,14
    price_pattern = r'^\d{2},14$'
    
    if re.match(name_pattern, name) and re.match(price_pattern, price):
        return True
    return False

def print_heart():
    heart = [
        "  *** *** ",
        " ***** ***** ",
        "*************",
        " *********** ",
        "  ********* ",
        "   ******* ",
        "    ***** ",
        "     *** ",
        "      * "
    ]
    for line in heart:
        print(line)
        
#exs2
#class structure
import random
import json

class Character:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.stats = {
            "Strength": self.roll_dice(),
            "Dexterity": self.roll_dice(),
            "Constitution": self.roll_dice(),
            "Intelligence": self.roll_dice(),
            "Wisdom": self.roll_dice(),
            "Charisma": self.roll_dice()
        }

    @staticmethod
    def roll_dice():
        rolls = [random.randint(1, 6) for _ in range(4)]
        rolls.sort()
        return sum(rolls[1:]) # Sum the top 3

class Game:
    def __init__(self):
        self.players = []

    def start(self):
        num_players = int(input("How many players? "))
        for _ in range(num_players):
            name = input("Character Name: ")
            age = input("Character Age: ")
            self.players.append(Character(name, age))
        
        self.export_json()
        self.export_txt()

    def export_json(self):
        data = [p.__dict__ for p in self.players]
        with open("characters.json", "w") as f:
            json.dump(data, f, indent=4)

    def export_txt(self):
        with open("characters.txt", "w") as f:
            for p in self.players:
                f.write(f"--- {p.name} (Age: {p.age}) ---\n")
                for stat, val in p.stats.items():
                    f.write(f"{stat}: {val}\n")
                f.write("\n")