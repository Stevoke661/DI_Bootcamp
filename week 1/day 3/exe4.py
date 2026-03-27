#exe1
#part 1
# The raw data
car_string = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"

# 1. Convert to list (splitting by comma and space)
manufacturers = car_string.split(", ")

# 2. Print count
print(f"There are {len(manufacturers)} manufacturers in the list.")

# 3. Reverse descending order (Z-A)
# We sort it normally first, then reverse it
sorted_desc = sorted(manufacturers, reverse=True)
print(f"Z-A Order: {sorted_desc}")

#part 2
# 4. Count names with 'o'
with_o = [name for name in manufacturers if 'o' in name.lower()]
print(f"Manufacturers with 'o': {len(with_o)}")

# 5. Count names without 'i'
without_i = [name for name in manufacturers if 'i' not in name.lower()]
print(f"Manufacturers without 'i': {len(without_i)}")
bonus_list = ["Honda", "Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]

# Remove duplicates using set
unique_cars = list(set(bonus_list))

# Print as comma-separated string
# .join() is your best friend here!
print(", ".join(unique_cars))
print(f"There are now {len(unique_cars)} unique companies.")
# 1. Sort A-Z
ascending_cars = sorted(unique_cars)

# 2. Reverse letters of each name
# [::-1] is the Python "slice" trick for reversing strings
reversed_names = [name[::-1] for name in ascending_cars]

print(f"A-Z with reversed names: {reversed_names}")
