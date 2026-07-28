# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class StackObject:
    def __init__(self, depth=0, node=None):
        self.depth = depth
        self.node = node


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        max_depth = 0
        s = []
        s.append(StackObject(1, root))
        while s:
            node = s.pop()
            if node.depth > max_depth:
                max_depth = node.depth
            
            cur_node = node.node

            if cur_node.left:
                s.append(StackObject(node.depth + 1, cur_node.left))
            if cur_node.right:
                s.append(StackObject(node.depth + 1, cur_node.right))
        return max_depth
