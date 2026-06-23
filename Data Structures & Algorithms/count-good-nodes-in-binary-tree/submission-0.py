# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = deque([(root, root.val)])
        print(q)
        good_counter = 0
        while q:
            node, path_max = q.popleft()
            if node.val >= path_max:
                good_counter += 1
            path_max = max(path_max, node.val)
            if node.left:
                q.append((node.left, path_max))
            if node.right:
                q.append((node.right, path_max))
        return good_counter