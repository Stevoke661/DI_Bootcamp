#exs1
print(("Hello world" * 4) + ("I love python" * 4))

#exs2
month = int(input("Enter a month (1-12): "))

if 3 <= month <= 5:
    print("The season is Spring.")
elif 6 <= month <= 8:
    print("The season is Summer.")
elif 9 <= month <= 11:
    print("The season is Autumn.")
elif month == 12 or 1 <= month <= 2:
    print("The season is Winter.")
else:
    print("That's not a valid month! Please enter a number between 1 and 12.")