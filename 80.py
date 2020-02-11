class Solution:
    def removeDuplicates(self, nums) -> int:
        if len(nums) < 3:
            return len(nums)
        pos = left = 0
        right = 2
        while right < len(nums):
            if nums[right] != nums[left]:
                nums[pos] = nums[left]
                pos += 1
            left += 1
            right += 1
        nums[pos] = nums[-2]
        nums[pos + 1] = nums[-1]
        return pos + 2
