class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        [0, 0, 0]
        [-1, -2, 4]

        [-1, -2, -8, -4, -5, 7, -3]
        """
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <= len(nums):
                if nums[val - 1] > 0:
                    nums[val - 1] = -nums[val - 1]
            elif val == 0:
                nums[i] = len(nums) + 1
        print(nums)
        for i in range(1, len(nums) + 1):
            if nums[i - 1] > 0:
                return i
        return len(nums) + 1