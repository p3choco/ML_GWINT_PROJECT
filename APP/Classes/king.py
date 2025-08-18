from card import Card

king_names = {
    "eredin dowodca",
    "eredin zdradziecki",
    "foltest zdobywca",
    "foltest dowodca polnocy",
    "foltest krol temerii",
    "foltest syn medella",
    "foltest zelazny wladca",
    "francesca elfka",
    "francesca krolowa",
    "francesca nadzieja",
    "francesca najpiekniejsza",
    "francesca stokrotka",
    "emhyr bialy plomien",
    "emhyr cesarz nilfgaardu",
    "emhyr jez z erlenwaldu",
    "emhyr najezdzca polnocy",
    "emhyr pan poludnia",
}

class King(Card):

    def __init__(self, signs):
        super().__init__("king")

        self.king_name = None
        
        for sign in signs:
            if sign in king_names:
                self.king_name = sign
    
    def __str__(self):
        return f"""
        Card type: {self.card_type}
        King name: {self.king_name}
        """