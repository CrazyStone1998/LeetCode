class Solution:
    def letterCombinations(self, digits: str):
        ans = []
        d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mns', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        if not len(digits):
            return []
        def recursion(digits, pos, end, d, s, ans):
            if pos == end:
                ans.append(s)
            else:
                for i in d.get(digits[pos]):
                    recursion(digits, pos + 1, end, d, s + i, ans)

        recursion(digits, 0, len(digits), d, '', ans)
        return ans


Solution().letterCombinations('23')
