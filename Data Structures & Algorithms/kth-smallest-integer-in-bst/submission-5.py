# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        count = 0
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            if not curr:
                curr = stack.pop()
            count += 1
            if count == k:
                return curr.val
            if curr.right:
                curr = curr.right
            else:
                curr = None
        return -1
