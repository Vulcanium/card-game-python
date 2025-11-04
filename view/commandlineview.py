"""Command line view."""


class CommandLineView:
    """Card game view."""
        
    def prompt_for_player(self):
        """Prompt for a player name."""
        player_name = input("Enter player name: ")
        if not player_name:
            return None
        return player_name

    def show_player_hand(self, player_name, player_hand):
        """Show the player hand."""
        print(f"[Player {player_name}]")

        for card in player_hand:
            if card.is_face_up:
                print(card)
            else:
                print("(face-down card)")


    def prompt_for_flip_cards(self):
        """Request to reveal the cards."""
        print()
        input("Ready to reveal the cards?")
        return True

    def show_winner(self, player_name):
        """Show the winner."""
        print(f"Congrats {player_name} !")

    def prompt_for_new_game(self):
        """Request to replay."""
        print("Do you want to play again?")
        choice = input("y/n: ")
        if choice.strip().lower() == "n":
            return False
        return True

