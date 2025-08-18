from card import Card

row_types = {
                "miecz",
                "lucznik",
                "katapulta",
                "lucznik katapulta",
                "miecz lucznik",
            } 

class Character(Card):

    def __init__(self, signs):
        super().__init__("character")

        self.num_points = -1
        self.card_row = None
        self.high_morale = False
        self.bond = False
        self.horn = False
        self.is_spy = False
        self.is_hero = False

        if "wysokie morale" in signs:
            self.high_morale = True
        
        if "wiez" in signs:
            self.bond = True
        
        for sign in signs:
            
            if sign.isdigit():
                self.num_points = sign
            elif sign in row_types:
                self.card_row = sign
            elif sign == "rog":
                self.horn = True 
            elif sign == "szpiegostwo":
                self.is_spy = True
            elif sign == "bohater":
                self.is_hero = True

    def __str__(self):
        return f"""
        Card type: {self.card_type}
        Row Type: {self.card_row}
        Number of points: {self.num_points}
        Have high morale: {self.high_morale}
        Have bond: {self.bond}
        Have horn: {self.horn}
        Is spy: {self.is_spy}
        Is hero: {self.is_hero}
        """