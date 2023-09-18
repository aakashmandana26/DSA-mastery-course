class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def printLL(self):
        while self:
            print(self.value, end = "-->")
            self = self.next


head = LinkedList(5)
tail = LinkedList(10)
head.next = tail
head.printLL()