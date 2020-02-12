class Solution:
    def mySqrt(self, x: int) -> int:
        if not x: return x
        left, right = 1, x
        while left < right - 1:
            mid = (left + right) // 2
            if mid * mid < x:
                left = mid
            elif mid * mid > x:
                right = mid
            else:
                return mid
        return left


print(Solution().mySqrt(8))
