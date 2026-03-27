#exs1
def get_age(year, month, day):
    # Hard-coded current date (March 2026)
    current_year = 2026
    current_month = 3
    
    age = current_year - year
    
    # If the birthday hasn't happened yet this year, subtract 1
    if current_month < month:
        age -= 1
        
    return age

def can_retire(gender, date_of_birth):
    # Split the "yyyy/mm/dd" string into integers
    year, month, day = map(int, date_of_birth.split("/"))
    
    age = get_age(year, month, day)
    
    if gender == "m":
        return age >= 67
    elif gender == "f":
        return age >= 62
    else:
        return False

# Asking for input
user_gender = input("Enter your gender (m/f): ").lower()
user_dob = input("Enter your date of birth (yyyy/mm/dd): ")

if can_retire(user_gender, user_dob):
    print("You can retire! Enjoy the golden years.")
else:
    print("You still have some working years ahead of you!")
    
#exs2
def calculate_sum(x):
    # Convert X to string to replicate it easily
    s = str(x)
    
    # Create the terms
    t1 = int(s)
    t2 = int(s * 2)
    t3 = int(s * 3)
    t4 = int(s * 4)
    
    return t1 + t2 + t3 + t4

# Example check
print(calculate_sum(3))  # Output: 3702

#exs3
import random

def throw_dice():
    return random.randint(1, 6)

def throw_until_doubles():
    throws = 0
    while True:
        throws += 1
        dice1 = throw_dice()
        dice2 = throw_dice()
        if dice1 == dice2:
            return throws

def main():
    results = []
    
    # Run the simulation 100 times
    for _ in range(100):
        attempts_to_double = throw_until_doubles()
        results.append(attempts_to_double)
    
    total_throws = sum(results)
    average_throws = total_throws / len(results)
    
    print(f"Total throws: {total_throws}")
    print(f"Average throws to reach doubles: {round(average_throws, 2)}")

# Run the main function
main()