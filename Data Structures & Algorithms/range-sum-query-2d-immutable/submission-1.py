class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROW_LENGTH = len(matrix)
        COL_LENGTH = len(matrix[0])
        self.new_matrix = [[0] * (COL_LENGTH + 1) for _ in range(ROW_LENGTH + 1)]
        for i in range(ROW_LENGTH):
            prefix = 0
            for j in range(COL_LENGTH):
                above = self.new_matrix[i][j + 1]
                prefix += matrix[i][j]
                self.new_matrix[i + 1][j + 1] = prefix + above
        print(self.new_matrix)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bottom_right = self.new_matrix[row2 + 1][col2 + 1] 
        bottom_left = self.new_matrix[row2 + 1][col1]
        top_right = self.new_matrix[row1][col2 + 1]
        above = self.new_matrix[row1][col1]
        return bottom_right - bottom_left - top_right + above


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)