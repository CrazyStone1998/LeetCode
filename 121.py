class Solution:
    def maxProfit(self, prices) -> int:
        if not prices:
            return 0
        pre = prices[0]
        ans = 0
        for i in prices:
            if i < pre:
                pre = i
            else:
                ans = max(ans, i - pre)
        return ans
