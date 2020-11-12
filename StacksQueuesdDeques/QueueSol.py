class QueueSol(object):

    def __init__(self):
        self.instack = []
        self.outstack = []

    def enqueue(self, element):
        self.instack.append(element)
        # print("enqueue")

    def dequeue(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()

x = QueueSol()
for i in range(5):
    print(i)
    x.enqueue(i)
    # print(x.enqueue(i))

for i in range(5):
    print(x.dequeue())