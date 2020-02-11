class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        start = cost = ans = 0
        for end in range(len(s)):
            cost += abs(ord(s[end]) - ord(t[end]))
            if cost > maxCost:
                ans = max(ans, end - start)
                while cost > maxCost:
                    cost -= abs(ord(s[start]) - ord(t[start]))
                    start += 1
        return max(ans, len(s) - start)
