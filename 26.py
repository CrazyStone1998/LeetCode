class Solution:
    def removeDuplicates(self, nums) -> int:
        if len(nums) < 1:
            return len(nums)
        left = right = 1
        ans = 1
        while right < len(nums):
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1
                ans += 1
            right += 1
        return ans