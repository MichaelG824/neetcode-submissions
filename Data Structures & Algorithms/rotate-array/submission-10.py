class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return
        def reverse(l, r):
            while l < r:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                r -= 1
                l += 1 
        tot = k % len(nums)
        reverse(0, len(nums) - 1)
        reverse(0, tot - 1)
        reverse(tot, len(nums) - 1)
        
        
        

