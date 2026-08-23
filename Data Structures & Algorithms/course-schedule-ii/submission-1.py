class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        
        q = deque()

        for pre, dest in prerequisites:
            indegree[pre] += 1
            adj[dest].append(pre)
        total = 0
        res = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        # [[0, 1], [1, 0]]
        while q:
            node = q.popleft()
            res.append(node)
            total += 1
            for val in adj[node]:
                indegree[val] -= 1
                if indegree[val] == 0:
                    q.append(val)
        return res if total == numCourses else []