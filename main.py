"""Entry point."""

from model.deck import Deck
from view.commandlineview import CommandLineView
from controller.gamecontroller import GameController


def main():
    game = GameController(Deck(), CommandLineView())
    game.run()


if __name__ == "__main__":
    main()
