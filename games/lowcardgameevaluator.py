from games.gameevaluator import GameEvaluator
from model.card import RANKS, SUITS


class LowCardGameEvaluator(GameEvaluator):
    def evaluate_winner(self, players):
        """Evaluate the winner of the game with the lower card."""
        previous_player = players[0]
        best_candidate = players[0]

        for current_player in players[1:]:
            current_player_card = current_player.hand[0]
            previous_player_card = previous_player.hand[0]

            current_score = (
                RANKS.index(current_player_card.rank), 
                SUITS.index(current_player_card.suit)
                )
            previous_score = (
                RANKS.index(previous_player_card.rank),
                SUITS.index(previous_player_card.suit),
            )

            if current_score[0] < previous_score[0]:
                best_candidate = current_player
            elif current_score[0] == previous_score[0]:
                if current_score[1] < previous_score[1]:
                    best_candidate = current_player

            previous_player = current_player

        return best_candidate.name