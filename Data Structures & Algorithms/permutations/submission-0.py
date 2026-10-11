class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(path, visited):
            if len(path) == len(nums):
                res.append(list(path))
                return
            for i in range(len(nums)):
                if nums[i] not in visited:
                    # Include path
                    path.append(nums[i])
                    visited.add(nums[i])
                    dfs(path, visited)
                    # Do not include this in path
                    path.pop()
                    visited.remove(nums[i])
        dfs([], set())
        return res