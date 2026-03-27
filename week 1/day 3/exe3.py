#exs1,2&3
# Exercise 1: Initialize the dictionary
birthdays = {
    "Albert Einstein": "1879/03/14",
    "Ada Lovelace": "1815/12/10",
    "Alan Turing": "1912/06/23",
    "Marie Curie": "1867/11/07",
    "Nikola Tesla": "1856/07/10"
}

print("Welcome to the Birthday Registry!")

# Exercise 3: Add a new birthday first
new_name = input("Enter a name to add to the list: ")
new_date = input(f"Enter the birthday for {new_name} (YYYY/MM/DD): ")
birthdays[new_name] = new_date

# Exercise 2: Print all available names
print("\nYou can look up the birthdays of the following people:")
for name in birthdays.keys():
    print(f"- {name}")

# Exercise 1 & 2: Look-up logic
search_name = input("\nWhose birthday would you like to look up? ")

if search_name in birthdays:
    print(f"{search_name}'s birthday is on {birthdays[search_name]}.")
else:
    # Exercise 2: Error message
    print(f"Sorry, we don’t have the birthday information for {search_name}.")
    
    #exs4 part A
    items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

for fruit, price in items.items():
    print(f"A {fruit} costs {price} dollars.")
    #part B
    items_in_stock = {
    "banana": {"price": 4, "stock": 10},
    "apple": {"price": 2, "stock": 5},
    "orange": {"price": 1.5, "stock": 24},
    "pear": {"price": 3, "stock": 1}
}

total_cost = 0

for fruit, info in items_in_stock.items():
    # Accessing values inside the nested dictionary
    item_total = info["price"] * info["stock"]
    total_cost += item_total

print(f"The total cost to buy everything in stock is ${total_cost}.")
