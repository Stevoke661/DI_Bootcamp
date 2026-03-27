#challenge 1
# 1. Ask for user inputs and convert them to integers
num = int(input("Enter the number: "))
length = int(input("Enter the length: "))

# 2. Create an empty list to store the results
multiples = []

# 3. Loop through the range of the length
# We start at 1 and go to length + 1 because range is exclusive of the stop number
for i in range(1, length + 1):
    multiples.append(num * i)

# 4. Print the final list
print(multiples)

#challenge 2
# 1. Ask the user for a string
word = input("Enter a word: ")

# 2. Create an empty string to store the result
result = ""

# 3. Iterate through the input word
for char in word:
    # If the result is empty, OR the current character is NOT 
    # the same as the last character added to result...
    if len(result) == 0 or char != result[-1]:
        result += char

# 4. Print the modified string
print(result)