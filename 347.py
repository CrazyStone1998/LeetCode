from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums, k: int):
        # tip 1
        # return [i[0] for i in Counter(nums).most_common(k)]

        # tip 2
        # count_dict = Counter(nums)
        # return heapq.nlargest(k, count_dict.keys(), key=count_dict.get)

        self.count_dict = {}
        self.heap = [['', 0] for i in range(k)]
        for i in nums:
            self.count_dict[i] = self.count_dict.get(i, 0) + 1
        for key, val in self.count_dict.items():
            if val > self.heap[0][1]:
                self.heap[0] = [key, val]
                pos = 0
                while True:
                    child = 2 * pos + 1
                    if child >= k:
                        break
                    if child + 1 < k and self.heap[child + 1][1] < self.heap[child][1]:
                        child += 1
                    if val < self.heap[child][1]:
                        break
                    self.heap[pos], self.heap[child] = self.heap[child], self.heap[pos]
                    pos = child
        return [i[0] for i in self.heap]
