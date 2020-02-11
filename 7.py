class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        x = abs(x)
        x_reverse = 0
        while x > 0:
            x_reverse = x_reverse * 10 + x % 10
            x //= 10
        x_reverse *= sign
        if x_reverse < -2 ** 31 or x_reverse >= 2 ** 31:
            return 0
        return x_reverse
