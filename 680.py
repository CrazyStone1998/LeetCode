class Solution:
    def validPalindrome(self, s: str) -> bool:
        def recursion(start, end, s, th):
            if start >= end:return True
            if s[start] == s[end]:return recursion(start + 1, end - 1, s, th)
            return recursion(start + 1, end, s, th - 1) or recursion(start, end - 1, s, th - 1) if th else False
        return recursion(0, len(s) - 1, s, 1)

print(Solution().validPalindrome('abba'))
