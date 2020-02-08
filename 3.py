class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        start = 0
        num = 0
        for cur in range(len(s)):
            if d.get(s[cur], None) is not None:
                if d[s[cur]] >= start:
                    num = max(num, cur - start)
                    start = d[s[cur]] + 1
                d[s[cur]] = cur
            else:
                d[s[cur]] = cur
        return max(num, len(s) - start)


print(Solution().lengthOfLongestSubstring("pwwkew"))
