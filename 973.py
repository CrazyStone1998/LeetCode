import heapq


class Solution:
    def kClosest(self, points, K: int):
        return sorted(points, key=lambda x: x[0] ** 2 + x[1] ** 2)[:K]

        # l = len(points)
        # heap = [l for _ in range(K)]
        # temp = [i[0] ** 2 + i[1] ** 2 for i in points]
        # temp.append(2*10000**2)
        # for i in range(l):
        #     if temp[i] < temp[heap[0]]:
        #         heap[0] = i
        #         pos = 0
        #         while True:
        #             child = 2 * pos + 1
        #             if child >= K:
        #                 break
        #             if child + 1 < K and temp[heap[child + 1]] > temp[heap[child]]:
        #                 child += 1
        #             if temp[heap[pos]] > temp[heap[child]]:
        #                 break
        #             heap[pos], heap[child] = heap[child], heap[pos]
        #             pos = child
        # return [points[i] for i in heap]
