from APP.Classes.const.cards import special_cards
from card import Card

class SpecialCard(Card):

    def __init__(self, signs):
        super().__init__("special_card")

        self.name = None

        for sign in signs:
            if sign in special_cards:
                self.name = sign

    def __str__(self):
        return f"""
        Card type: {self.card_type}
        Name: {self.name}
        """