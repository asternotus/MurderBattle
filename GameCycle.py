import random

from Card import Card
from Citizen import Citizen
from Player import Player
from States.CleanState import CleanState
from States.CardUsingState import CardUsingState
from States.KillStealState import KillStealState
from States.ResolveState import ResolveState

cards = [];
cards.append(Card('Анонимный звонок'))
cards.append(Card('Система тревоги'))
cards.append(Card('Защита свидетеля'))
cards.append(Card('Инсценировка'))
cards.append(Card('Сценический реквизит'))
cards.append(Card('Видеокамера'))
cards.append(Card('Ловушка'))
cards.append(Card('Сплетни'))
cards.append(Card('Неопытный напарник'))
cards.append(Card('Налоги'))
cards.append(Card('База данных'))
cards.append(Card('Клафелинщица'))

citizens = [];
citizens.append(Citizen('Вечно недовольная старушка', cards[0]))
citizens.append(Citizen('Надзиратель', cards[1]))
citizens.append(Citizen('Полицейский', cards[2]))
citizens.append(Citizen('Врач', cards[3]))
citizens.append(Citizen('Актёр', cards[4]))
citizens.append(Citizen('Начальник охраны', cards[5]))
citizens.append(Citizen('Охотник', cards[6]))
citizens.append(Citizen('Ночная продавщица', cards[7]))
citizens.append(Citizen('Наркоман', cards[8]))
citizens.append(Citizen('Соцработник', cards[9]))
citizens.append(Citizen('Мальчик хакер', cards[10]))
citizens.append(Citizen('Сутенер', cards[11]))

def buildPlayer(position, strikes, type):

    player = Player(citizens[position].name, citizens[position].mainCard, position, strikes, type)

    return player

def nextState(player, enemy, current_player, n):

    state = CleanState()
    state.clean(citizens)

    print("НОЧЬ "+str(n)+"\n")

    state.showPlayerInfo(current_player)

    state = CardUsingState()
    state.cardUsing(current_player)

    state = KillStealState()
    state.killSteal(citizens, current_player)

    print("ДЕНЬ "+str(n))

    state = ResolveState()
    state.resolve(citizens, current_player)

    n += 1

    print(current_player.name)

    if(current_player.type == "player"):
        nextState(player, enemy, enemy, n)
    else:
        nextState(player, enemy, player, n)

if __name__ == "__main__":

    player = buildPlayer(random.randint(0, len(citizens)-1),0, "player")
    enemy = buildPlayer(random.randint(0, len(citizens)-1),0, "enemy")
    n = 1
    nextState(player, enemy, player, n)