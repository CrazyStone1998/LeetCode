class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1
        s = s.lower()
        while start < end:
            while not s[start].isalnum():
                start += 1
                if start > end:
                    return True
            while not s[end].isalnum():
                end -= 1
            if s[start] != s[end]:
                return False
            else:
                start += 1
                end -= 1
        return True
