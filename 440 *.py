import math


class Solution:
    num = [0 for i in range(9)]
    def findKthNumber(self, n, k):
        height = int(math.log10(n + 1)) + 1
        H_n = n - 10 ** (height - 1) + 1
        m = H_n//10
        d = H_n%10
        for i in range(9):
            if i <= m:
                self.num[i] = 1/9*(10**(height-1)-1) + 10
            elif i == m+1:
                self.num[i] = 1/9*(10**(height-1)-1) + d
            else:
                self.num[i] = 1/9*(10**(height-1)-1)
        tree = 0
        last = 0
        for i in range(9):
            if sum(self.num[0:i+1]) > k:
                tree = i+1
                last = sum(self.num[0:i+1]) - self.num[i]
                break
        s = str(last % 10 - 1)

        for i in range(height - 2):
            last = last // 10
            s = str(last) + s
        s = str(tree) + s
        print(s)

        return int(s)

Solution().findKthNumber(13,2)