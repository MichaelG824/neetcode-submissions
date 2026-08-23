class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        1 1 0
        0 2 2
        0 2 2
        """
        q = deque()
        # Go through each square and get rotten fruit
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
        res = -1
        # Go through each value in queue up to length of what was in the queue
        while len(q):
            total = len(q)
            print("Total, Res size", total, res)
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for _ in range(total):
                c, r = q.popleft()
                for dc, dr in directions:
                    row = r + dr 
                    col = c + dc
                    if row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col] == 1:
                        print("Res: ", res, row, col)
                        q.append((row, col))
                        grid[row][col] = 2
            res += 1
            print("Outside Res", res)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return 0 if res == -1 else res