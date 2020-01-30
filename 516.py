class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        l = len(s)
        m = [[0 for _ in range(l)] for _ in range(l)]
        for j in range(l):
            for i in range(j, -1, -1):
                if s[i] == s[j]:
                    m[i][j] = j - i + 1 if j - i < 3 else m[i + 1][j - 1] + 2
                else:
                    m[i][j] = max(m[i + 1][j], m[i][j - 1])
        return m[0][l-1]