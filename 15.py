class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        length = len(nums)
        ans = set()
        for i in range(length - 2):
            if nums[i] > 0:
                return ans
            elif i > 0 and nums[i] == nums[i - 1]:
                continue
            else:
                left, right = i + 1, length - 1
                while left < right:
                    if nums[i] + nums[left] + nums[right] == 0:
                        ans.add((nums[i], nums[left], nums[right]))
                        left += 1
                        right -= 1
                    elif nums[i] + nums[left] + nums[right] > 0:
                        right -= 1
                    else:
                        left += 1
        return [list(i) for i in ans]

        # length = len(nums)
        # d = {}
        # ans = set()
        # for j in range(length - 1):
        #     for i in range(j):
        #         if not d.get(nums[i] + nums[j], None):
        #             d[nums[i] + nums[j]] = set()
        #         d[nums[i] + nums[j]].add((nums[i], nums[j]) if nums[i] < nums[j] else (nums[j], nums[i]))
        #     if d.get(0 - nums[j + 1], None):
        #         for k in d.get(0 - nums[j + 1]):
        #             if nums[j + 1] > k[1]:
        #                 ans.add((k[0], k[1], nums[j + 1]))
        #             elif nums[j + 1] < k[0]:
        #                 ans.add((nums[j + 1], k[0], k[1]))
        #             else:
        #                 ans.add((k[0], nums[j + 1], k[1]))
        # return [list(i) for i in ans]


print(Solution().threeSum([1, -1, -1, 0]))
