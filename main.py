import random

class Players:
    name = ""
    id = 0
    playedWith = []

    def __init__(self, id):
        self.id = id

    def played(self, id):
        self.playedWith.append(id)

    def name(self, name):
        self.name = name

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

p1.name = "Chad"
p2.name = "Brad"
p3.name = "Rob"
p4.name = "Zack"
p5.name = "Phil"
p6.name = "Dan"
p7.name = "Vector"
p8.name = "Vvs"
p9.name = "Ben"
p10.name = "Goin"
p11.name = "Fdfd"
p12.name = "Rurur"

player = [p1.name, p2.name, p3.name, p4.name, p5.name, p6.name, p7.name, p8.name, p9.name, p10.name, p11.name, p12.name]

random.shuffle(player)

p1.playedWith(player())
