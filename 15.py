class Solution:
    def threeSum(self, nums):
        l = len(nums)
        result = []
        for i in range(l):

            for j in range(i + 1, l):

                for k in range(j + 1, l):
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.append([nums[i], nums[j], nums[k]])

        return result