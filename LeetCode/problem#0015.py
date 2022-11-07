# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# # Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.



# My Solution #

from typing import Callable

class Solution:
    
    def __partition(self, array, start, end):
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

    def __quicksort(self, array, start=0, end=None):
        if end is None:
            end = len(array) - 1
        if start < end:
            pivot = self.__partition(array, start, end)
            self.__quicksort(array, start, pivot-1)
            self.__quicksort(array, pivot+1, end)
        return array
    
    def __rightBinSearch(self, nums: list[int], target: int, operator: str) -> int:
        i: int; j: int
        i, j = 0, len(nums)-1
        while i <= j:
            mid: int = (i+j)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                i = mid+1
            elif nums[mid] > target:
                j = mid-1
        return j if operator == "j" else i
    
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = self.__quicksort(nums)
        res: dict; ind: int; length: int
        res, ind, length = {}, 0, len(nums)
        for i in range(length):
            pivot: int = nums[i]
            if i > 0 and nums[i-1] == pivot:
                continue
            elif pivot > 0:
                break
            l: int; r: int
            l, r = i+1, length-1
            while l < r:
                threesum: int = pivot+nums[l]+nums[r]
                if threesum > 0:
                    r: Callable[[list[int], int, str], int] = self.__rightBinSearch(nums[l+1:r], -(nums[l]+pivot), "j") + l + 1
                elif threesum < 0:
                    l: Callable[[list[int], int, str], int] = self.__rightBinSearch(nums[l+1:r], -(nums[r]+pivot), "i") + l + 1
                else:
                    res[ind] = [pivot, nums[l], nums[r]]
                    l, r, ind = l+1, r-1, ind+1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return [res[key] for key in res]
      
# The solution I put it in Leet Code because of time and space complexity #

class Solution:
    
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res: dict, ind: int, length: int
        res, ind, length = {}, 0, len(nums)
        for i in range(length):
            pivot: int = nums[i]
            if i > 0 and nums[i-1] == pivot:
                continue
            #edge case
            elif pivot > 0:
                break
            l: int; r: int
            l, r = i+1, length-1
            while l < r:
                threesum: int = pivot+nums[l]+nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    res[ind] = [pivot, nums[l], nums[r]]
                    l, r, ind = l+1, r-1, ind+1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return [res[key] for key in res]
