class Solution(object):
    def countPalindromicSubsequences(self, S):
        mask = 10 ** 9 + 7
        length = len(S)
        arr = [ord(i) - ord('a') for i in S]
        mat = [[[0 for _ in range(length)] for _ in range(length)] for _ in range(4)]
        for i in range(length - 1, -1, -1):
            for j in range(i, length):
                for k in range(4):
                    if i == j:
                        mat[k][i][j] = 1 if arr[i] == k else 0
                    else:
                        if arr[i] != k:
                            mat[k][i][j] = mat[k][i + 1][j]
                        elif arr[j] != k:
                            mat[k][i][j] = mat[k][i][j - 1]
                        else:
                            # arr[i] == arr[j] == k
                            if i + 1 == j:
                                mat[k][i][j] = 2
                            else:
                                mat[k][i][j] = 2
                                for e in range(4):
                                    mat[k][i][j] += mat[e][i + 1][j - 1]
        return (mat[0][0][length - 1] + mat[1][0][length - 1] + mat[2][0][length - 1] + mat[3][0][length - 1]) % mask


print(Solution().countPalindromicSubsequences('a'))
