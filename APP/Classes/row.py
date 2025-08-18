class Row:

    def __init__(self, cards_list):
        self.cards_list = []
        for card in cards_list:
            self.cards_list.append(card)
    
    def __str__(self):
        message = ""
        for card in self.cards_list:
            message += f"\nCard:\n { card }"
        return message
        
        
        




