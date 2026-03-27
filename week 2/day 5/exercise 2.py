#part 1
import random

class Game:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]

    def get_user_item(self):
        """Ask the user for their move and validate it."""
        while True:
            user_input = input("Select an item (rock/paper/scissors): ").lower().strip()
            if user_input in self.choices:
                return user_input
            print("Invalid choice. Please try again.")

    def get_computer_item(self):
        """Randomly select a move for the computer."""
        return random.choice(self.choices)

    def get_game_result(self, user_item, computer_item):
        """Determine if the user won, lost, or drew."""
        if user_item == computer_item:
            return "draw"
        
        # Win conditions for the user
        win_conditions = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper"
        }
        
        if win_conditions[user_item] == computer_item:
            return "win"
        else:
            return "loss"

    def play(self):
        """Orchestrate a single round of the game."""
        user_choice = self.get_user_item()
        computer_choice = self.get_computer_item()
        result = self.get_game_result(user_choice, computer_choice)
        
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        print(f"Result: You {result}!")
        print("-" * 20)
        
        return result
    
    part 2
    from game import Game

def get_user_menu_choice():
    """Display menu and return a validated choice."""
    print("\n--- Main Menu ---")
    print("1. Play a new game")
    print("2. Show scores")
    print("3. Quit")
    
    while True:
        choice = input("Enter your choice (1-3): ").strip()
        if choice in ["1", "2", "3"]:
            return choice
        print("Invalid selection. Please enter 1, 2, or 3.")

def print_results(results):
    """Format and print the session summary."""
    print("\n" + "="*20)
    print("FINAL SUMMARY")
    print(f"Wins:   {results['win']}")
    print(f"Losses: {results['loss']}")
    print(f"Draws:  {results['draw']}")
    print("="*20)
    print("Thanks for playing!")

def main():
    # Initialize the results dictionary
    results = {"win": 0, "loss": 0, "draw": 0}
    
    while True:
        choice = get_user_menu_choice()
        
        if choice == "1":
            # Create a new Game instance and play
            new_game = Game()
            outcome = new_game.play()
            # Update the score
            results[outcome] += 1
            
        elif choice == "2":
            # Just show current scores without quitting
            print(f"\nCurrent Scoreboard: {results}")
            
        elif choice == "3":
            # Exit the loop and show final summary
            print_results(results)
            break

if __name__ == "__main__":
    main()