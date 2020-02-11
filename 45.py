import sys


class Solution:
    def jump(self, nums) -> int:
        length = len(nums)
        if length == 1:
            return 0
        end = length - 1
        step = 0
        while end != 0:
            for i in range(length):
                if i + nums[i] >= end:
                    step += 1
                    end = i
                    break
        return step
        # max jump
        # length = len(nums)
        # if not length:
        #     return 0
        # end = 0
        # step = 0
        # max_distance = 0
        # for i in range(length):
        #     max_distance = max(max_distance, nums[i] + i)
        #     if max_distance >= length-1:
        #         step += 1
        #         return step
        #     if i == end:
        #         end = max_distance
        #         step += 1

        # length = len(nums)
        # flag = [sys.maxsize for _ in range(length)]
        # flag[-1] = 0
        # for i in range(length - 2, -1, -1):
        #     for j in range(i + 1, min(i + nums[i] + 1, length)):
        #         flag[i] = min(flag[j], flag[i])
        #     flag[i] += 1
        # return flag[0]


print(Solution().jump(
    [2, 3, 1, 1, 4]))
