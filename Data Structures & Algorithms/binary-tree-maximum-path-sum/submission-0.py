# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        globalMax = root.val

        def evaluatePath(node):
            if not node:
                return 0
            nonlocal globalMax

            leftPath = evaluatePath(node.left)
            rightPath = evaluatePath(node.right)
            pathMax = max(node.val, node.val + leftPath, node.val + rightPath)
            globalMax = max(globalMax, pathMax, node.val + leftPath + rightPath)

            return pathMax
            
        evaluatePath(root)
        return globalMax