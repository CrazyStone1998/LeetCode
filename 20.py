class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {')': '(', '}': '{', ']': '['}
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            elif not stack or stack.pop() != d.get(i):
                return False
        if stack:
            return False
        return True
