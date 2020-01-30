import math
class Solution:

    def numSquarefulPerms(self, A):
        self.num = 0
        self.permutations(A, 0, self.num)
        print(self.num)

    def permutations(self, arr, cursor, num):
        if cursor == len(arr) - 1:
            if self.isSquare(arr, cursor, cursor - 1, 0) and self.isSquare(arr, cursor - 1, cursor - 2, 1):
                print(arr)
                self.num += 1
        else:
            for i in range(cursor, len(arr)):
                if not self.isSquare(arr, cursor - 1, cursor - 2, 1):
                    break
                if self.isRepeat(arr, i) or not self.isSquare(arr, cursor - 1, i, 0):
                    continue
                self.swap(arr, cursor, i)
                self.permutations(arr, cursor + 1, self.num)
                self.swap(arr, cursor, i)

    def isRepeat(self, arr, i):
        return arr[i] in arr[i + 1:]

    def isSquare(self, arr, i, j, condition):

        if i >= condition:
            temp = arr[i] + arr[j]
            return math.modf(temp**0.5)[0] == 0
        return True

    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

a= Solution().numSquarefulPerms([65,44,5,11])