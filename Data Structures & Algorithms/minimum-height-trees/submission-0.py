class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        edge_cnt = {}
        leaves = deque()

        for src, neighbors in adj.items():
            edge_cnt[src] = len(neighbors)
            if len(neighbors) == 1:
                leaves.append(src)
        
        while leaves:
            if n <= 2:
                return list(leaves)
            for _ in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for neighbor in adj[node]:
                    edge_cnt[neighbor] -= 1
                    if edge_cnt[neighbor] == 1:
                        leaves.append(neighbor)
