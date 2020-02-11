class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ''
        end = len(strs[0])
        ans = strs[0]
        for i in strs[1:]:
            pos = 0
            while pos < end and pos < len(i):
                if i[pos] == ans[pos]:
                    pos +=1
                else:
                    end = pos
        return ans[:end]




Solution().longestCommonPrefix(["flower","flow","flight"])