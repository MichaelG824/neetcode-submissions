class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window_sum = 0
        min_window_length = float("inf")
        j = 0
        i = 0
        
        while j < len(nums):
            window_sum += nums[j]
            while window_sum >= target:
                min_window_length = min(min_window_length, j - i + 1)
                window_sum -= nums[i]
                i += 1
            j += 1    
        return 0 if min_window_length == float("inf") else min_window_length   

