from collections import deque
# append, popleft
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        if not root:
            return out
        q = deque([[root, 1]])
        max_level = 0
        while q:
            qlen = len(q)
            for i in range(qlen):
                cur = q.popleft()
                if cur[1] > max_level:
                    out.append(cur[0].val)
                    max_level = cur[1]
                if cur[0].right:
                    q.append([cur[0].right, cur[1] + 1])
                if cur[0].left:
                    q.append([cur[0].left, cur[1] + 1])
        return out

    