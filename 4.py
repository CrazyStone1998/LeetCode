class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        length_1, length_2 = len(nums1), len(nums2)
        left, right = (length_1 + length_2 + 1) // 2, (length_1 + length_2 + 2) // 2
        if not length_1:
            return (nums2[left - 1] + nums2[right - 1]) / 2
        if not length_2:
            return (nums1[left - 1] + nums1[right - 1]) / 2

        def recursion(arr1, arr2, end1, end2, start1, start2, pos):
            if pos == 1:
                return min(arr1[start1], arr2[start2])
            else:
                temp = pos // 2
                i = min(start1 + temp - 1, end1)
                j = min(start2 + temp - 1, end2)
                if arr1[i] < arr2[j]:
                    pos -= i - start1 + 1
                    start1 = i + 1
                else:
                    pos -= j - start2 + 1
                    start2 = j + 1
                if start1 > end1:
                    return arr2[start2 + pos - 1]
                elif start2 > end2:
                    return arr1[start1 + pos - 1]
                return recursion(arr1, arr2, end1, end2, start1, start2, pos)

        return (
                       recursion(nums1, nums2, length_1 - 1, length_2 - 1, 0, 0, left) +
                    recursion(nums1, nums2, length_1 - 1, length_2 - 1, 0, 0, right)
               ) / 2


