class Stack(object):

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def print_items(self):
        print(self.items)


s = Stack()
print(s.is_empty())
s.push(3)
s.push('two')
s.pop()
s.push(True)
s.is_empty()
s.peek()
print(s.size())
s.print_items()
print(s.is_empty())

