class Solution:
    def permuteUnique(self, nums):
        self.target = []
        self._permutation(nums, 0)
        return self.target
    def _permutation(self, arr, cursor):
        if cursor == len(arr) - 1:
            temp = arr.copy()
            self.target.append(temp)
        else:
            for i in range(cursor, len(arr)):
                if self._isRepeat(arr, i):
                    continue
                self._swap(arr, cursor, i)
                self._permutation(arr, cursor + 1)
                self._swap(arr, cursor, i)

    def _isRepeat(self, arr, i):
        return arr[i] in arr[i + 1:]

    def _swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

