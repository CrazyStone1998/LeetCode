class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        start = pos = 0
        while pos < len(haystack):
            temp = pos
            if haystack[pos] == needle[start]:
                start += 1
                if start == len(needle):
                    return temp
            else:
                start = 0
            pos += 1
        return -1

