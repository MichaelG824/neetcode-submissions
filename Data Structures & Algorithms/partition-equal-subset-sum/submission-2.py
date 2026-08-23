class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        n = len(nums)

        # dp[i][s] = True if we can form sum s using nums[i:]
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        dp[n][0] = True   # with no elements, we can only achieve sum 0

        # Fill from bottom (i = n-1 down to 0)
        for i in range(n - 1, -1, -1):
            for s in range(target + 1):
                # Option 1: skip nums[i]
                dp[i][s] = dp[i + 1][s]
                # Option 2: take nums[i] (if it fits)
                if s >= nums[i]:
                    dp[i][s] = dp[i][s] or dp[i + 1][s - nums[i]]

        return dp[0][target]
            
