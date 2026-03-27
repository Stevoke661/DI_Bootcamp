#exs1
# Create and populate
my_fav_numbers = {7, 13, 22, 42}

# Add two numbers
my_fav_numbers.add(10)
my_fav_numbers.add(88)

# Remove the "last" one (Note: sets are unordered, so we remove a specific one)
my_fav_numbers.remove(88)

# Friend's set
friend_fav_numbers = {3, 7, 11, 21}

# Concatenate (Union)
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

#exs3
basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")

apple_count = basket.count("Apples")
basket.clear()

print(f"Final basket: {basket}") # Result: []

#exs4
# Using a loop with a 0.5 step logic
mixed_list = []
for x in range(3, 11):
    mixed_list.append(x / 2)

print(mixed_list) # [1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]

#exs5
# All numbers 1-20
for i in range(1, 21):
    print(i)

# Numbers where the index (value) is even
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
        
#exs6
while True:
    name = input("Please enter your name: ")
    
    if not name.isdigit() and len(name) >= 3:
        print("Thank you!")
        break
    else:
        print("Invalid input. Name must be at least 3 letters and no digits.")
        
#exs7
user_input = input("Enter your favorite fruits separated by spaces: ")
fav_fruits = user_input.split()

choice = input("Enter the name of a fruit: ")

if choice in fav_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")
    
#exs8
toppings = []
base_price = 10

while True:
    topping = input("Enter a topping (or 'quit' to finish): ").lower()
    if topping == 'quit':
        break
    
    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")

total_price = base_price + (len(toppings) * 2.50)
print(f"\nYour toppings: {', '.join(toppings)}")
print(f"Total price: ${total_price:.22f}")

#exs9
# Part 1: Family Tickets
total_cost = 0
family_size = int(input("How many people are buying tickets? "))

for _ in range(family_size):
    age = int(input("Enter age: "))
    if 3 <= age <= 12:
        total_cost += 10
    elif age > 12:
        total_cost += 15

print(f"Total ticket cost: ${total_cost}")

# Bonus: Restricted Movie
teens = ["Alice", "Bob", "Charlie", "Dave"]
allowed = []

for name in teens:
    age = int(input(f"How old is {name}? "))
    if 16 <= age <= 21:
        allowed.append(name)

print(f"Final attendees: {allowed}")
