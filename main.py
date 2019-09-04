import random
import itertools


p1 = "Tom"
p2 = "Brad"
p3 = "Chad"
p4 = "Frank"
p5 = "John"
p6 = "Alex"
p7 = "Thomas"
p8 = "Phil"
p9 = "Dan"
p10 = "Robert"
p11 = "Dequavis"
p12 = "Zack"

p1playedwith = []
p2playedwith = []
p3playedwith = []
p4playedwith = []
p5playedwith = []
p6playedwith = []
p7playedwith = []
p8playedwith = []
p9playedwith = []
p10playedwith = []
p11playedwith = []
p12playedwith = []

p1playedagainst = []
p2playedagainst = []
p3playedagainst = []
p4playedagainst = []
p5playedagainst = []
p6playedagainst = []
p7playedagainst = []
p8playedagainst = []
p9playedagainst = []
p10playedagainst = []
p11playedagainst = []
p12playedagainst = []

players = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12]

random.shuffle(players)

dub1 = players[0], players[1]
dub2 = players[2], players[3]
dub3 = players[4], players[5]
dub4 = players[6], players[7]
dub5 = players[8], players[9]
dub6 = players[10], players[11]

p1playedwith.append(dub1)
p2playedwith.append(dub1)
p3playedwith.append(dub2)
p4playedwith.append(dub2)
p5playedwith.append(dub3)
p6playedwith.append(dub3)
p7playedwith.append(dub4)
p8playedwith.append(dub4)
p9playedwith.append(dub5)
p10playedwith.append(dub5)
p11playedwith.append(dub6)
p12playedwith.append(dub6)

p1playedagainst.append(dub2)
p2playedagainst.append(dub2)
p3playedagainst.append(dub1)
p4playedagainst.append(dub1)
p5playedagainst.append(dub4)
p6playedagainst.append(dub4)
p7playedagainst.append(dub3)
p8playedagainst.append(dub3)
p9playedagainst.append(dub6)
p10playedagainst.append(dub6)
p11playedagainst.append(dub5)
p12playedagainst.append(dub5)

random.shuffle(players)

dub1 = players[0], players[1]
dub2 = players[2], players[3]
dub3 = players[4], players[5]
dub4 = players[6], players[7]
dub5 = players[8], players[9]
dub6 = players[10], players[11]

'''
players = ["Tom", "Chad", "Brad", "Don", "Kevin", "Arnold", "Rod", "Joe"]

# results = list(itertools.permutations(players, 4))
random.shuffle(players)
x = 0

testgroup = []
firstdubs = []
seconddubs = []

for y in range(8):
    testgroup.append(players[x])
    x = x+1

x = 0

for r in range(4):
    firstdubs.append(testgroup[x])
    x = x+1

for t in range(4):
    seconddubs.append(testgroup[x])
    x = x+1

firstdoubles = firstdubs
seconddoubles = seconddubs


print ("First Match: COURT1:", firstdoubles)
print ("First Match: COURT2:", seconddoubles)

firstdoubles = [firstdubs[0], seconddubs[0], firstdubs[1], seconddubs[1]]
seconddoubles = [firstdubs[2], seconddubs[2], firstdubs[3], seconddubs[3]]

print ("Second Match: COURT1:", firstdoubles)
print ("Second Match: COURT2:", seconddoubles)

# firstdoubles.insert(0, firstdoubles.pop())
# seconddoubles.insert(0, seconddoubles.pop())
'''

