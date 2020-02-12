class Solution:
    def searchRange(self, nums, target: int):
        if not nums: return [-1,-1]
        left, right = 0, len(nums) - 1
        ans = 0
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                right = mid
        if nums[left] == target:
            ans = left
        else:
            return [-1, -1]
        right = len(nums) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        return [ans, right]