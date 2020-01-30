class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """

        for i in range(len(nums) - 1, 0, -1):

            if nums[i] > nums[i - 1]:
                loc = i
                for j in range(i, len(nums)):
                    if nums[i - 1] >= nums[j]:
                        loc = j - 1
                        break
                    loc = j
                self._swap(nums, i-1, loc)
                self._swapAll(nums, i, len(nums) - 1)
                return

        self._swapAll(nums, 0, len(nums) - 1)
        return

    def _swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def _swapAll(self, arr, i, j):
        if i < j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            self._swapAll(arr, i + 1, j - 1)
Solution().nextPermutation([1,3,2])