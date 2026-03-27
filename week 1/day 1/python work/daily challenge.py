#challenge
import random

# 1. Ask for User Input
user_input = input("Enter a string that is exactly 10 characters long: ")

# 2. Check the Length of the String
if len(user_input) < 10:
    print("String not long enough.")
elif len(user_input) > 10:
    print("String too long.")
else:
    print("Perfect string")
    
    # 3. Print the First and Last Characters
    # Index 0 is the first, index -1 is the last
    print(f"First character: {user_input[0]}")
    print(f"Last character: {user_input[-1]}")
    
    # 4. Build the String Character by Character
    print("\nBuilding your string:")
    current_build = ""
    for char in user_input:
        current_build += char
        print(current_build)
        
    # 5. Bonus: Jumble the String
    # We convert the string to a list because strings are immutable (can't be changed in place)
    char_list = list(user_input)
    random.shuffle(char_list)
    jumbled_string = "".join(char_list)
    
    print(f"\nJumbled version: {jumbled_string}")