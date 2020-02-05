from queue import LifoQueue as Stack


class Solution:
    def partition(self, s: str):
        path = Stack()
        result = []
        self.recursion(s, 0, len(s), path, result)
        return result

    def recursion(self, s, start, end, path: Stack, result):

        if start == end:
            result.append(path.queue.copy())
            return
        for i in range(start, end):
            pre = s[start:i + 1]
            if self.is_palindrome(s, start, i):
                path.put(s[start:i + 1])
                self.recursion(s, i + 1, end, path, result)
                path.get()

    def is_palindrome(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True


# d = {}
# self.find(s, 0, len(s) + 1, d)
# return d[0]
# def find(self, s, start, end, d):
#     if start == end - 1:
#         return []
#     else:
#         for i in range(start + 1, end):
#             pre = s[start:i]
#             if self.huiwen(pre):
#                 if not d.get(i, None):
#                     d[i] = self.find(s, i, end, d)
#                 if d[i]:
#                     d[start] = d.get(start, [])
#                     for k in [[pre] + k for k in d[i]]:
#                         d[start].append(k)
#                 else:
#                     d[start] = d.get(start, [])
#                     d[start].append([pre])
#         return d[start]
# def huiwen(self, s):
#     for i in range(len(s) // 2):
#         if s[i] != s[len(s) - i - 1]:
#             return False
#     return True


print(Solution().partition("aab"))
