#detect if there exists a cycle in the graph
#Use topological sorting

from collections import deque,defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #create an adjacency list
        graph = defaultdict(list)
        in_degree = [0]*numCourses

        for dest,src in prerequisites:
            graph[src].append(dest)
            in_degree[dest] += 1

        #Initialize queue with nodes havinng zero in-degree
        queue = deque([i for i in range(numCourses) if in_degree[i]==0])
        visited_courses = 0

        while queue:
            course = queue.popleft()
            visited_courses+=1
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return visited_courses == numCourses
