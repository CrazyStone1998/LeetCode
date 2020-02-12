class Solution:
    def maxSubArray(self, nums) -> int:
        nums[0] = nums[0] if nums[0] > 0 else nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i - 1] + nums[i])
            ans = max(ans,nums[i])
        return ans