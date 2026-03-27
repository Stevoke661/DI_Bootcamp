#exc1
print("Hello world" * 4)

#exs2
print((99**3) * 8)

#exs4
computer_brand = "Apple" 
print(f"I have a {computer_brand} computer.")

#exs5
name = "Gemini"
age = 1
shoe_size = 0  # I don't have feet, but let's go with 0!
info = f"My name is {name}, I am {age} year old, and even though my shoe size is {shoe_size}, I run pretty fast."

print(info)

#exs6
a = 10
b = 5

if a > b:
    print("Hello World")
    
#exs7
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("That's an even number!")
else:
    print("That's an odd number!")
    
    #exs8
    my_name = "Gemini"
user_name = input("What is your name? ")

if user_name.lower() == my_name.lower():
    print("No way! We have the same name. Are you also powered by a massive neural network?")
else:
    print(f"Nice to meet you, {user_name}. My name is cooler, but yours is okay too.")
    
#exs9
height = int(input("Enter your height in cm: "))

if height > 145:
    print("Enjoy the ride! Try not to scream too loud.")
else:
    print("You'll need to grow a bit more. Maybe try some spinach?")