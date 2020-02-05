# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root, k: int) -> bool:
        d = {}
        return self.pre_order(root, d, k)

    def pre_order(self, root, d, k):
        if root:
            if d.get(k - root.val, None):
                return True
            d[root.val] = 1
            if self.pre_order(root.left, d, k):
                return True
            if self.pre_order(root.right, d, k):
                return True

        return False
