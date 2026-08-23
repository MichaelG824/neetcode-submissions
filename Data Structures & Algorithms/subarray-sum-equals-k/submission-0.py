class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Brute Force: [2, -1, 1, 2]
        [2, ]

        """
        res = 0
        prefix_sum = 0
        d = {
            0: 1
        }

        for num in nums:
            prefix_sum += num
            diff = prefix_sum - k
            if diff in d:
                res += d[diff]
            if prefix_sum in d:
                d[prefix_sum] += 1 
            else:
                d[prefix_sum] = 1

        return res