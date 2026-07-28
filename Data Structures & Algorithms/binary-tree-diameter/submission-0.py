# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftdepth = self.dfs(root.left)
        rightdepth = self.dfs(root.right)

        return max(leftdepth + rightdepth, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
    def dfs(self, root):
        if not root:
            return 0
        return 1 + max(self.dfs(root.left), self.dfs(root.right))