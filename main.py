import random
import itertools

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

