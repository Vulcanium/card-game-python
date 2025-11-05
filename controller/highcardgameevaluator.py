from controller.gameevaluator import GameEvaluator
from model.card import RANKS, SUITS


class HighCardGameEvaluator(GameEvaluator):
    def evaluate_winner(self, players):
        """Evaluate the winner of the game with the higher card."""
        best_player = None
        best_rank = None
        best_suit = None
        
        for player in players:
            new_best_player = False

            if not best_player:
                new_best_player = True

            else:
                card = player.hand[0]
                this_rank = RANKS.index(card.rank)
                this_suit = SUITS.index(card.suit)

                if this_rank >= best_rank:
                    if this_rank > best_rank:
                        new_best_player = True
                    elif this_suit > best_suit:
                        new_best_player = True

            if new_best_player:
                best_player = player
                card = player.hand[0]
                best_rank = RANKS.index(card.rank)
                best_suit = SUITS.index(card.suit)

        return best_player.name