'''
Depth-First Search (DFS) Approach
In this approach, we treat the matrix as an adjacency matrix of a graph and use DFS to explore all connected nodes starting from each unvisited node.

Here is the Python code using DFS:
'''
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def DFS(node):
            for neighbor,is_connected in enumerate(isConnected[node]):
                if is_connected and neighbor not in visited:
                    visited.add(neighbor)
                    DFS(neighbor)

        n=len(isConnected)
        visited = set()
        provinces =0

        for i in range(n):
            if i not in visited:
                DFS(i)
                provinces+=1

        return provinces
