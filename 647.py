class Solution:
    def countSubstrings(self, s: str) -> int:
        l = len(s)

        m = [[0 for _ in range(l)] for _ in range(l)]

        for j in range(l):
            for i in range(j+1):
                if s[i] == s[j]:
                    m[i][j] = 1 if j-i<3 else m[i+1][j-1]
        return sum([sum(i) for i in m])
Solution().countSubstrings("abc")