class Citizen(object):

    def __init__(self, name, card):
        super().__init__()
        self.effects = []

        self.name = name
        self.mainCard = card
