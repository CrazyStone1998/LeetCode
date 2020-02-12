# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root) -> bool:
        if not root: return True
        def recursion(root1, root2):
            if root1 is None and root2 is None:
                return True
            elif root1 and root2:
                if root1.val == root2.val:
                    return recursion(root1.left, root2.right) and recursion(root1.right, root2.left)
            return False

        return recursion(root.left, root.right)
