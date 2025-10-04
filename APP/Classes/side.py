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