#exs1
def display_message():
    print("I am learning about functions in Python.")

display_message()

#exs2
def favorite_book(title):
    print(f"One of my favorite books is {title}.")

favorite_book("Alice in Wonderland")

#exs3
def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}.")

# Calling with both arguments
describe_city("Reykjavik", "Iceland")
# Calling with only the required argument (uses default for country)
describe_city("Paris")

#exs4
import random

def compare_numbers(user_num):
    random_num = random.randint(1, 100)
    
    if user_num == random_num:
        print("Success!")
    else:
        print(f"Fail! Your number: {user_num}, Random number: {random_num}")

compare_numbers(50)

#exs5
# Defining with default values
def make_shirt(size="large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}.")

# Large shirt with default message
make_shirt()

# Medium shirt with default message
make_shirt("medium")

# Custom shirt using positional arguments
make_shirt("small", "Keep Coding")

# Bonus: Using keyword arguments
make_shirt(text="Hello!", size="extra-small")

#exs6
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(magicians):
    for name in magicians:
        print(name)

def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = f"{magicians[i]} the Great"

make_great(magician_names)
show_magicians(magician_names)

#exs7
import random

def get_random_temp(month):
    # Determine temperature range based on season (Bonus Step 5)
    if month in [12, 1, 2]:    # Winter
        return random.uniform(-10, 5)
    elif month in [3, 4, 5]:   # Spring
        return random.uniform(6, 18)
    elif month in [6, 7, 8]:   # Summer
        return random.uniform(19, 40)
    else:                      # Fall (9, 10, 11)
        return random.uniform(5, 20)

def main():
    try:
        user_month = int(input("Enter the month number (1-12): "))
        # Get a random float (Bonus Step 4)
        temp = get_random_temp(user_month)
        
        print(f"The temperature right now is {temp:.1f} degrees Celsius.")

        # Temperature-based advice
        if temp < 0:
            print("Brrr, that’s freezing! Wear some extra layers today.")
        elif 0 <= temp <= 16:
            print("Quite chilly! Don’t forget your coat.")
        elif 16 < temp <= 23:
            print("Nice weather.")
        elif 23 < temp <= 32:
            print("A bit warm, stay hydrated.")
        else:
            print("It’s really hot! Stay cool.")
            
    except ValueError:
        print("Please enter a valid number for the month.")

main()