class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        cache = {}
        def lis_starting_at(i):
            if i in cache:
                return cache[i]
            best = 1                                   # nums[i] alone
            for r in range(i + 1, len(nums)):
                if nums[r] > nums[i]:
                    best = max(best, 1 + lis_starting_at(r))
            cache[i] = best
            return best
        return max(lis_starting_at(i) for i in range(len(nums)))