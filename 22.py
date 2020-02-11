class Solution:
    def generateParenthesis(self, n: int):
        ans = []

        def recursion(left, right, proxy, ans):
            if left == right == 0:
                ans.append(proxy)
            else:
                if left < right:
                    if left > 0:
                        recursion(left - 1, right, proxy + '(', ans)
                    if right > 0:
                        recursion(left, right - 1, proxy + ')', ans)
                else:
                    recursion(left - 1, right, proxy + '(', ans)

        recursion(n, n, '', ans)
        return ans
