'''
Union-Find (Disjoint Set Union) Approach
In this approach, we use a Union-Find data structure to group nodes into connected components.
'''

class UnionFind:
    def __init__(self,size):
        self.parent = list(range(size))
        self.rank = [1]* size
        self.count = size
    def find(self,node):
        if self.parent[node]!=node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    def union(self,node1,node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1!= root2:
            if self.rank[root1]>self.rank[root2]:
                self.parent[root2]=root1
            elif self.rank[root1]<self.rank[root2]:
                self.parent[root1]=root2
            else:
                self.parent[root2]=root1
                self.rank[root1]+=1
            self.count -=1

    def get_count(self):
        return self.count

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n= len (isConnected)
        uf= UnionFind(n)

        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j]==1:
                    uf.union(i,j)
        
        return uf.get_count()
