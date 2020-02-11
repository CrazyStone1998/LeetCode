class Solution:
    def maximalRectangle(self, matrix) -> int:
        if not len(matrix):
            return 0
        height = len(matrix)
        width = len(matrix[0])
        dp = [[0 for _ in range(width + 1)] for _ in range(height)]
        for i in range(height):
            for j in range(width):
                if matrix[i][j] == '1':
                    dp[i][j + 1] = dp[i][j] + 1
        area = 0
        for i in range(height):
            for j in range(width):
                if matrix[i][j] == '1':
                    f, h, w = i, 0, dp[i][j + 1]
                    while f > -1 and dp[f][j + 1]:
                        h += 1
                        w = min(w, dp[f][j + 1])
                        f -= 1
                        area = max(area, h * w)
        return area


print(Solution().maximalRectangle(
    [["0", "1", "1", "0", "1"],
     ["1", "1", "0", "1", "0"],
     ["0", "1", "1", "1", "0"],
     ["1", "1", "1", "1", "0"],
     ["1", "1", "1", "1", "1"],
     ["0", "0", "0", "0", "0"]]))
