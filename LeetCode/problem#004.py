# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays
# The overall run time complexity should be O(log (m+n)).

# Example :
# input : nums1 = [1,3], nums2 = [2]
# output : 2.00000

# Example 2 :
# input : nums1 = [1,2], nums2 = [3,4]
# output : 2.50000

def partition(array, start, end):
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

def quicksort(array, start=0, end=None):
    if end is None:
        end = len(array) - 1
    if start < end:
        pivot = partition(array, start, end)
        quicksort(array, start, pivot-1)
        quicksort(array, pivot+1, end)
    return array

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums = quicksort(nums1+nums2)
        medianIndex = len(nums)//2
        if len(nums) % 2 == 0:
            return (nums[medianIndex]+nums[medianIndex-1])/2
        return nums[medianIndex]/2*2
