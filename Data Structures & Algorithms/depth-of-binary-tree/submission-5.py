# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maximumDepth = 0

        def dfs(root):
            nonlocal maximumDepth

            if not root:
                return 0
            
            depth = 1 + max(dfs(root.left), dfs(root.right))

            maximumDepth = max(maximumDepth, depth)

            return depth

        dfs(root)
        return maximumDepth