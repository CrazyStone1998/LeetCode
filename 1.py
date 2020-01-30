class Solution:
    def twoSum(self, nums, target: int):
        m = {}
        for i in range(len(nums)):
            t = m.get((target - nums[i]), None)
            if t is not None and t != i:
                return [i, t]
            m[nums[i]] = i

