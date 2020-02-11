class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums = sorted(nums)
        ans = 2 ** 32
        for i in range(len(nums) - 2):
            if i > 1 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                temp = nums[i] + nums[left] + nums[right] - target
                if temp > 0:
                    right -= 1
                elif temp < 0:
                    left += 1
                else:
                    return temp + target
                ans = temp if abs(ans) > abs(temp) else ans
        return ans + target


print(Solution().threeSumClosest(
    [1, 2, 4, 8, 16, 32, 64, 128]
    , 82))
