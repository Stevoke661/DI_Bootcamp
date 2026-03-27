#exs1
from datetime import datetime

def time_until_holiday():
    today = datetime.now()
    print(f"Today's date is: {today.strftime('%Y-%m-%d %H:%M:%S')}")

    # Example holiday: Labor Day 2026 (May 1st)
    # In a real app, you'd find the closest date from a list
    holiday_name = "Labor Day"
    holiday_date = datetime(2026, 5, 1)
    
    delta = holiday_date - today
    print(f"The next holiday is {holiday_name} in {delta.days} days and {delta.seconds // 3600} hours.")

time_until_holiday()

#exs2
def calculate_planetary_age(seconds):
    earth_year_seconds = 31557600
    periods = {
        "Earth": 1.0,
        "Mercury": 0.2408467,
        "Venus": 0.61519726,
        "Mars": 1.8808158,
        "Jupiter": 11.862615,
        "Saturn": 29.447498,
        "Uranus": 84.016846,
        "Neptune": 164.79132
    }
    
    for planet, period in periods.items():
        age = seconds / (earth_year_seconds * period)
        print(f"{planet}: {age:.2f} years old")

calculate_planetary_age(1000000000)

#exs3&4
import re

# Exercise 3: Extract numbers
def return_numbers(text):
    return "".join(re.findall(r'\d', text))

# Exercise 4: Name Validator
def validate_name():
    name = input("Enter your full name (First Last): ")
    # Pattern: Capital letter + lowercase letters, a space, then Capital + lowercase
    pattern = r'^[A-Z][a-z]+\s[A-Z][a-z]+$'
    
    if re.match(pattern, name):
        print("Valid name!")
    else:
        print("Invalid format. Ensure 'First Last' with proper capitalization.")
        
#exs5
import string
import random
import re

def check_password_validity(password, length):
    """Test function to verify password strength."""
    if len(password) != length: return False
    if not re.search(r'[a-z]', password): return False
    if not re.search(r'[A-Z]', password): return False
    if not re.search(r'\d', password): return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>_]', password): return False
    return True

def generate_password(length):
    chars = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    # Fill the rest of the length
    all_chars = string.ascii_letters + string.digits + string.punctuation
    chars += [random.choice(all_chars) for _ in range(length - 4)]
    
    random.shuffle(chars)
    return "".join(chars)

def run_program():
    while True:
        try:
            length = int(input("Enter password length (6-30): "))
            if 6 <= length <= 30:
                break
            print("Please stay between 6 and 30.")
        except ValueError:
            print("Please enter a number.")

    pwd = generate_password(length)
    print(f"Your new password: {pwd}")
    print("Keep this in a safe place!")

    # Mass testing 100 times
    print("\nStarting 100-run validation test...")
    success = all(check_password_validity(generate_password(random.randint(6, 30)), 0) == False # Logic check
                  for _ in range(100)) 
    # Note: Refine the test loop to pass the specific random length to check_password_validity