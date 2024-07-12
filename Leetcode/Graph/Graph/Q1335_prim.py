'''
To solve this problem using Prim's algorithm, follow these steps:

Initialize a Min-Heap to always extend the MST with the smallest edge.
Start from an arbitrary node and push its edges into the heap.
Pop the smallest edge from the heap, add it to the MST if it connects a new node.
Push all edges of the newly added node that connect to unvisited nodes into the heap.
Repeat until all nodes are connected or the heap is empty.
Check if all nodes are connected and return the total cost if they are; otherwise, return -1.
'''
#The result is much slower than the Kruskal with UnionFind

import heapq
from collections import defaultdict

class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        #Create an  adjacent list
        graph = defaultdict(list)
        for x,y,cost in connections:
            graph[x].append((cost,y))
            graph[y].append((cost,x))

        #minheap to pick the smallest edge
        min_heap = [(0,1)]
        visited = set()
        total_cost =0

        while min_heap and len(visited)<n:
            cost,node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            total_cost+= cost
            for edge_cost,neighbor in graph[node]:
                if neighbor not in graph[node]:
                    heapq.heappush(min_heap,(edge_cost,neighbor))

        return total_cost if len(visited)==n else -1
