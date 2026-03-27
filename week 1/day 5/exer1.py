#basic list
# Exercise 1: Insert item at index
my_list = [1, 2, 4, 5]
item = 3
index = 2
my_list.insert(index, item)
print(my_list)

# Exercise 2: Count spaces in a string
text = "Hello World from Python"
space_count = 0
for char in text:
    if char == " ":
        space_count += 1
print(f"Spaces: {space_count}")

# Exercise 3: Count upper and lower case
text = "Hello World!"
upper, lower = 0, 0
for char in text:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
print(f"Upper: {upper}, Lower: {lower}")

#custom logic function
# Exercise 4: Manual Sum
def my_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total

# Exercise 5: Manual Max
def find_max(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

# Exercise 6: Factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Exercise 7: Manual Count
def list_count(arr, target):
    count = 0
    for item in arr:
        if item == target:
            count += 1
    return count

# Exercise 8: L2-Norm
def norm(arr):
    # Formula: sqrt(x1^2 + x2^2 + ...)
    sum_sq = 0
    for x in arr:
        sum_sq += x**2
    return sum_sq**0.5

# Exercise 9: Monotonic Check
def is_mono(arr):
    # Check if all elements are non-increasing OR non-decreasing
    inc = dec = True
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]: inc = False
        if arr[i] < arr[i+1]: dec = False
    return inc or dec

#list processing
# Exercise 10: Longest word
def longest_word(words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    print(longest)

# Exercise 11: Separate types
def separate_types(mixed_list):
    ints = [x for x in mixed_list if type(x) == int]
    strs = [x for x in mixed_list if type(x) == str]
    return ints, strs

# Exercise 12: Palindrome
def is_palindrome(s):
    clean_s = str(s).lower()
    return clean_s == clean_s[::-1]

# Exercise 13: Words longer than k
def sum_over_k(sentence, k):
    words = sentence.split()
    count = 0
    for word in words:
        if len(word) > k:
            count += 1
    return count

# Exercise 14: Dictionary average
def dict_avg(d):
    values = d.values()
    return sum(values) / len(values)

#advanced logic
# Exercise 15: Common Divisors
def common_div(a, b):
    divisors = []
    # Only need to check up to the smaller of the two numbers
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            divisors.append(i)
    return divisors

# Exercise 16: Prime Check
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Exercise 17: Even index AND even value
def weird_print(arr):
    result = []
    for i in range(len(arr)):
        if i % 2 == 0 and arr[i] % 2 == 0:
            result.append(arr[i])
    print(result)

# Exercise 18: Keyword argument type counter
def type_count(**kwargs):
    counts = {}
    for val in kwargs.values():
        t_name = type(val).__name__
        counts[t_name] = counts.get(t_name, 0) + 1
    # Formatting the output as requested
    return ", ".join([f"{k}: {v}" for k, v in counts.items()])

# Exercise 19: Manual Split
def my_split(s, delimiter=" "):
    result = []
    current_word = ""
    for char in s:
        if char == delimiter:
            result.append(current_word)
            current_word = ""
        else:
            current_word += char
    result.append(current_word) # Add last part
    return result

# Exercise 20: Password mask
def make_password(s):
    return "*" * len(s)