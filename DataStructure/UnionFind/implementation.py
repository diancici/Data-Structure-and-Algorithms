# Union-Find : for dynamic connectivity problems
class UF:
    def __init__(self, n: int):
        self.count = n # number of components
        self.id = [i for i in range(n)]   # array of component id(root node) for each site(node)
        self.size = [i for i in range(n)] # number of child nodes for each site(node) + itself(root)

    """ Return the number of components """
    def countN(self):
        return self.count

    """ Determine if site p and site q has already been connected """
    def connected(self, p: int, q: int):
        return self.find(p) == self.find(q)   

    """ Return the id of site p """
    ## Solution 1 – quick find: not in use for large problems
    # T(n) = n for union()
    # def find(self, p):
    #     return self.id[p] # id represent the root directly

    # ## connnect p and q if they are not connected
    # def union(self, p, q):
    #     pID = self.find(p)
    #     qID = self.find(q)
    #     # nothing to do if p and q are already in the same component
    #     if pID == qID: return
    #     # If not, change values from id[p] to id[q]
    #     for i in range(len(self.id)):
    #         if id[i] == pID:
    #             id[i] == qID
    #     self.count -= 1

    ## Solution 2 – quick union: id[] represent the parent node, root's parent is root itself
    # T(n) = tree height for union and find
    # def find(self, p: int):
    #     while p != self.id[p]:
    #         p = self.id[p]
    #     return p
    
    # def union(self, p, q):
    #     pRoot = self.find(p)
    #     qRoot = self.find(q)
    #     if pRoot == qRoot: return
    #     self.id[pRoot] = qRoot # make the root of q as the parent of p's root
    #     self.count -= 1

    ## Solution 3 - Union-find: weighted quick-union (logN)
    # T(n) = logN : possible be used in large problems
    def find(self, p: int):
        while p != self.id[p]:
            self.id[p] = self.id[self.id[p]] ## Solution 3 Optimal: Path pression
            p = self.id[p]
        return p
    
    def union(self, p: int, q: int):
        pRoot = self.find(p)
        qRoot = self.find(q)
        if pRoot == qRoot: return
        # Make smaller tree's root link to larger tree
        if self.size[pRoot] < self.size[qRoot]:
            self.id[pRoot] = qRoot
            self.size[qRoot] += self.size[pRoot]
        else:
            self.id[qRoot] = pRoot
            self.size[pRoot] += self.size[qRoot]
        self.count -= 1


if __name__ == "__main__":
    with open("/Users/chendian/Downloads/algs4-data/largeUF.txt") as f:
        n = int(f.readline())
        uf = UF(n)
        for line in f:
            line = line.split()
            p = int(line[0])
            q = int(line[1])
            if uf.connected(p, q): continue
            uf.union(p, q)
            print("{} {}".format(p, q))
        print("{} trees".format(uf.countN()))
