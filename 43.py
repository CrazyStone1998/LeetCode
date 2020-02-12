class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0': return 0
        n1 = n2 = 0
        for i in num1:
            n1 = n1*10 + int(i)
        for i in num2:
            n2 = n2*10 + int(i)
        return str(n1*n2)


print(Solution().multiply('2','3'))