#game set up
import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist)

# Track the game state
guessed_letters = []
attempts_left = 6
display_word = ["*" if char != " " else " " for char in word] 

print("Welcome to Hangman!")

#game loop
while attempts_left > 0 and "*" in display_word:
    print(f"\nWord: {''.join(display_word)}")
    print(f"Attempts left: {attempts_left}")
    print(f"Guessed so far: {', '.join(guessed_letters)}")
    
    guess = input("Guess a letter: ").lower()

    # Validation: Check if it's a single letter and hasn't been guessed
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue
    
    if guess in guessed_letters:
        print(f"You already guessed '{guess}'!")
        continue

    guessed_letters.append(guess)

    # Check if the guess is in the word
    if guess in word:
        print(f"Good job! '{guess}' is in the word.")
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
    else:
        attempts_left -= 1
        print(f"Sorry, '{guess}' is not there. You lost a body part!")

### 3. Ending the Game
#Once the loop finishes, we check if the user won or lost.

if "*" not in display_word:
    print(f"\nCongratulations! You guessed the word: {word}")
else:
    print(f"\nGame Over! The gallows are full. The word was: {word}")