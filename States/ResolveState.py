from Card import Card
from States.State import State

class ResolveState(State):

    def resolve(self, citizens, player):
        for citizen in citizens:
            for effect in citizen.effects:
                if(effect == "killed"):
                    print("Этой ночью нас покинул персонаж "+citizen.name+" - светлая память!")
                    self._stealing(player, citizen)
                    citizens.remove(citizen)
                if (effect == "stolen"):
                    self._stealing(player, citizen)

    def _stealing(self, player, citizen):
        print("В целом довольно скучная ночь")
        if(citizen.mainCard.name == "NO CARD"):
            print("\nВы не получили карту из этого дома\n")
        else:
            print("\nВы получили карту - "+citizen.mainCard.name+"\n")
            player.cards.append(Card(citizen.mainCard.name))
            citizen.mainCard.name = "NO CARD"




