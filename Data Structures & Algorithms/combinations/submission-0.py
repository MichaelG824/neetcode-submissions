class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(start, curr):
            if len(curr) == k:
                res.append(curr.copy())
                return
            for num in range(start, n + 1):
                curr.append(num)
                dfs(num + 1, curr)
                curr.pop()
        
        dfs(1, [])
        return res