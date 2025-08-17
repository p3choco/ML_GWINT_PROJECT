from card import Card

special_cards = {
    "mgla",
    "czyste niebo",
    "deszcz", 
    "mroz",
    "pozoga",
    "rogkarta",
    "manekin"
}

class SpecialCard(Card):

    name = None

    def __init__(self, signs):
        super().__init__("special_card")

        for sign in signs:
            if sign in special_cards:
                self.name = sign

    def __str__(self):
        return f"""
        Card type: {self.card_type}
        Name: {self.name}
        """