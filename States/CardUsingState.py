import random

from States.State import State


class CardUsingState(State):

    def cardUsing(self, player):

        if(player.type == "player"):
            ans = input("Использовать карту (введи yes если да и no если нет)\n")
        else:
            number = random.randint(0, len(player.cards)-1)
            return

        if(ans == "yes"):
            self.showPlayerCardsInfo(player)
            number = input("Введите номер карты\n")
            print("Карта номер "+ number +" будет использована")
        if(ans == "no"):
            return