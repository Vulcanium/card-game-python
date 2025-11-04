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

        self._rank_score = RANKS.index(self.rank)
        self._suit_score = SUITS.index(self.suit)

    def __str__(self):
        """Used in print."""
        return f"{self.rank} of {self.suit}"
    
    def __repr__(self):
        """Used in print."""
        return str(self)
    
    def __lt__(self, other: "Card"):
        """Compares the score of the current card with the score of another card."""
        if self._rank_score != other._rank_score:
            return self._rank_score < other._rank_score
        
        return self._suit_score < other._suit_score
