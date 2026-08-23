class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(l, r):
            l_i = 0
            r_i = 0
            res = []
            while l_i < len(l) or r_i < len(r):
                if l_i < len(l) and r_i < len(r):
                    if l[l_i] < r[r_i]:
                        res.append(l[l_i])
                        l_i += 1
                    else:
                        res.append(r[r_i])
                        r_i += 1
                elif l_i < len(l):
                    res.append(l[l_i])
                    l_i += 1
                else:
                    res.append(r[r_i])
                    r_i += 1
            return res

        if len(nums) > 1:
            mid = len(nums) // 2
            l = self.sortArray(nums[:mid])
            r = self.sortArray(nums[mid:])
            return merge(l, r)
        return nums