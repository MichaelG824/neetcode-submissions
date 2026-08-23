class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        total = 0
        def dfs(i, j):
            if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1 or grid[i][j] != 1:
                return
            nonlocal total
            temp_add = 4
            print(grid)
            grid[i][j] = 2
            if i - 1 >= 0 and grid[i - 1][j] != 0:
                temp_add -= 1
            if j - 1 >= 0 and grid[i][j - 1] != 0:
                temp_add -= 1
            if j + 1 < len(grid[0]) and grid[i][j + 1] != 0:
                temp_add -= 1
            if i + 1 < len(grid) and grid[i + 1][j] != 0:
                temp_add -= 1
            total += temp_add
            
            dfs(i - 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
            dfs(i + 1, j)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i, j)
        return total