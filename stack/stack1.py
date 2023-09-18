class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        if(self.top):
            return self.top.value
        return None

    
    def push(self, nodeValue):
        newNode = Node(nodeValue)
        if(self.length == 0):
            self.top = newNode
            self.bottom = newNode
            self.length += 1
        else:
            oldNode = self.top
            self.top = newNode
            newNode.next = oldNode
            self.length += 1

    def pop(self):
        if(self.length==0):
            return "Cannot pop. stack is empty!!"
        

        else:
            popNode = self.top.value
            self.top = self.top.next
            self.length -= 1
            return popNode

    




s1 = Stack()
print(s1.length)
print('Adding new Node...')
s1.push(5)
print("top = ",s1.peek())

print("length = ",s1.length)
print('Adding new Node...')
s1.push(10)
print("top = ",s1.peek())
print("length = ",s1.length)
print('Adding new Node...')
s1.push(100)
print("top = ",s1.peek())
print("length = ",s1.length)
print("Popping node")
print(s1.pop())
print("top = ",s1.peek())
print("length = ",s1.length)
print("Popping node")
print(s1.pop())
print("top = ",s1.peek())
print("length = ",s1.length)
print("Popping node")
print(s1.pop())
print("top = ",s1.peek())
print("length = ",s1.length)
print("Popping node")
print(s1.pop())
print("top = ",s1.peek())
print("length = ",s1.length)





