class Solution:
    def maxArea(self, height) -> int:
        start, end = 0, len(height) - 1
        ans = 0
        while start < end:
            if height[start] < height[end]:
                ans = max(ans, (end - start) * height[start])
                start += 1
            else:
                ans = max(ans, (end - start) * height[end])
                end -= 1
        return ans