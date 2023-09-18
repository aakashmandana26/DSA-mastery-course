class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        if(self.first):
            return (self.first.value, self.last.value)
        return None

    def enqueue(self, nodeValue):
        newNode = Node(nodeValue)
        if(self.first is None):
            self.first = newNode
            self.last = newNode
            self.length += 1

        else:
            oldNode = self.last
            oldNode.next = newNode
            self.last = newNode
            self.length += 1

    def deque(self):
        if(self.first is None):
            return "Cannot deque. Queue is empty!!"

        else:
            oldNode = self.first
            self.first = self.first.next
            self.length -= 1
            return oldNode.value


q1 = Queue()
q1.enqueue(5)
print(q1.peek())
q1.enqueue(10)
print(q1.peek())
q1.enqueue(15)
print(q1.peek())
print(q1.deque())
print(q1.peek())
print(q1.deque())
print(q1.peek())
print(q1.deque())
print(q1.peek())


