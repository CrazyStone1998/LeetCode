import sys
import heapq


class Solution:
    def mincostToHireWorkers(self, quality, wage, K: int) -> float:
        pay = sys.maxsize
        l = len(quality)
        wq = sorted((float(wage[i] / quality[i]), quality[i]) for i in range(l))
        heap = []
        sum = 0
        for p, q in wq:
            heapq.heappush(heap, -q)
            sum += q
            if len(heap) > K:
                sum += heapq.heappop(heap)
            if len(heap) == K:
                pay = min(pay, p * sum)

        return pay
