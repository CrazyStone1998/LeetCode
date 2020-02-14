class Solution:
    def change(self, amount: int, coins) -> int:
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1
        for i in coins:
            for j in range(j, amount + 1):
                dp[j] += dp[j - i]
        return dp[-1]


print(Solution().change(
    2,
    [1, 2, 5]))
