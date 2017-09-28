import random

from States.State import State

class KillStealState(State):

    def killSteal(self, citizens, player):

        if(player.type == "player"):

            self.ans = input("Убить или украсть? (введи kill, чтобы убить, steal, чтобы украсть или no, чтобы закончить ход)\n")

            if(self.ans == "kill"):
                self.showCitizens(citizens)
                self.number = input("Введите номер игрока для убийства\n")
                citizens[int(self.number)].effects.append("killed")

            if(self.ans == "steal"):
                self.showCitizens(citizens)
                self.number = input("Введите номер игрока для кражи карты\n")
                citizens[int(self.number)].effects.append("stolen")

        else:
            self.number = random.randint(0, len(citizens))
            citizens[int(self.number)].effects.append("killed")

        print("Ход принят\n")

        return self.number