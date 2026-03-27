#exs1
import math

C = 50
H = 30

# Get input and split by comma
user_input = input("Enter comma-separated numbers for D: ")
d_values = user_input.split(",")

results = []
for d in d_values:
    # Formula: Q = Square root of [(2 * C * D)/H]
    q = math.sqrt((2 * C * int(d)) / H)
    results.append(str(round(q)))

print(",".join(results))

#exs2
import random

# Bonus 12/13/14: Generating a random list of random length
list_length = random.randint(50, 100)
numbers = [random.randint(-100, 100) for _ in range(list_length)]

# 2a & 2b
print(f"Original List: {numbers}")
print(f"Sorted Descending: {sorted(numbers, reverse=True)}")

# 3, 4, 5, 6
print(f"First and Last: {[numbers[0], numbers[-1]]}")
print(f"Greater than 50: {[n for n in numbers if n > 50]}")
print(f"Smaller than 10: {[n for n in numbers if n < 10]}")
print(f"Squared: {' '.join([str(n**2) for n in numbers])}")

# 7: Unique numbers
unique_numbers = list(set(numbers))
print(f"Unique List: {unique_numbers}\nCount: {len(unique_numbers)}")

# 11: Bonus - Manual calculations
manual_sum = 0
manual_max = numbers[0]
manual_min = numbers[0]

for n in numbers:
    manual_sum += n
    if n > manual_max: manual_max = n
    if n < manual_min: manual_min = n

manual_avg = manual_sum / len(numbers)

print(f"Sum: {manual_sum} | Avg: {manual_avg:.2f} | Max: {manual_max} | Min: {manual_min}")

# 15: Bonus Answer
# Yes, the code works regardless of list length because we use len(numbers) 
# and loops rather than hard-coded indices!

#exs3
paragraph = "Python is high-level and interpreted. It was created by Guido van Rossum. Python is great for data! Is it the best? Yes, it is."

# Calculations
chars = len(paragraph)
non_whitespace = len(paragraph.replace(" ", ""))
# Simplified sentence count: splitting by punctuation
sentences = paragraph.count(".") + paragraph.count("!") + paragraph.count("?")
words = paragraph.split()
unique_words = set([w.lower().strip(".,!?") for w in words])

print(f"Characters: {chars}")
print(f"Non-whitespace: {non_whitespace}")
print(f"Sentences: {sentences}")
print(f"Words: {len(words)}")
print(f"Unique words: {len(unique_words)}")
print(f"Avg words per sentence: {len(words) / sentences:.2f}")

#exs4
text = input("Enter a string: ")
words = text.split()

# Use a dictionary to store counts
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

# Sorting alphabetically for a cleaner output
for word in sorted(frequency.keys()):
    print(f"{word}:{frequency[word]}")