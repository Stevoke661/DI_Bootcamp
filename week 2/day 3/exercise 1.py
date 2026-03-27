#exs1.py
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        # Returns '5 dollars' or '1 shekel'
        suffix = "s" if self.amount != 1 else ""
        return f"{self.amount} {self.currency}{suffix}"

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        return self.amount

    def __add__(self, other):
        # If adding an integer: Currency(10) + 5
        if isinstance(other, int):
            return self.amount + other
        # If adding another Currency object
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            return self.amount + other.amount
        return NotImplemented

    def __iadd__(self, other):
        # Logic for +=
        if isinstance(other, int):
            self.amount += other
        elif isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            self.amount += other.amount
        return self # iadd must return self
    
#exs2 file 1
def sum_numbers(a, b):
    print(a + b)
#file 2
from func import sum_numbers

sum_numbers(10, 20)

#exs3
import string
import random

def generate_random_string(length=5):
    letters = string.ascii_letters
    result = ''.join(random.choice(letters) for _ in range(length))
    print(result)

generate_random_string()

#exs4
from datetime import date

def display_current_date():
    today = date.today()
    print(f"Today's date is: {today}")

display_current_date()

#exs5
from datetime import datetime

def time_until_january_first():
    now = datetime.now()
    next_year = now.year + 1
    jan_first = datetime(next_year, 1, 1)
    
    delta = jan_first - now
    
    print(f"The 1st of January is in {delta.days} days and {delta.seconds // 3600} hours.")

time_until_january_first()

#exs6
from datetime import datetime

def minutes_lived(birthdate_str):
    # Format: YYYY-MM-DD
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    now = datetime.now()
    
    difference = now - birthdate
    # .total_seconds() gives the full span in seconds
    minutes = int(difference.total_seconds() / 60)
    
    print(f"You have lived approximately {minutes:,} minutes!")

minutes_lived("1995-05-15")

#exs7
from faker import Faker

fake = Faker()
users = []

def add_users(how_many):
    for _ in range(how_many):
        user_data = {
            "name": fake.name(),
            "address": fake.address(),
            "language_code": fake.language_code()
        }
        users.append(user_data)

add_users(5)
for u in users:
    print(u)
