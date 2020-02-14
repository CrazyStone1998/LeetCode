class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split(' ')
        for i in range(len(arr) - 1,-1,-1):
            if i.isalpha():
                return len(i)
            continue
        return 0
