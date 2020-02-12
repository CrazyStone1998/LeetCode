class Solution:
    def combinationSum(self, candidates, target: int):
        recursion
        ans = []
        def recursion(candidates, pos, length, proxy, allowance, ans):
            if allowance == 0:
                ans.append(proxy.strip().split(' '))
                return
            if pos == length:
                return
            times = 0
            allowance -= candidates[pos] * times
            while allowance >= 0:
                recursion(candidates, pos + 1, length, proxy + (' ' + str(candidates[pos])) * times, allowance, ans)
                times += 1
                allowance -= candidates[pos] * times
        recursion(candidates, 0, len(candidates), '', target, ans)
        return ans
