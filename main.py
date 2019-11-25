import random

# Create objects for players with ID and playedWith list, will use ID later
class Players:

    def __init__(self, name):
        self.name = name
        #self.id = id
        self.playedWith = []

    # def add_player(self, playedWith):
    #     self.playedWith = playedWith

    def name(self, id):
        self.id = id

playerList = []
playerList.append(Players("Richard"))
playerList.append(Players("Chad"))

playerList[0].append(playerList[1])
print playerList[0].name

# Create player objects
p1 = Players(1)
p2 = Players(2)
p3 = Players(3)
p4 = Players(4)
p5 = Players(5)
p6 = Players(6)
p7 = Players(7)
p8 = Players(8)
p9 = Players(9)
p10 = Players(10)
p11 = Players(11)
p12 = Players(12)

# Give temporary placeholder names for players
Players(1).name = "Chad"
Players(2).name = "Brad"
Players(3).name = "Rob"
Players(4).name = "Zack"
Players(5).name = "Phil"
Players(6).name = "Dan"
Players(7).name = "Vector"
Players(8).name = "Robert"
Players(9).name = "Ben"
Players(10).name = "Thomas"
Players(11).name = "Brendan"
Players(12).name = "Rick"

# Create player list to be mixed
#player = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12]
player = [Players(1), Players(12), Players(3), Players(4), Players(5), Players(6), Players(7), Players(8), Players(9), Players(10), Players(11), Players(12)]

def firstRound():
    random.shuffle(player)

    # Create temporary doubles pairs (temporary method)
    dub1 = [player[0].name, player[1].name]
    dub2 = [player[2].name, player[3].name]
    dub3 = [player[4].name, player[5].name]
    dub4 = [player[6].name, player[7].name]
    dub5 = [player[8].name, player[9].name]
    dub6 = [player[10].name, player[11].name]

    # Test list for all four players on a court
    dubpair1 = [dub1, dub2]
    dubpair2 = [dub3, dub4]
    dubpair3 = [dub5, dub6]

    # Add player's first round partner to the player's playedWith list
    player[0].add_player(player[1])
    #player[0].playedWith.extend(player[1])
    player[1].add_player(player[0])
    player[2].add_player(player[3])
    player[3].add_player(player[2])
    player[4].add_player(player[5])
    player[5].add_player(player[4])
    player[6].add_player(player[7])
    player[7].add_player(player[6])
    player[8].add_player(player[9])
    player[9].add_player(player[8])
    player[10].add_player(player[11])
    player[11].add_player(player[10])

# First set of double pair created, will need to be printed and code above should be in a function

random.shuffle(player)

# Second round player mixing, finish elif statements
def secondRound():
    random.shuffle(player)
    duba1 = [player[0].name, player[1].name]
    duba2 = [player[2].name, player[3].name]
    duba3 = [player[4].name, player[5].name]
    duba4 = [player[6].name, player[7].name]
    duba5 = [player[8].name, player[9].name]
    duba6 = [player[10].name, player[11].name]

    # Checks if a player's new partner is in their playedWith list
    counter = 0   #counts while loop
    dubaNum = 1   #for dubNum
    dubNum = duba1   #double pair name
    playerNum = 0   #for playerNum
    dubCounter = 0   #for assigning dubNum
    while counter >= 6:
        if player[playerNum].playedWith.name in dubNum[dubaNum]:
            counter = 0
            dubaNum = 1
            dubNum = duba1
            playerNum = 0
            secondRound()
        else:
            counter = counter + 1
            playerNum = playerNum + 1

            if dubCounter == 0:
                dubNum = duba1
            elif dubCounter == 1:
                dubNum = duba2
            elif dubCounter == 2:
                dubNum = duba3
            elif dubCounter == 3:
                dubNum = duba4
            elif dubCounter == 4:
                dubNum = duba5
            elif dubCounter == 5:
                dubNum = duba5
            elif dubCounter == 6:
                dubNum = duba6

            if counter == 1:
                dubaNum = 0
            elif counter == 2:
                dubaNum = 1
            elif counter == 3:
                dubaNum = 0
            elif counter == 4:
                dubaNum = 1
            elif counter == 5:
                dubaNum = 0
            elif counter == 6:
                dubaNum = 1

# firstRound()
# secondRound()



