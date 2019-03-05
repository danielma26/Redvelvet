class Redvelvet:

    memCount = 0

    def __init__(self, name, age, height, bloodtype):
        self.name = name
        self.height = height
        self.age = age
        self.bloodtype = bloodtype
        Redvelvet.memCount += 1

    def displayCount(self):
        print "Total member %d" % Redvelvet.memCount

    def displayRedvelvet(self):
        print "Name : ", self.name, "age :", self.age, " height: ", self.height, " bloodtype: ", self.bloodtype

"This will create first member of redvelvet class"
mem1 = Redvelvet("Irene", 27, 158, "A")

"This will create second member of redvelvet class"
mem2 = Redvelvet("Seulgi", 25, 161, "A")

"This will create third member of redvelvet class"
mem3 = Redvelvet("Wendy", 25, 159, "O")

"This will create forth member of redvelvet class"
mem4 = Redvelvet("Joy", 22, 167, "A")

"This will create fift member of redvelvet class"
mem5 = Redvelvet("Yeri", 19, 159, 'O')


mem1.displayRedvelvet()
mem2.displayRedvelvet()
mem3.displayRedvelvet()
mem4.displayRedvelvet()
mem5.displayRedvelvet()

print "Total number of Redvelvet %d" % Redvelvet.memCount
