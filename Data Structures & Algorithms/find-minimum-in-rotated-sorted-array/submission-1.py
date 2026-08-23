class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            print(l, r)
            print("--------")
            if mid < len(nums) - 1 and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            
            elif l == 0 and r == 0:
                return nums[0]
            elif nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1

        return nums[l]