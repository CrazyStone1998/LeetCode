import sys
class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        heap = [-sys.maxsize for _ in range(k)]

        for i in nums:
            if i > heap[0]:
                heap[0] = i
                pos = 0
                while True:
                    child = 2 * pos + 1
                    if child >= k:
                        break
                    if child + 1 < k and heap[child + 1] < heap[child]:
                        child += 1
                    if heap[pos] < heap[child]:
                        break
                    heap[pos], heap[child] = heap[child], heap[pos]
                    pos = child
        return heap[0]