#exs
def count_occurrences(input_string, char):
    # Initialize the counter
    count = 0
    
    # Loop through the string character by character
    for c in input_string:
        if c == char:
            count += 1
            
    return count

# Test Cases
string1 = "Programming is cool!"
char1 = "o"
print(f"String: {string1} | Character: {char1} | Result: {count_occurrences(string1, char1)}")

string2 = "This is a great example"
char2 = "y"
print(f"String: {string2} | Character: {char2} | Result: {count_occurrences(string2, char2)}")