#exs
x = int(input('Enter the Number:'))

# Initialize a variable to store the sum of divisors
divisor_sum = 0

# Loop through all numbers from 1 up to (but not including) x
for i in range(1, x):
    if x % i == 0:
        # If 'i' divides x perfectly, add it to the sum
        divisor_sum += i

# Check if the sum of divisors equals the original number
if divisor_sum == x:
    print(True)
else:
    print(False)