# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target

# You may return the answer in any order.

# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

# Example 2:

# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]

class Solution:
    
    def __helperFunction(self, nums: list[int], start: int, end: int) -> int:
        for i in range(start, end):
            if nums[i] != nums[i-1]: return i
        return end
    
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        length: int; res: dict; ind:int; fPivot: int
        length, res, ind, fPivot = len(nums), {}, 0, 0
        while fPivot < length-3:
            if target > 0 and nums[-1] < 0 or target < 0 and nums[fPivot] > 0: break
            sPivot: int = fPivot+1
            while sPivot < length-2:
                tPivot: int; f4Pivot: int
                tPivot, f4Pivot = sPivot + 1, length-1
                while tPivot < f4Pivot:
                    f4Sum = nums[fPivot] + nums[sPivot] + nums[tPivot] + nums[f4Pivot]
                    if f4Sum > target: f4Pivot -= 1
                    elif f4Sum < target: tPivot += 1
                    else:
                        res[ind] = [nums[fPivot], nums[sPivot], nums[tPivot] , nums[f4Pivot]]
                        ind, tPivot = ind+1, tPivot+1
                        while tPivot < length and nums[tPivot] == nums[tPivot-1]: tPivot += 1
                sPivot = self.__helperFunction(nums, sPivot+1, length-2)
            fPivot = self.__helperFunction(nums, fPivot+1, length-3)
        return [res[key] for key in res]
