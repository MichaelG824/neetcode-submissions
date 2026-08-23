class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        mid = -1
        while left <= right:
            mid = (left + right) // 2
            print("MId", mid)
            if matrix[mid][0] <= target and matrix[mid][len(matrix[0]) - 1] >= target:
                break
            elif matrix[mid][0] > target:
                print("Hit left", matrix[mid][0])
                right = mid - 1
            else:
                left = mid + 1
        if mid == -1:
            return False
        
        left = 0
        right = len(matrix[0]) - 1
        print("Hit", mid)
        while left <= right:
            col_mid = (left + right) // 2
            if matrix[mid][col_mid] == target:
                return True
            elif matrix[mid][col_mid] > target:
                right = col_mid - 1
            else:
                left = col_mid + 1
        return False