"""Entry point."""

from model.deck import Deck
from view.commandlineview import CommandLineView
from controller.gamecontroller import GameController
from games.highcardgameevaluator import HighCardGameEvaluator
from games.lowcardgameevaluator import LowCardGameEvaluator


def main():
    # The player with the highest card wins
    game = GameController(Deck(), CommandLineView(), HighCardGameEvaluator())
    game.run()

    # The player with the lowest card wins
    # game = GameController(Deck(), CommandLineView(), LowCardGameEvaluator())
    # game.run()


if __name__ == "__main__":
    main()
