class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        
        """
        i = 0
        j = len(heights) - 1
        max_area = 0
        while i < j:
            max_area = max(min(heights[i], heights[j]) * (j - i), max_area)
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        return max_area
