#DFS method
from collections import deque, defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for dest,src in prerequisites:
            graph[src].append(dest)

        visited = [0]*numCourses

        def dfs(course):
            if visited[course] ==1:
                return False
            if visited[course] ==2:
                return True
            visited[course] =1
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            visited[course] =2
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
