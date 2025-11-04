from collections import UserList

from .card import Card


class Hand(UserList):
    """Player hand."""

    def __init__(self):
        """Has zero or more cards."""
        super().__init__()

    def append(self, object):
        """Append a card."""
        if not isinstance(object, Card):
            raise ValueError("Vous ne pouvez ajouter que des cartes !")
        return super().append(object)