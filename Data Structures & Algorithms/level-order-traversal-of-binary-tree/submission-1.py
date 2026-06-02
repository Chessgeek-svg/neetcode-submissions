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

        nodeQueue = deque()
        nextQueue = deque()
        nodeQueue.append(root)

        res = []
        level = []
        while True:
            while nodeQueue:
                node = nodeQueue.popleft()
                if node:
                    level.append(node.val)
                    nextQueue.append(node.left)
                    nextQueue.append(node.right)
            if level:
                res.append(level)
                level = []
            nodeQueue = copy.deepcopy(nextQueue)
            nextQueue.clear()
            if len(nodeQueue) == 0:
                break
        
        return res