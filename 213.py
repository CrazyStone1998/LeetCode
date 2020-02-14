class Solution:
    def rob(self, nums) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]

        def dp(grand, parent, start, end, nums):
            for pos in range(start, end):
                grand, parent = parent, max(grand + nums[pos], parent)
            return parent

        return max(dp(0, nums[0], 1, len(nums) - 1, nums), dp(0, nums[1], 2, len(nums), nums))

