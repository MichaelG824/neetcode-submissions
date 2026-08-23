class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        
        q = deque()

        for pre, dest in prerequisites:
            indegree[dest] += 1
            adj[pre].append(dest)
        total = 0
        
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        # [[0, 1], [1, 0]]

        while q:
            node = q.popleft()
            total += 1
            for val in adj[node]:
                indegree[val] -= 1
                if indegree[val] == 0:
                    q.append(val)
        return total == numCourses
                
