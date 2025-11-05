"""Define the broadcast view."""


class BroadcastView:
    """Card game broadcast on TV."""

    def show_player_hand(self, player_name, player_hand):
        card = player_hand[0]
        card = card if card.is_face_up else "face-down card"
        print(f"[TV] {player_name} -> {card}")

    def show_winner(self, name):
        print(f"[TV] {name} wins!")