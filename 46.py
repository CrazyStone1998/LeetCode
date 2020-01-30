class Solution:
    def permute(self, nums):
        self.target = []
        self._permutation(nums,0)
        return self.target

    def _permutation(self, arr, cursor):
        if (cursor == len(arr) - 1):
            self.target.append(arr.copy())
        else:
            for i in range(cursor, len(arr)):
                self._swap(arr, cursor, i)
                self._permutation(arr, cursor + 1)
                self._swap(arr, cursor, i)

    def _swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

print(Solution().permute([1,2,3]))