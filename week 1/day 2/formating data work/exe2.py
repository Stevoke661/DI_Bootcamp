#exs1
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Using extend
list1.extend(list2)
print(list1)

#exs2
for num in range(1500, 2501):
    if num % 5 == 0 and num % 7 == 0:
        print(num)
        
#exs3
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user_name = input("Enter your name: ")

if user_name in names:
    print(names.index(user_name))
else:
    print("Name not found.")
    
#exs4
num1 = int(input("Input the 1st number: "))
num2 = int(input("Input the 2nd number: "))
num3 = int(input("Input the 3rd number: "))

greatest = max(num1, num2, num3)
print(f"The greatest number is: {greatest}")

#exs5
alphabet = "abcdefghijklmnopqrstuvwxyz"
vowels = "aeiou"

for letter in alphabet:
    if letter in vowels:
        print(f"{letter} is a vowel")
    else:
        print(f"{letter} is a consonant")
        
#exs6
words = []
for i in range(7):
    words.append(input(f"Enter word {i+1}: "))

letter = input("Enter a single character: ")

for word in words:
    index = word.find(letter)
    if index != -1:
        print(f"In '{word}', '{letter}' first appears at index {index}.")
    else:
        print(f"Sorry, the letter '{letter}' is not in the word '{word}'.")
        
#exs7
numbers = list(range(1, 1000001))

print(f"Min: {min(numbers)}")
print(f"Max: {max(numbers)}")
print(f"Sum: {sum(numbers)}")

#exs8
raw_input = input("Enter comma-separated numbers: ")
# split() creates a list based on a delimiter
list_version = raw_input.split(",")
tuple_version = tuple(list_version)

print(list_version)
print(tuple_version)

#exs9
import random

wins = 0
losses = 0

while True:
    user_input = input("Guess a number 1-9 (or type 'quit' to stop): ")
    
    if user_input.lower() == 'quit':
        break
        
    user_guess = int(user_input)
    secret_number = random.randint(1, 9)
    
    if user_guess == secret_number:
        print("Winner!")
        wins += 1
    else:
        print(f"Better luck next time. The number was {secret_number}.")
        losses += 1

print(f"\nGame Over! Total Wins: {wins} | Total Losses: {losses}")
