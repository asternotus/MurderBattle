from Citizen import Citizen

class Player(Citizen):

    def __init__(self, name, card, position, strikes, type):
        super().__init__(name, card)
        self.type = type
        self.position = position
        self.strikes = strikes
        self.cards = []
        self.cards.append(card)