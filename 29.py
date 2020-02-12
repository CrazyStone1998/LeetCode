class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = 0
        sign = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1
        dividend, divisor = abs(dividend), abs(divisor)
        times = [(divisor, 1), ]
        mask = 2
        for i in range(1, 31):
            mask += mask
            times.append((times[i - 1][0] + times[i - 1][0], times[i - 1][1] + times[i - 1][1]))
        divisor, pos = 0, 30
        while True:
            if divisor + times[pos][0] <= dividend:
                ans += times[pos][1]
                divisor += times[pos][0]
            else:
                if pos == 0:
                    ans *= sign
                    if ans > mask or ans <= -mask:
                        return mask-1
                    else:
                        return ans
                pos -= 1



print(Solution().divide(10, 3))
