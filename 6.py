class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ans = ['' for _ in range(numRows)]
        pos = 0
        for i in s:
            if pos == 0:
                z = 1
            elif pos == numRows-1:
                z = -1
            ans[pos] += i
            pos += z
        return ''.join(ans)
print(Solution().convert('LEETCODEISHIRING',3))