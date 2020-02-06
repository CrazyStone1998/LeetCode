class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0x100000000
        MAX_INT = 0x7FFFFFFF
        MIN_INT = MAX_INT+1
        while b != 0:
            a, b = (a ^ b) % mask, ((a & b) << 1) % mask
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)

print(Solution().getSum(-1, -6))
