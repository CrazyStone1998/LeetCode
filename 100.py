# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q) -> bool:
        def recursion(root1, root2):
            if root1 is None and root2 is None:
                return True
            elif root1 and root2:
                if root1.val == root2.val:
                    return recursion(root1.left, root2.left) and recursion(root1.right, root2.right)
            return False

        return recursion(p, q)
