class Solution:
    def rob(self, nums) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        nums[1] = nums[1] if nums[1] > nums[0] else nums[0]
        for i in range(2, len(nums)):
            nums[i] = max(nums[i - 2] + nums[i], nums[i - 1])
        return nums[-1]