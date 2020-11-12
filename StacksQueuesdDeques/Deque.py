class Deque(object):

    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        self.items.pop()

    def removeRear(self):
        self.items.pop(0)

    def printDeque(self):
        print(self.items)


d = Deque()
d.addRear(1)
d.addFront(2)
d.addFront(3)
d.addRear(4)
d.addRear(5)
d.addFront(6)
d.addRear(7)
d.printDeque()
d.removeFront()
d.printDeque()


