# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append((float("-inf"), root, float("inf")))
        while queue:
            left, node, right = queue.popleft()
            if not (left < node.val < right):
                return False
            if node.left:
                queue.append((left, node.left, node.val))
            if node.right:
                queue.append((node.val, node.right, right))
        return True

