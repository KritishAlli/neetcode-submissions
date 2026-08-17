from collections import deque
# append, popleft
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        out = []
        if not root:
            return out
        cur = []
        q = deque([root])
        while q:
            qlen = len(q)
            for i in range(qlen):
                node = q.popleft()
                cur.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                

            out.append(cur)
            cur = []
        return out


