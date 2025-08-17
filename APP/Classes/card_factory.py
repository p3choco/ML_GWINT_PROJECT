from king import King, king_names
from special_card import SpecialCard, special_cards
from character import Character
from card import Card

class CardFactory: 
    
    @staticmethod
    def create_card(signs):
        for sign in signs:
            if sign in special_cards:
                return SpecialCard(signs)
            elif sign in king_names:
                return King(signs)
        
        return Character(signs)
