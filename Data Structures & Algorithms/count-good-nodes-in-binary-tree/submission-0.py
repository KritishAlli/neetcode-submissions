# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.path(root, root.val)
        
    def path(self, root, maxVal):
        if not root:
            return 0

        if root.val >= maxVal:
            return (1 + self.path(root.left, root.val) + self.path(root.right, root.val))
        else:
            return (self.path(root.left, maxVal) + self.path(root.right, maxVal))