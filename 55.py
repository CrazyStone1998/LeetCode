class Solution:
    def canJump(self, nums) -> bool:
        # dp
        # length = len(nums)
        # flag = [False for _ in range(len(nums))]
        # flag[length - 1] = True
        # for i in range(length - 2, -1, -1):
        #     for j in range(i + 1, min(i + nums[i] + 1, length)):
        #         if flag[j]:
        #             flag[i] = True
        #             break
        # return flag[0]

        # # recursion
    # def jump(nums, pos):
    #     if pos >= len(nums) - 1:
    #         return True
    #     for i in range(nums[pos], 0, -1):
    #         if jump(nums,pos + i):
    #             return True
    #     return False
    # return jump(nums, 0)

    # 贪心算法
        end = 1
        for i in range(len(nums)):
            if i < end:
                end = max(end, i + nums[i]+1)
                if end >= len(nums):
                    return True
            else:
                return False
        return False
