class Solution:
    def countSquares(self, matrix) -> int:
        if not matrix:
            return 0
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 or j == 0:
                    ans += matrix[i][j]
                elif matrix[i][j] == 0:
                    ans += 0
                else:
                    matrix[i][j] = min(matrix[i - 1][j - 1], matrix[i][j - 1], matrix[i - 1][j]) + 1
                    ans += matrix[i][j]
        return ans
