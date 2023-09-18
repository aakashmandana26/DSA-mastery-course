class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None


    def insert(self,value):
        
        if(self.key is None):
            self.key = value
            return
            
        else:
            if(value < self.key):
                if(self.lchild is None):
                    self.lchild = BST(value)
                    return
                else:
                    self.lchild.insert(value)

            else:
                if(self.rchild is None):
                    self.rchild = BST(value)
                    return
                else:
                    self.rchild.insert(value)
                


t1 = BST(9)
t1.insert(6)
t1.insert(12)
t1.insert(1)
t1.insert(4)
t1.insert(34)
t1.insert(45)


