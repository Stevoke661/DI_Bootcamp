#exs1
#Run this command in the terminal to open a python console

#exs4
my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

print(len(my_text))

#exs5
longest_length = 0

while True:
    sentence = input("Enter the longest sentence you can without the letter 'A' (or 'quit' to stop): ")
    
    if sentence.lower() == 'quit':
        break
        
    if 'a' in sentence.lower():
        print("Busted! That sentence contains an 'A'. Try again.")
    else:
        if len(sentence) > longest_length:
            longest_length = len(sentence)
            print(f"Congratulations! New record: {longest_length} characters.")
        else:
            print(f"Good, but not longer than your record of {longest_length}.")
    