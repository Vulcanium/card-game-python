"""Define the internet streaming view."""


class InternetStreamingView:
    """Card game stream on internet."""

    def show_player_hand(self, name, hand):
        card = hand[0]
        card = card if card.is_face_up else "face-down card"
        print(f"[Internet] {name} -> {card}")

    def show_winner(self, name):
        print(f"[Internet] {name} wins!")