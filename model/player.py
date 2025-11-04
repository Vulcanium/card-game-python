from hand import Hand

class Player:
    """Player."""

    def __init__(self, name):
        """Has a name and a hand."""
        self.name = name
        self.hand = Hand()