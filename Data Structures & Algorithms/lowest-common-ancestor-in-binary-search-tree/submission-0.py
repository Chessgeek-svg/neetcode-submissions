# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cache_p = []
        cache_q = []

        def binarySearch(root, target, cache):
            if root:
                cache.append(root)

                if target < root.val:
                    binarySearch(root.left, target, cache)
                elif target > root.val:
                    binarySearch(root.right, target, cache)
            
        binarySearch(root, p.val, cache_p)
        binarySearch(root, q.val, cache_q)

        for node in cache_p[::-1]:
            if node in set(cache_q):
                return node
