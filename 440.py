class Solution:
    def findKthNumber(self, n, k):
        def count(i, j, n):
            num = 0
            while i <= n:
                num += min(j, n + 1) - i
                i *= 10
                j *= 10
            return num
        pos = 1
        pre = 1
        while pos < k:
            now = pos + count(pre, pre + 1, n)
            if now > k:
                pre *= 10
                pos += 1
            else:
                pre += 1
                pos = now

        return pre


print(Solution().findKthNumber(100, 10))
