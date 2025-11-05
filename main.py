"""Entry point."""

from model.deck import Deck
from view.playerview import PlayerView
from view.broadcastview import BroadcastView
from view.internetstreamingview import InternetStreamingView
from view.views import Views
from controller.gamecontroller import GameController
from controller.highcardgameevaluator import HighCardGameEvaluator
from controller.lowcardgameevaluator import LowCardGameEvaluator


def main():
    # Prepare useful variables
    deck = Deck()
    active_view = PlayerView()
    passive_views = (BroadcastView(), InternetStreamingView())
    views = Views(active_view, passive_views)

    # The player with the highest card wins
    game = GameController(deck, views, HighCardGameEvaluator())
    game.run()

    # The player with the lowest card wins
    # game = GameController(deck, views, LowCardGameEvaluator())
    # game.run()


if __name__ == "__main__":
    main()
