"""Define the game evaluator."""

from abc import ABC, abstractmethod


class GameEvaluator(ABC):
    @abstractmethod
    def evaluate_winner(self, players):
        """Evaluate the winner of the game according to the defined rules."""
        pass