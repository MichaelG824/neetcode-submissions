class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 1 -> 
        # 1 -> 3 -> 3 
        slow_index = 0
        fast_index = 0
        while True:
            slow_index = nums[slow_index]
            fast_index = nums[nums[fast_index]]
            if slow_index == fast_index:
                break
        new_index = 0

        while True:
            slow_index = nums[slow_index]
            new_index = nums[new_index]
            if slow_index == new_index:
                return new_index