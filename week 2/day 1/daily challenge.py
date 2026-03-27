#challenge
class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type=None, count=1, **kwargs):
        """
        Handles both positional arguments and keyword arguments (**kwargs) 
        to add animals to the dictionary.
        """
        # Step 8: Handle **kwargs for multiple animals
        if kwargs:
            for animal, qty in kwargs.items():
                self._update_animal_dict(animal, qty)
        
        # Step 3: Handle single animal input
        if animal_type:
            self._update_animal_dict(animal_type, count)

    def _update_animal_dict(self, animal_type, count):
        """Helper method to update the dictionary logic."""
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count

    def get_info(self):
        # Step 4: Format the output string
        info = f"{self.name}'s farm\n\n"
        for animal, count in self.animals.items():
            info += f"{animal: <10} : {count}\n"
        
        info += f"\n    E-I-E-I-0!"
        return info

    def get_animal_types(self):
        # Step 6: Return a sorted list of keys
        return sorted(list(self.animals.keys()))

    def get_short_info(self):
        # Step 7: Construct a human-readable summary
        animal_list = self.get_animal_types()
        
        # Pluralize animal names based on count
        plural_animals = []
        for animal in animal_list:
            if self.animals[animal] > 1:
                plural_animals.append(f"{animal}s")
            else:
                plural_animals.append(animal)

        # Logic for joining strings with commas and "and"
        if len(plural_animals) > 1:
            list_str = ", ".join(plural_animals[:-1]) + f" and {plural_animals[-1]}"
        else:
            list_str = plural_animals[0]

        return f"{self.name}'s farm has {list_str}."

# --- Testing the implementation ---

macdonald = Farm("McDonald")

# Testing the upgraded add_animal with **kwargs
macdonald.add_animal(cow=5, sheep=2, goat=12)

# Testing positional add_animal (should increment)
macdonald.add_animal('cow', 1) 

print(macdonald.get_info())
print("-" * 20)
print(macdonald.get_short_info())