# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.val = 0
        self.r_val = -1
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(r):
            if not r:
                return
            dfs(r.left)
            if k == self.val:
                return
            self.val += 1
            if k == self.val:
                self.r_val = r.val
                return
            dfs(r.right)
        dfs(root)
        return self.r_val