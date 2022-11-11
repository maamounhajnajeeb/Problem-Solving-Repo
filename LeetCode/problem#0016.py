# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

# Example 2:

# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

from math import inf

class Solution:
    
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        res: int; length: int
        length, res = len(nums), inf
        for i in range(length):
            pivot: int = nums[i]
            if i > 0 and nums[i-1] == pivot:
                continue
            l: int; r: int
            l, r = i+1, length-1
            while l < r:
                threeSum: int = pivot+nums[l]+nums[r]
                res = res if abs(res-target) <= abs(threeSum-target) else threeSum
                if threeSum < target: l += 1
                elif threeSum > target: r -= 1
                else: return res
        return res
