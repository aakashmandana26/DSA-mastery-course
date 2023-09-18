class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None


    def insert(self, nodeValue):
        newNode = Node(nodeValue)
        if(self.root is None):
            self.root = newNode
            return

        else:
            currentNode = self.root
            while(True):
                
                if(nodeValue < currentNode.value):
                    if(currentNode.left is None):
                        currentNode.left = newNode
                        return 
                    else:
                        currentNode = currentNode.left
                
                else:
                    if(currentNode.right is None):
                        currentNode.right = newNode
                        return 
                    else:
                        currentNode = currentNode.right

    def lookup(self, searchValue):
        if(self.root is None):
            return "Node not found!"

        else:
            currentNode = self.root
            while(currentNode):
                if(searchValue < currentNode.value):
                    currentNode = currentNode.left
                elif(searchValue > currentNode.value):
                    currentNode = currentNode.right
                else:
                    return "Node found!"
            
            return "Node not found!"

                


    def remove(self, nodeValue):
        if(self.root is None):
            return "Node not present!"
        else:
            currentNode = self.root
            while(currentNode):
                if(nodeValue < currentNode.value):
                    prevNode = currentNode
                    currentNode = currentNode.left
                elif(nodeValue > currentNode.value):
                    prevNode = currentNode
                    currentNode = currentNode.right
                elif(nodeValue == currentNode.value):
                    if(currentNode.left is None):
                        prevNode.right = currentNode.right
                        return "Node deleted"
                    elif(currentNode.right is None):
                        prevNode.left = currentNode.left
                        return "Node deleted"
                    else:
                        pass
                        

                        




                
            


t1 = BST()
t1.insert(50)
t1.insert(100)
t1.insert(30)
t1.insert(45)
print(t1.root.value)
print(t1.root.left.value)
print(t1.root.right.value)
print(t1.root.left.right.value)
print(t1.lookup(450))
print(t1.lookup(45))
print(t1.root.left.right.value)