# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDepth = 0
        def search(node):
            nonlocal maxDepth

            if not node:
                return 0
            
            left = search(node.left)
            right = search(node.right)

            maxDepth = max(maxDepth, left + right)

            return max(left, right) + 1


        if root:
            search(root)
        return maxDepth