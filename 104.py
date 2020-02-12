# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root) -> int:
        def recursion(root):
            if root is None:
                return 0
            return max(recursion(root.left), recursion(root.right)) + 1
        return recursion(root)

