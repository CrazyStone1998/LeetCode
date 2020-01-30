class Solution:
    def findLongestWord(self, s: str, d) -> str:
        d = sorted(d, key=lambda x: (-len(x), x))
        for e in d:
            flag = False
            pos = 0
            l = len(e)
            for i in s:
                if i == e[pos]:
                    pos += 1
                if pos >= l:
                    flag = True
                    break
            if flag:
                return e
        return ""


Solution().findLongestWord("aaa",
                           ["aaa", "aa", "a"])
