class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        [0,0,0]
        O()
        []
        [1, 2, 3]
        []
        """

        # change all to 0s 
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 > val or val > len(nums):
                continue
            if nums[val - 1] == 0:
                nums[val - 1] = -1 * (len(nums) + 1) 
            elif nums[val - 1] > 0:
                nums[val - 1] *= -1
        
        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i
        return len(nums) + 1