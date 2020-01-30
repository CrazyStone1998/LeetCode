class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        m = [[0 for _ in range(l)] for _ in range(l)]
        start, end = 0, 0
        for j in range(l):
            for i in range(j + 1):
                if s[i] == s[j]:
                    m[i][j] = 1 if j - i < 3 else m[i + 1][j - 1]
                if m[i][j] and j - i > end - start:
                    start = i
                    end = j
        return s[start:end + 1]
        # # 中心扩散
        # sl = list(s)
        # l = len(sl)
        # for i in range(1, l + 1):
        #     sl.insert(2 * i - 1, '#')
        # m = [1 for i in range(2 * l - 1)]
        #
        # for i in range(2 * l - 1):
        #     n = 1
        #     while i - n >= 0 and i + n < 2 * l - 1:
        #         if sl[i-n] == sl[i+n]:
        #             m[i] +=1
        #             n+=1
        #         else:
        #             break
        # return max(m)

Solution().longestPalindrome("babad")