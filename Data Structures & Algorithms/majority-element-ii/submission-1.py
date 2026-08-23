class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1 = 0
        count2 = 0
        num1 = -1000000001
        num2 = -1000000001

        for num in nums:
            if num == num1:
                count1 += 1
            elif num == num2:
                count2 += 1
            elif count1 == 0:
                num1 = num
                count1 = 1
            elif count2 == 0:
                num2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        count1 = 0
        count2 = 0
        res = []
        hash_set = set()
        for num in nums:
            if num == num1 and num not in hash_set:
                count1 += 1
                if count1 > len(nums) // 3:
                    res.append(num)
                    hash_set.add(num)
            elif num == num2 and num not in hash_set:
                count2 += 1
                if count2 > len(nums) // 3:
                    res.append(num)
                    hash_set.add(num)
        return res



