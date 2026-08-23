class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dfs(curr_sum):
            if curr_sum > target:
                return 0
            if curr_sum == target:
                return 1
            return sum(dfs(curr_sum + n) for n in nums)

        return dfs(0)
        
        