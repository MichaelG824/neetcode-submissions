class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0   
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            print("L, R", l, r)
            print("Mid: ", mid)
            # Left side is sorted
            if nums[l] <= nums[mid]:
                if nums[mid] < target or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right side is sorted
            else:
                if nums[mid] > target or nums[r] < target:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1 
