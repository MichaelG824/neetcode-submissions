class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        temp = 0
        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1:
                return
            nonlocal res
            nonlocal temp
            temp += 1
            res = max(res, temp)
            grid[i][j] = 2

            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                temp = 0
                if grid[i][j] == 1:
                    dfs(i, j)
        return res