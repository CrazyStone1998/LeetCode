class Solution:
    def twoSum(self, numbers, target: int):
        d = {}
        for i in range(len(numbers)):
            num = numbers[i]
            if d.get(target - num, None):
                return [d.get(target - num), i + 1]
            d[num] = i+1
