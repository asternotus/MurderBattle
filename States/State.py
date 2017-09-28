class State(object):

    def showCitizens(self, citizens):
        for i in range(0, len(citizens)):
            print(str(i)+") "+citizens[i].name)

    def showPlayerInfo(self, player):
        print("Ваша роль - " + player.name + "\n")

        print("Ваши карты:")

        for i in range(0, len(player.cards)):
            print(str(i)+") "+player.cards[i].name)

        print("\n")
        print("Количество страйков: "+str(player.strikes)+"\n")

    def showPlayerCardsInfo(self, player):
        for i in range(0, len(player.cards)):
            print(str(i)+") "+player.cards[i].name)

    def help(self):
        print("help")