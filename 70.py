class Solution:
    num = 0

    def climbStairs(self, n: int) -> int:
        return self._dp(n)

    def _rs(self, n, ):
        if n == 0:
            self.num += 1
        elif n > 1:
            self._rs(n - 1)
            self._rs(n - 2)
        else:
            self._rs(n - 1)

    def _dp(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            solutions = [i for i in range(n + 1)]
            solutions[1] = 1
            solutions[2] = 2
            for i in range(3, n + 1):
                solutions[i] = solutions[i - 1] + solutions[i - 2]
            return solutions[n]

    def _climb(self, now, n):
        if now >= n - 1:
            return 1
        return self._climb(now + 1, n) + self._climb(now + 2, n)


