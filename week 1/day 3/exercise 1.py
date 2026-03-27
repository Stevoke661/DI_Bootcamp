#exs1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# Using zip and the dict constructor
result = dict(zip(keys, values))

print(result)

#exs2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_cost = 0

for name, age in family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    
    print(f"{name.capitalize()} pays ${price}")
    total_cost += price

print(f"Total cost for the family: ${total_cost}")

#exs3
# 1. Create the dictionary
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

# 2. Modify number_stores
brand["number_stores"] = 2

# 3. Print sentence about clients
print(f"Zara sells clothes for {', '.join(brand['type_of_clothes'][:-1])} and {brand['type_of_clothes'][-1]}.")

# 4. Add country_creation
brand["country_creation"] = "Spain"

# 5. Check and update competitors
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

# 6. Delete creation_date
brand.pop("creation_date")

# 7. Print last competitor
print(f"Last competitor: {brand['international_competitors'][-1]}")

# 8. Print US major colors
print(f"US Colors: {brand['major_color']['US']}")

# 9. & 10. Length and Keys
print(f"Number of keys: {len(brand)}")
print(f"Keys: {list(brand.keys())}")

# Bonus: Merge dictionaries
more_on_zara = {"creation_date": 1975, "number_stores": 10000}
brand.update(more_on_zara) # This will overwrite the previous number_stores (2)

#exs4
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# 1. Name to Index
disney_users_A = {user: i for i, user in enumerate(users)}
print(disney_users_A)

# 2. Index to Name
disney_users_B = {i: user for i, user in enumerate(users)}
print(disney_users_B)

# 3. Sorted Alphabetically
users_sorted = sorted(users)
disney_users_C = {user: i for i, user in enumerate(users_sorted)}
print(disney_users_C)