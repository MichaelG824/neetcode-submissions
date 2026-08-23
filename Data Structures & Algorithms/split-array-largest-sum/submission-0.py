class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # [2, 4, 10, 1, 5]

        def number_of_pieces(capacity):
            sub_arrays = 0
            temp_sum = 0
            for n in nums:
                if temp_sum + n > capacity:
                    sub_arrays += 1
                    temp_sum = n
                else:
                    temp_sum += n
            return sub_arrays + 1
        res = sum(nums)
        l = max(nums)
        r = sum(nums)

        while l <= r:
            mid = (l + r) // 2
            print(mid)
            if number_of_pieces(mid) <= k:
                res = mid 
                r = mid - 1
            else:
                l = mid + 1
        return res