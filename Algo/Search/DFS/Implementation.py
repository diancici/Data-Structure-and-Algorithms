from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def insertEdge(self,v1,v2):
        self.graph[v1].append(v2)

    # DFS_iterative   
    def DFS(self, startNode):
        st = [] # Stack : save node has not been chosen 
        visited = set()
        st.append(startNode)
        
        while(st):
            cur = st[-1]
            st.pop()
            
            if (cur not in visited):
                print("current node: ",cur)
                visited.add(cur)
                
            for vertex in self.graph[cur]:
                if (vertex not in visited):
                    st.append(vertex)
                    print("st after every append: ", st)

    def DFS_recursive(self, root):
        visited = set()
        self.DFS_traverse(root, visited)
    
    def DFS_traverse(self, root, visited):
        # do something to the current node before move to next step
        print("current node: ", root)
        visited.add(root)

        # recur for all the child nodes which are not visited
        for child in self.graph[root]:
            if child not in visited:
                self.DFS_traverse(child, visited)

g = Graph()
g.insertEdge(2,1)
g.insertEdge(2,5)
g.insertEdge(5,1)
g.insertEdge(1,11)
g.insertEdge(1,10)
g.insertEdge(5,6)
g.insertEdge(5,8)

g.DFS(2)
#print("......................")
#g.DFS_recursive(2)     