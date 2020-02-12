class Solution:
    def countAndSay(self, n: int) -> str:
        if not n: return ''
        ans = '1'

        for _ in range(n - 1):
            temp = ''
            pre = ans[0]
            num = 0
            for i in ans:
                if i != pre:
                    temp += str(num) + pre
                    pre = i
                    num = 0
                num += 1
            ans = temp + str(num) + pre
        return ans
