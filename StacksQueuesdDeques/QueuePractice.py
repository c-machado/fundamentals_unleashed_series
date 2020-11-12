class QueuePractice(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, element):
        self.stack1.insert(0, element)
        # print("enqueue")

    def dequeue(self):
        self.stack1.pop()
        # print("dequeue")

    def print_items(self):
        print(self.items)

x = QueuePractice()
for i in range(5):
    print(i)
    x.enqueue(i)
    # print(x.enqueue(i))

for i in range(5):
    print(x.dequeue())