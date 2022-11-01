# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

# Example : input: nums1 = [1,2,2,1], nums2 = [2,2]
#         : output: [2, 2]
# Example : input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
#         : output: [4, 9]

class Solution:    
    
    # 3] Hash Table
    resultHashTable: dict = {}

    # 3.1] Binaray Search and two pointers helper function
    def helperFunc(self, nums1: list[int], nums2: list[int],  fPointer: int) -> dict:
        nums1 = nums1[fPointer+1:]
        if len(nums2) > 0 and len(nums1) > 0:
            return self.binSearch(nums1, nums2)
        else:
            return Solution.resultHashTable

    # 1] Sorting
    def partition(self, array: list[int], start:int, end:int):
        if end is None:
            end = len(array)-1
        l, r = start, end-1
        while l < r:
            if array[l] <= array[end]:
                l += 1
            elif array[r] > array[end]:
                r -= 1
            else:
                array[l], array[r] = array[r], array[l]
        if array[l] > array[end]:
            array[l], array[end] = array[end], array[l]
            return l
        else:
            return end
    def quicksort(self, array: list[int], start=0, end=None):
        if end is None:
            end = len(array) - 1
        if start < end:
            pivot = self.partition(array, start, end)
            self.quicksort(array, start, pivot-1)
            self.quicksort(array, pivot+1, end)
        return array

    # 2] Two Pointers and Binary Search and Hash Table
    def binSearch(self, nums1: list[int], nums2: list[int]) -> dict:
        fPointer: int = 0
        target: int = nums1[fPointer]
        start: int = 0
        end: int = len(nums2) - 1
        while start <= end:
            mid: int = (start+end) // 2
            if nums2[mid] == target:
                try:
                    Solution.resultHashTable[target] += 1
                except KeyError:
                    Solution.resultHashTable[target] = 1
                nums2 = nums2[mid+1:]
                return self.helperFunc(nums1, nums2, fPointer)
            elif nums2[mid] > target:
                end = mid-1
            elif nums2[mid] < target:
                start = mid+1
        return self.helperFunc(nums1, nums2, fPointer)

    # 0] main function
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1 = self.quicksort(nums1)
        nums2 = self.quicksort(nums2)
        mainResult: dict = self.binSearch(nums1, nums2)
        resultList: list = []
        for key, value in mainResult.items():
            resultList += [key for i in range(value)]
        return resultList
