# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rob(self, root) -> int:
        def recursion(root, dp):
            if not root:
                return 0
            if dp.get(root, None):
                return dp.get(root)
            dp[root] = root.val
            if root.left:
                dp[root] += dp[root.left.left] if dp.get(root.left.left, None) else recursion(root.left.left, dp) \
                                                                                    + dp[root.left.right] if dp.get(
                    root.left.right, None) else recursion(root.left.right, dp)
            if root.right:
                dp[root] += dp[root.right.left] if dp.get(root.right.left, None) else recursion(root.right.left, dp) \
                                                                                      + dp[root.right.right] if dp.get(
                    root.right.right, None) else recursion(root.right.right, dp)

            dp[root] = max(dp[root], dp[root.right] if dp.get(root.right, None) else recursion(root.right)
                                                                                     + dp[root.left] if dp.get(
                root.left, None) else recursion(root.left, dp))
            return dp[root]

        recursion(root, {})
# class Solution:
#     def rob(self, root) -> int:
#
#         def recursion(root):
#             if not root: return 0
#             ans = root.val
#             if root.left:
#                 ans += recursion(root.left.left) + recursion(root.left.right)
#             if root.right:
#                 ans += recursion(root.right.left) + recursion(root.right.right)
#             return max(ans, recursion(root.left) + recursion(root.right))
#         return recursion(root)
#
