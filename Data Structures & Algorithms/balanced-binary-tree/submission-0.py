# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced = True
        def dfs(r):
            nonlocal is_balanced
            if r is None:
                return 0
            
            left = dfs(r.left)
            right = dfs(r.right)
            print(left, right)
            if abs(left - right) > 1:
                is_balanced = False
            return 1 + max(left, right)
        dfs(root)
        return is_balanced