# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []
        self.depthFirstSearch(root, values)
        print(values)
        return values[k-1]

    def depthFirstSearch(self, root: Optional[TreeNode], values: List[int]):
        if not root:
            return None

        self.depthFirstSearch(root.left, values)
        values.append(root.val)
        self.depthFirstSearch(root.right, values)
    
        