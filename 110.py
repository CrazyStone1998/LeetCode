# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root) -> bool:
        def getHeight(root):
            if root is None:
                return 0
            return max(getHeight(root.left), getHeight((root.right))) + 1

        def is_balanced(root):
            if root is None:
                return True
            if abs(getHeight(root.left) - getHeight(root.right)) < 2:
                return is_balanced(root.left) and is_balanced(root.right)
            return False
        return is_balanced(root)