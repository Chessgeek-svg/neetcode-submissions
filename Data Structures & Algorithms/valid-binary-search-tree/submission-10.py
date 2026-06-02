# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checkValid(min, curr, max):
            if not curr:
                return True
            if not (min < curr.val < max):
                return False
            
            return (checkValid(min, curr.left, curr.val)\
                and checkValid(curr.val, curr.right, max))
        
        return checkValid(-1001, root, 1001)