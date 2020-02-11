class Solution:
    def trap(self, height) -> int:
        # stack
        stack = [0, ]
        ans = 0
        if not height:
            return 0
        for i in range(1, len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                h = min(height[i], height[stack[-1]]) - height[top]
                ans += h * (i - stack[-1] - 1)
            stack.append(i)
        return ans


        # double points dynamic
        # if not height:
        #     return 0
        # left, right = 0, len(height) - 1
        # left_max, right_max = height[left], height[right]
        # ans = 0
        # while left < right:
        #     if height[left] <= height[right]:
        #         if height[left] > left_max:
        #             left_max = height[left]
        #         else:
        #             ans += left_max - height[left]
        #         left += 1
        #     else:
        #         if height[right] > right_max:
        #             right_max = height[right]
        #         else:
        #             ans += right_max - height[right]
        #         right -= 1
        # return ans
        # double points
        # deep = [0 for _ in range(len(height))]
        # ans = 0
        # top = 0
        # for i in range(len(height)):
        #     deep[i] = top = max(top, height[i])
        # top = 0
        # for i in range(len(height) - 1, -1, -1):
        #     top = max((top, height[i]))
        #     deep[i] = min(deep[i], top)
        # for i in range(len(height)):
        #     ans += deep[i] - height[i]
        # return ans
print(Solution().trap(
[0,1,0,2,1,0,1,3,2,1,2,1]))