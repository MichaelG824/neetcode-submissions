# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = queue.Queue()
        q.put(root)
        res = []
        while q.qsize() > 0:
            q_len = q.qsize()
            tmp = []
            for _ in range(q_len):
                node = q.get()
                tmp.append(node.val)
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            res.append(tmp)

        return res

