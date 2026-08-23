class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            best = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    best = max(best, 1 + dp[j])
            dp[i] = best
        return max(dp)