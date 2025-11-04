import random

from collections import UserList

from card import RANKS, SUITS, Card

class Deck(UserList):
    """Deck of cards."""

    def __init__(self):
        """Has some cards."""
        super().__init__()

        for rank in RANKS:
            for suit in SUITS:
                print(f"Creating card [{rank}][{suit}]")
                card = Card(rank, suit)
                self.append(card)
        
        self.shuffle()

    def shuffle(self):
        """Shuffle the deck."""
        random.shuffle(self)

    def draw_card(self):
        """Draw the top card."""
        try:
            return self.pop()
        except IndexError:
            return None
