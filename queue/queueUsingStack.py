class Stack:
    def __init__(self):
        self.stack = []
        self.length = 0

    def peek(self):
        return self.stack[0]
    
    def push(self, value):
        self.stack.append(value)
        self.length += 1

    def pop(self):
        ans = self.stack[0]
        self.stack.pop(0)
        self.length -= 1
        return ans

    
s1 = Stack()
s1.push(5)
print(s1.peek())
s1.push(15)
print(s1.peek())
print(s1.pop())
print(s1.peek())



