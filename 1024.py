class Solution:
    def videoStitching(self, clips, T) -> int:
        d = {}
        target = []
        for i in clips:
            if i[1] > d.get(i[0], 0):
                d[i[0]] = i[1]
        for i, j in d.items():
            target.append([i, j])
        target = sorted(target, key=lambda x: (x[0] - x[1]))
        return self.find(0, T, target, 0)

    def find(self, start, end, arr, num):
        left = 0
        right = 0
        for i in arr:
            if i[0] <= start and i[1] - start > left:
                temp_min = i
                left = i[1] - start
            if i[1] >= end and end - i[0] > right:
                temp_max = i
                right = end - i[0]
        if left == 0 or right == 0:
            return -1
        print(temp_min, temp_max)
        if temp_min[1] >= end or temp_max[0] <= start:
            return num + 1
        elif temp_min[1] >= temp_max[0]:
            return num + 2

        return self.find(temp_min[1], temp_max[0], arr, num + 2)
