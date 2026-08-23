class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1 for _ in range(n)]

    def find(self, node):
        curr = node
        while curr != self.parent[curr]:
            curr = self.parent[curr]
        return curr
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.rank[pv] > self.rank[pu]:
            pu, pv = pv, pu
        self.parent[pv] = self.parent[pu]
        self.rank[pu] += self.rank[pv]
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        d = DSU(len(edges) + 1)

        for u, v in edges:
            if not d.union(u, v):
                return [u, v]