# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def recursion(node):
            if not node:
                return 0
            left = recursion(node.left)
            right = recursion(node.right)
            if left < 0 or right < 0 or abs(left - right) > 1:
                return -1
            else:
                return 1 + max(left, right)

        result = recursion(root)
        return result >= 0