class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        total_nodes_visited = 0
        visited = set()
        adj = [[] for _ in range(n)]
        
        def dfs(node, parent):
            nonlocal total_nodes_visited
            if node in visited:
                return False
            
            total_nodes_visited += 1
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
            
            return True



        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        return dfs(0, -1) and total_nodes_visited == n