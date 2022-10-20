# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1]
# You must write an algorithm with O(log n) runtime complexity.

# Examples : 
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Input: nums = [5,7,7,8,8,10], target = 6
# Output : [-1,-1]

# Input: nums = [], target = 0
# Output: [-1,-1]

class Solution:
    def findLeftResult(self, nums, target, mid):
        if mid >= 0 and nums[mid] == target:
            if mid-1 >= 0 and nums[mid-1] == target:
                return "left"
            return "found"
        elif nums[mid] > target:
            return "left"
        elif nums[mid] < target:
            return "right"

    def findRightResult(self, nums, target, mid):
        if mid <= len(nums)-1 and nums[mid] == target:
            if mid+1 <= len(nums)-1 and nums[mid+1] == target:
                return "right"
            return "found"
        elif nums[mid] < target:
            return "right"
        elif nums[mid] > target:
            return "left"

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        start, end= 0, len(nums)-1
        result = [-1, -1]
        while start <= end:
            mid = (start+end) // 2
            left_result = self.findLeftResult(nums, target, mid)
            if left_result == "found":
                result[0] = mid
                break
            elif left_result == "right":
                start = mid+1
            elif left_result == "left":
                end = mid-1

        start, end= result[0], len(nums)-1
        while start <= end:
            mid = (start+end)//2
            right_result = self.findRightResult(nums, target, mid)
            if right_result == "found":
                result[1] = mid
                break
            elif right_result == "right":
                start = mid+1
            elif right_result == "left":
                end = mid-1

        return result
