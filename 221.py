class Solution:
    def maximalSquare(self, matrix) -> int:
        # dp improve
        if not len(matrix):
            return 0
        height, width = len(matrix), len(matrix[0])
        dp = [0 for _ in range(width + 1)]
        ans = temp = 0
        for i in range(height):
            for j in range(width):
                pre = dp[j + 1]
                if matrix[i][j] == '1':
                    dp[j + 1] = min(temp, dp[j], dp[j + 1]) + 1
                    ans = max(ans, dp[j + 1])
                else:
                    dp[j + 1] = 0
                temp = pre
            temp = 0
        return ans ** 2


print(Solution().maximalSquare([["1", "0", "1", "1", "1"],
                                ["0", "1", "0", "1", "0"],
                                ["1", "1", "0", "1", "1"],
                                ["1", "1", "0", "1", "1"],
                                ["0", "1", "1", "1", "1"]]))
# dp
# height = len(matrix)
# if not height:
#     return 0
# width = len(matrix[0])
# ans = 0
# dp = [[0 for _ in range(width + 1)] for _ in range(height + 1)]
# for i in range(height):
#     for j in range(width):
#         if matrix[i][j] == '1':
#             dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j], dp[i][j]) + 1
#             ans = max(dp[i + 1][j + 1], ans)
# return ans**2
