#exs
REverseinp = raw_input()

# 1. Split the string into a list of words
words = REverseinp.split()

# 2. Reverse the list using slicing [::-1]
reversed_list = words[::-1]

# 3. Join the reversed list back into a single string
reversed = " ".join(reversed_list)

print(reversed)