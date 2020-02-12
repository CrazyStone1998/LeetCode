class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        sign = 1 if n > 0 else -1
        n = abs(n)
        times = ans = 1
        temp = x
        while n != 0:
            if times * 2 <= n:
                temp *= temp
                times += times
            else:
                n -= times
                ans *= temp
                temp = x
                times = 1
        ans = 1/ans if sign < 0 else ans
        return ans