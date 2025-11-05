"""Define the views."""


class Views:
    """Implement the other views."""

    def __init__(self, active_view, views):
        """Init the active view and the passive views."""
        self.active_view = active_view
        self.views = views

    def prompt_for_player(self):
        """Call the active view."""
        return self.active_view.prompt_for_player()

    def show_player_hand(self, player_name, player_hand):
        """Call the passive views."""
        for view in self.views:
            view.show_player_hand(player_name, player_hand)

    def prompt_for_flip_cards(self):
        """Call the active view."""
        return self.active_view.prompt_for_flip_cards()

    def show_winner(self, player_name):
        """Call the passive views."""
        for view in self.views:
            view.show_winner(player_name)

    def prompt_for_new_game(self):
        """Call the active view."""
        return self.active_view.prompt_for_new_game()