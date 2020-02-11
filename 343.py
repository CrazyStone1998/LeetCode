class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        n3 = n // 3
        mod3 = n % 3
        if mod3 == 1:
            return 3 ** (n3 - 1) * 4
        elif mod3 == 2:
            return 3 ** n3 * 2
        else:
            return 3 ** n3
