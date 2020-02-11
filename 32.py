class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # dp
        if len(s) < 2:
            return 0
        dp = [0 for _ in range(len(s))]
        dp[1] = 2 if s[0] == '(' and s[1] == ')' else 0
        ans = dp[1]
        for i in range(2, len(s)):
            if s[i] == ')' and s[i - 1] == '(':
                dp[i] = dp[i - 2] + 2
            if s[i] == ')' and s[i - 1] == ')' and i - dp[i - 1] - 1 > -1 and s[i - dp[i - 1] - 1] == '(':
                dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
            ans = max(dp[i], ans)
        return ans
        # stack
        # stack = [-1, ]
        # ans = 0
        # for i in range(len(s)):
        #     if s[i] == '(':
        #         stack.append(i)
        #     else:
        #         stack.pop()
        #         if not stack:
        #             stack.append(i)
        #         else:
        #             ans = max(ans, i - stack[-1] + 1)
        # return ans


print(Solution().longestValidParentheses("(()))())("))
