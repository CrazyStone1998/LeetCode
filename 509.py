class Solution:
    def fib(self, N: int) -> int:
        return

    def _rs(self, N):
        if N == 1:
            return 1
        elif N == 0:
            return 0
        else:
            return self.fib(N - 1) + self.fib(N - 2)

    def _poly(self, N):
        if N == 0:
            return 0
        N_0 = 0
        N_1 = 1
        for i in range(2, N + 1):
            temp = N_0 + N_1
            N_0 = N_1
            N_1 = temp
        return N_1