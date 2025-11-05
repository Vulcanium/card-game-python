"""Define the game controller."""

from typing import List

from model.deck import Deck
from model.player import Player
from view.views import Views
from controller.gameevaluator import GameEvaluator

MAXIMUM_PLAYERS = 5


class GameController:
    """Game controller."""

    def __init__(
            self, 
            deck: Deck, 
            view: Views, 
            game_evaluator: GameEvaluator
            ):
        """Has a deck, a list of players, a view and an evaluator."""

        # Models
        self.players: List[Player] = []
        self.deck = deck

        # View
        self.view = view

        # Evaluator
        self.game_evaluator = game_evaluator

    def get_players(self):
        """Get some players."""
        while len(self.players) < MAXIMUM_PLAYERS:

            name = self.view.prompt_for_player()

            if not name:
                return
            
            player = Player(name)
            self.players.append(player)

    def start_game(self):
        """Shuffle the deck and makes the players draw a card."""
        self.deck.shuffle()

        for player in self.players:
            card = self.deck.draw_card()
            if card:
                player.hand.append(card)

    def evaluate_game(self):
        """Evaluate the best player."""
        return self.game_evaluator.evaluate_winner(self.players)

    def rebuild_deck(self):
        """Rebuild the deck."""
        for player in self.players:
            while player.hand:
                card = player.hand.pop()
                card.is_face_up = False
                self.deck.append(card)
                
        self.deck.shuffle()

    def run(self):
        """Run the game."""
        self.get_players()

        running = True
        while running:

            self.start_game()
            for player in self.players:
                self.view.show_player_hand(player.name, player.hand)

            self.view.prompt_for_flip_cards()
            for player in self.players:
                for card in player.hand:
                    card.is_face_up = True

                self.view.show_player_hand(player.name, player.hand)

            self.view.show_winner(self.evaluate_game())
            running = self.view.prompt_for_new_game()

            self.rebuild_deck()
