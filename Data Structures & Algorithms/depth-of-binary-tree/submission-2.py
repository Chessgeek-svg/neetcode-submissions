# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math

class Solution:
    def maxDepth(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        depth = 1

        if node.left and node.right:
            return depth + max(self.maxDepth(node.left), self.maxDepth(node.right))
        elif node.left:
            return depth + self.maxDepth(node.left)
        elif node.right:
            return depth + self.maxDepth(node.right)
        
        return depth