class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        from queue import Queue
        q = Queue()
        for i in range(1, n): q.put(str(i))
        ans = [0]

        def recursion(q: Queue, left, k, s, ans):
            if q.empty():
                ans[0] += 1
                if ans[0] == k:
                    return s
                else:
                    return None
            for i in range(left):
                temp = q.get()
                res = recursion(q, left - 1, k, s + temp, ans)
                if res:
                    return res
                q.put(temp)

        return recursion(q, n, k, '', ans)
