from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def insertEdge(self, v1, v2):
        self.graph[v1].append(v2)
        
    def BFS(self, startNode):
        queue = []
        queue.append(startNode)
        
        visited = set()
        
        while(queue):
            v = queue.pop(0)
            print("current node: ", v)
            visited.add(v)
            
            for node in self.graph[v]:
                if (node not in visited):
                    queue.append(node)

g = Graph()
g.insertEdge(2,1)
g.insertEdge(2,5)
g.insertEdge(1,11)
g.insertEdge(1,10)
g.insertEdge(5,6)
g.insertEdge(5,8)

g.BFS(2)