# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        maxDepth = 0
        def dfs(root):
            if not root:
                return 0

            nonlocal maxDepth

            depth = 1 + max(dfs(root.left), dfs(root.right))
            maxDepth = max(maxDepth, depth)

            return depth
            
        dfs(root)
        return maxDepth