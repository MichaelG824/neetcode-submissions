class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if (k % len(nums)) == 0:
            return 
        k %= (len(nums))
        # [8, 7, 6, 5, 4, 3, 2, 1]
        def reverse(i, j, k):
            tot = 0
            r_len = (j - i) // 2
            while tot < r_len:
                nums[i], nums[j - 1] = nums[j - 1], nums[i]
                i += 1
                j -= 1  
                tot += 1

        reverse(0, len(nums), k)
        reverse(0, k, k)
        reverse(k, len(nums), k)
        
        

