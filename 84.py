class Solution:
    def largestRectangleArea(self, heights) -> int:
        heights = [0] + heights + [0]
        stack = [0]
        ans = 0
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                ans = max(ans, heights[stack.pop()] * (i - stack[-1]-1))
            stack.append(i)
        return ans


print(Solution().largestRectangleArea([2, 1, 2]))
