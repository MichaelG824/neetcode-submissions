# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.good_nodes = 0
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(r, max_val):
            if not r:
                return
            if r.val >= max_val:
                max_val = r.val
                self.good_nodes += 1
            dfs(r.left, max_val)
            dfs(r.right, max_val)
        dfs(root, -1000)
        return self.good_nodes
        