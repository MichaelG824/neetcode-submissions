class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """

        """
        cache = {}

        def dfs(i, curr_val):
            if (i, curr_val) in cache:
                return cache[(i, curr_val)]
            if i >= len(nums):
                return False
            if curr_val == 0:
                return True
            cache[(i, curr_val)] = dfs(i + 1, curr_val) or dfs(i + 1, curr_val - nums[i])
            return cache[(i, curr_val)]
        
        return dfs(0, sum(nums)/2)
            
