class Card:

    SPECIAL_CARDS = {"Jack" : 11, "Queen" : 12, "King" : 13, "Ace" : 14}

    def __init__(self, value, suit):
        self._value = value
        self.suit = suit

    @property
    def value(self):
        return self._value
    
    def show(self):
        print("Value : ",self.value)
        print("Suit : "self.suit)