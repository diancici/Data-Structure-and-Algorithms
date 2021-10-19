# Directed Graph

# Adjacency list
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list) # Node1: [Node2, Node3]
        
    # Add a relation/an edge between two nodes node1 -> node2
    def insertEdge(self, v1, v2):
        self.graph[v1].append(v2)
        #self.graph[v2].append(v1) # undirected graph implementation
        
    # Print the graph
    def printGraph(self):
        for k, v in self.graph.items():
            print(k, '->', *v)
g = Graph()
# Create 1->5->2->7->1
g.insertEdge(1,5)
g.insertEdge(5,2)
g.insertEdge(2,7)
g.insertEdge(7,1)

g.printGraph()


# Adjacency Matrix
class Graph:
    def __init__(self, numberOfNodes):
        self.numberOfNodes = numberOfNodes + 1
        self.graph = [[0 for x in range(self.numberOfNodes)] 
                       for y in range(self.numberOfNodes)]
        
     # check if node exceed the limit of the graph matrix   
    def withInBound(self, v1, v2):
        return (v1>=0 and v1 < self.numberOfNodes) and (v2 >=0 and v2 < self.numberOfNodes)
    
    def insertEdge(self, v1, v2):
        if (self.withInBound(v1,v2)):
            self.graph[v1][v2] = 1
            #self.graph[v2][v1] = 1 # undirected graph implementation
            
    def printGraph(self):
        for i in range(self.numberOfNodes):
            for j in range(self.numberOfNodes):
                if(self.graph[i][j]):
                    print(i,"->",j)
g = Graph(5)
g.insertEdge(1,2)
g.insertEdge(2,3)
g.insertEdge(4,5)
g.printGraph()