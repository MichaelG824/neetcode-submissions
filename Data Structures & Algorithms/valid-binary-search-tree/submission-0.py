# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.is_valid = True
        self.curr_val = None
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(r):
            if not r:
                return
            dfs(r.left)
            if self.curr_val is None:
                self.curr_val = r.val
            else:
                if r.val <= self.curr_val:
                    self.is_valid = False
                self.curr_val = r.val
            dfs(r.right)
        dfs(root)
        return self.is_valid

