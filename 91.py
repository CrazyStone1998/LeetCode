class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0
        if len(s) == 1: return 1
        n0 = 1
        if s[1] == '0':
            if ord(s[0]) > ord('2'):
                return 0
            else: n1 = 1
        else:
            n1 = 2 if s[0] == '1' or (s[0] == '2' and ord(s[1]) < ord('7')) else 1

        for i in range(2, len(s)):
            if s[i] == '0' and s[i - 1] != '1' and s[i - 1] != '2':
                return 0
            elif s[i] == '0' and (s[i - 1] == '1' or s[i - 1] == '2'):
                temp = n0
            elif s[i - 1] == '1' or (s[i - 1] == '2' and ord(s[i]) < ord('7')):
                temp = n0 + n1
            else:
                temp = n1
            n0, n1 = n1, temp
        return n1


    # if s[0] == '0':
    #     return 0
    # if len(s) == 1:
    #     return 1
    # dp = [0 for i in range(len(s))]
    # dp[0] = 1
    # if s[1] == '0':
    #     if s[0] == '1' or s[0] == '2':
    #         dp[1] = 1
    #     else:
    #         return 0
    # else:
    #     if s[0] == '1' or (s[0] == '2' and ord(s[1]) < ord('7')):
    #         dp[1] = 2
    #     else:
    #         dp[1] = 1
    #
    # for i in range(2,len(s)):
    #     if s[i] == '0':
    #         if s[i-1] == '1' or (s[i-1] == '2' and ord(s[i]) < ord('7')):
    #             dp[i] = dp[i-2]
    #         else:
    #             return 0
    #     else:
    #         if s[i-1] == '0':
    #             dp[i] = dp[i-1]
    #         elif s[i-1] == '1' or (s[i-1] == '2' and ord(s[i]) < ord('7')):
    #             dp[i] = dp[i-1]+dp[i-2]
    #         else:
    #             dp[i] = dp[i-1]
    # return dp[-1]


print(Solution().numDecodings('12'))
