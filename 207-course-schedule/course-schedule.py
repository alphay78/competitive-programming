class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(numCourses)]
        indegree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        level = [i for i in range(numCourses) if indegree[i] == 0]
        taken_course = 0

        while level:
            next_level = []
            for node in level:
                taken_course += 1
                for adj in graph[node]:
                    indegree[adj] -= 1
                    if indegree[adj] == 0:
                        next_level.append(adj)
            level = next_level

        return numCourses == taken_course


