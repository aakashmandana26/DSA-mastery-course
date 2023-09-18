class Graph:
    def __init__(self):
        self.numberOfNodes = 0
        self.adjacencyList = {}

    def addVertex(self,node):
        if(node in self.adjacencyList.keys()):
            print("Given node was already present!")
        else:
            self.adjacencyList[node] = []
            self.numberOfNodes += 1

    def addEdge(self,node1, node2):
        if(node1 in self.adjacencyList.keys() and node2 in self.adjacencyList.keys()):
            self.adjacencyList[node1] += node2
            self.adjacencyList[node2] += node1
        else:
            print("Given vertices not present")

    def showConnections(self):
        for key in self.adjacencyList.keys():
            print(key,"-->",self.adjacencyList[key])


myGraph = Graph()
myGraph.addVertex('0')
myGraph.addVertex('1')
print(myGraph.numberOfNodes)
print(myGraph.adjacencyList)
myGraph.addEdge('0','1')
print(myGraph.adjacencyList)
myGraph.addEdge('0','2')
myGraph.addVertex('2')
myGraph.addEdge('0','2')
print(myGraph.adjacencyList)
myGraph.showConnections()


