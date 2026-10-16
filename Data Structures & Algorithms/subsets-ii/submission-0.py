class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # set of tuples 
        # and then convert to list 
        res = set()
        def backtrack(i, arr):
            res.add(tuple(sorted(arr)))
            for index in range(i, len(nums)):
                arr.append(nums[index])
                backtrack(index + 1, arr)
                arr.pop()
        backtrack(0, [])
        res = list(res)
        return res
        