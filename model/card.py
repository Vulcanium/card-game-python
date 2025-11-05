"""Define the cards."""

SUITS = ("diamonds", "hearts", "spades", "clubs")
RANKS = (
    "two", 
    "three", 
    "four", 
    "five", 
    "six", 
    "seven", 
    "eight", 
    "nine", 
    "ten",
    "jack", 
    "queen", 
    "king", 
    "ace"
    )


class Card:
    """Card class.

    Has a suit and a rank.
    """

    def __init__(self, rank, suit):
        """Init the suit, the rank, is_face_up and the scores."""
        self.rank = rank
        self.suit = suit
        self.is_face_up = False

    def __str__(self):
        """Used in print."""
        return f"{self.rank} of {self.suit}"
    
    def __repr__(self):
        """Used in print."""
        return str(self)
