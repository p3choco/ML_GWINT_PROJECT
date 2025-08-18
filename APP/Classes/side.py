from row import Row

class Side: 

    def __init__(self, side):
        self.sword_row = Row(side['sword_row'])
        self.bow_row = Row(side['bow_row'])
        self.catapult_row = Row(side['catapult_row'])

        self.king_card = next((card for card in side["no_row"] if card.card_type == "king"), None)
    
    
    def __str__(self):
        return f"""
    King Card: { self.king_card }

    SWORD ROW:
        { self.sword_row }
        
    BOW ROW:
        { self.bow_row }

    CATAPULT ROW:
        { self.catapult_row } 
        """

