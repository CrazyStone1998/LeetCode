class Solution:
    def numberOfArithmeticSlices(self, A) -> int:
        # dp
        ans = 0
        dp = 0
        for i in range(2,len(A)):
            if A[i-1]*2 == A[i]+A[i-2]:
                dp +=1
                ans += dp
            else:
                dp = 0
        return ans

        # if len(A) < 3:
        #     return 0
        # start, mid = A[0], A[1]
        # length = 2
        # ans = 0
        # for i in range(2, len(A)):
        #     if start + A[i] == 2 * mid:
        #         ans += length-1
        #         length += 1
        #     else:
        #         length = 2
        #     start, mid = mid, A[i]
        # return ans

