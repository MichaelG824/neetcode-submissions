class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt1 = 0
        cnt2 = 0
        num1 = num2 = -1
        n = len(nums)
        for num in nums:
            if num1 == num:
                cnt1 += 1
            elif num2 == num:
                cnt2 += 1
            elif cnt1 == 0:
                num1 = num
                cnt1 = 1
            elif cnt2 == 0:
                num2 = num
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        res = []
        cnt1 = 0
        cnt2 = 0

        for num in nums:
            if num == num1:
                cnt1 += 1
            if num == num2:
                cnt2 += 1
        if cnt1 > n/3:
            res.append(num1)
        if cnt2 > n/3:
            res.append(num2)
        return res 

