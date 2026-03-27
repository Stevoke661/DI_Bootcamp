#exercise
import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = []
        self.reset_deck()

    def reset_deck(self):
        """Helper to populate the deck with 52 cards."""
        self.cards = [Card(s, v) for s in self.suits for v in self.values]

    def shuffle(self):
        """Ensures a full deck and rearranges them."""
        if len(self.cards) != 52:
            print("Replenishing deck before shuffle...")
            self.reset_deck()
        random.shuffle(self.cards)
        print("Deck shuffled!")

    def deal(self):
        """Deals one card and removes it from the list."""
        if len(self.cards) == 0:
            return "No cards left in the deck!"
        return self.cards.pop()

# --- Testing the implementation ---
my_deck = Deck()
my_deck.shuffle()

card_dealt = my_deck.deal()
print(f"Dealt: {card_dealt}")
print(f"Cards remaining: {len(my_deck.cards)}")