#challenge 3
# 1. Initialize an empty list to store our data
user_data = []

print("Please enter the Name, Age, and Score for 5 users:")

# 2. Collect input 5 times
for i in range(5):
    user_input = input(f"Enter user {i+1} (format: Name,Age,Score): ")
    # Split the string and convert to a tuple
    # We keep them as strings/ints based on the requirement
    name, age, score = user_input.split(',')
    user_data.append((name.strip(), int(age), int(score)))

# 3. Sort the list using a lambda function
# The priority is Name > Age > Score
user_data.sort(key=lambda x: (x[0], x[1], x[2]))

# 4. Print the final result
print("\nSorted List:")
print(user_data)