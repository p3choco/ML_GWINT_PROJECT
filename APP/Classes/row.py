class Row:
    def __init__(self, cards_list):
        self.cards_list = list(cards_list)
        self.isHorn = False
        self.isWeather = False

    def __str__(self):
        if not self.cards_list:
            return "[ Pusto ]"
        return "\n    ".join(str(card) for card in self.cards_list)

    def add_card(self, card):
        self.cards_list.append(card)

    def get_cards(self):
        return self.cards_list
