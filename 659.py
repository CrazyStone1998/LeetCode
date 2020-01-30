class Solution:
    def isPossible(self, nums):
        col = {}
        start = []
        end = []
        for i in nums:
            col[i] = col.get(i, 0) + 1
        for n in range(col.get(nums[0])):
            start.append(nums[0])

        for i in range(nums[0], nums[-1]):
            if col.get(i, 0) < col.get(i + 1, 0):
                for n in range(col.get(i + 1, 0) - col.get(i, 0)):
                    start.append(i + 1)
            elif col.get(i, 0) > col.get(i + 1, 0):
                for n in range(col.get(i, 0) - col.get(i + 1, 0)):
                    end.append(i)

        for s, e in zip(start, end + [nums[-1] for i in range(len(start)-len(end))]):
            if e - s + 1 < 3:
                return False
            while s <= e:
                if col.get(s, 0) > 0:
                    nums.remove(s)
                    s += 1
                else:
                    return False

        if len(nums) == 0:
            return True
        else:
            return False
