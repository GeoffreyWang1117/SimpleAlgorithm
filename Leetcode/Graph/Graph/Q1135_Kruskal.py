#这一题是一道典型的MST问题，可以用Kruskal算法解决
'''
To solve this problem of finding the minimum cost to connect all cities, we can use Kruskal's algorithm to find the Minimum Spanning Tree (MST). Here is a step-by-step approach to implement this in Python:

Sort the connections by their cost in ascending order.
Initialize Union-Find (Disjoint Set Union) to keep track of which nodes are connected.
Iterate through the sorted connections and add edges to the MST if they connect two different components.
Check if all nodes are connected after processing all possible edges.
Return the cost of the MST if all nodes are connected, otherwise return -1.
'''
class UnionFind:
    def __init__(self,n):
        self.parent=list(range(n))
        self.rank=[1]*n
    
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX]>self.rank[rootY]:
                self.parent[rootY]=rootX
            elif self.rank[rootX]<self.rank[rootY]:
                self.parent[rootX]=rootY
            else:
                self.parent[rootY]=rootX
                self.rank[rootX]+=1
            return True
        return False


class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        uf=UnionFind(n)
        connections.sort(key= lambda x:x[2])
        total_cost=0
        edges_used=0

        for x,y,cost in connections:
            if uf.union(x-1,y-1):
                total_cost += cost
                edges_used += 1
                if edges_used == n-1:
                    return total_cost
    
        return -1
