from collections import deque 

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        q = deque()
        hash_set = set()

        def bfs(i, j):
            q.append((i, j, 0))

            while q:
                i, j, val = q.popleft()
                print(val)
                grid[i][j] = min(val, grid[i][j])
                if i - 1 >= 0 and grid[i - 1][j] != -1 and grid[i - 1][j] != 0 and (i - 1, j) not in hash_set:
                    hash_set.add((i - 1, j))
                    q.append((i - 1, j, val + 1))
                if i + 1 < len(grid) and grid[i + 1][j] != -1 and grid[i + 1][j] != 0 and (i + 1, j) not in hash_set:
                    hash_set.add((i + 1, j))
                    q.append((i + 1, j, val + 1))
                if j - 1 >= 0 and grid[i][j - 1] != -1 and grid[i][j - 1] != 0 and (i, j - 1) not in hash_set:
                    hash_set.add((i, j - 1))
                    q.append((i, j - 1, val + 1))
                if j + 1 < len(grid[0]) and grid[i][j + 1] != -1 and grid[i][j + 1] != 0 and (i, j + 1) not in hash_set:
                    hash_set.add((i, j + 1))
                    q.append((i, j + 1, val + 1))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    hash_set = set()
                    bfs(i, j)