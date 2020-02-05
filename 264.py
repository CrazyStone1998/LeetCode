class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n < 6:
            return n
        else:
            import heapq
            result = None
            d = {}
            num = 0
            heap = []
            heapq.heappush(heap, 1)
            d[1] = None
            while num < n:
                result = heapq.heappop(heap)
                a = result * 2
                b = result * 3
                c = result * 5
                if not d.get(a, None):
                    heapq.heappush(heap, a)
                    d[a] = 1
                if not d.get(b, None):
                    heapq.heappush(heap, b)
                    d[b] = 1
                if not d.get(c, None):
                    heapq.heappush(heap, c)
                    d[c] = 1
                num += 1

            return result


print(Solution().nthUglyNumber(7))
