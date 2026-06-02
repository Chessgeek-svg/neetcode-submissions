# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import copy
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        nodeQueue = []
        nodeQueue.append(root)

        res = []
        level = []
        while len(nodeQueue) > 0:
            for i in range(len(nodeQueue)):
                node = nodeQueue.pop(0)
                if node:
                    level.append(node.val)
                if node.left:
                    nodeQueue.append(node.left)
                if node.right:
                    nodeQueue.append(node.right)
            if level:
                res.append(level)
                level = []
        
        return res