from APP.Classes.king import King
from row import Row


class Side:
    def __init__(self, side):
        self.sword_row = Row(side.get('sword_row', []))
        self.bow_row = Row(side.get('bow_row', []))
        self.catapult_row = Row(side.get('catapult_row', []))
        self.no_row = Row(side.get('no_row', []))

        self.king_card = next((card for card in side.get('no_row', []) if isinstance(card, King)), None)

    def __str__(self):
        return f"""
    King Card: {self.king_card}

    SWORD ROW:
        {self.sword_row}

    BOW ROW:
        {self.bow_row}

    CATAPULT ROW:
        {self.catapult_row}
        """
    def findRow(self, card):
        if card.card_type == 'king':
            return self.no_row
        # TODO partia skojatel zmiana
        if card.card_row == 'miecz':
            return self.sword_row
        elif card.card_row == 'lucznik':
            return self.bow_row
        elif card.card_row == 'katapulta':
            return self.catapult_row
        else:
            return self.no_row