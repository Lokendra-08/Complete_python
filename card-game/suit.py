class Suit:
    
    SUIT_DETAIL = {}

    def __init__(self, description, symbol):
        self._description  =description
        self._symbol = symbol 
        Suit.SUIT_DETAIL[description] = symbol

    @property
    def description(self):
        return self._description
    
    @property
    def symbol(self):
        return self._symbol