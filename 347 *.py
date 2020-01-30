class Solution:
    def topKFrequent(self, nums, k: int):
        result = [0 for i in range(k)]

        col = {}

        for i in nums:
            col[i] = col.get(i, 0) + 1

        for key,value in col.items():
            if value > result[-1]:
                pass