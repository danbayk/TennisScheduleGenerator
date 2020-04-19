import sys
import random
sys.setrecursionlimit(2000)

class Players:
    def __init__(self, name):
        self.name = name
        self.playedWith = []

    def addPlayer(self, player):
        self.playedWith.append(player)

p1 = Players("Tom")
p2 = Players("Eric")
p3 = Players("Arnold")
p4 = Players("Tommy")
p5 = Players("Chad")
p6 = Players("Robert")
p7 = Players("Annie")
p8 = Players("Mike")

players = [p1, p2, p3, p4, p5, p6, p7, p8]

def firstRound():
    random.shuffle(players)
    y = 0
    for x in players:
        if y % 2 == 0:
            players[y].addPlayer(players[y + 1])
            y+=1
        else:
            players[y].addPlayer(players[y - 1])
            y+=1

def roundUp():
    random.shuffle(players)
    y = 0
    for x in players:
        if y % 2 == 0:
            if players[y + 1] in players[y].playedWith:
                roundUp()
            else:
                y+=1
        else:
            if players[y - 1] in players[y].playedWith:
                roundUp()
            else:
                y+=1
    y = 0
    for x in players:
        if y % 2 == 0:
            players[y].addPlayer(players[y + 1])
            y+=1

        else:
            players[y].addPlayer(players[y - 1])
            y+=1






firstRound()
roundUp()



