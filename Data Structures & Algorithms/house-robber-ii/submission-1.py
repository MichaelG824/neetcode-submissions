class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        cache = {}
        def dfs(i, flag):
            if i >= len(nums) or (flag and i == len(nums) - 1):
                return 0
            if i in cache:
                return cache[i]
            cache[i] = max(dfs(i + 1, flag),
                       nums[i] + dfs(i + 2, flag or i == 0))
            return cache[i]
        val = dfs(0, True)
        cache = {}
        val_2 = dfs(1, False)
        return max(val, val_2)