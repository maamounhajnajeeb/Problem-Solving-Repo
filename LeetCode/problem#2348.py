# Given an integer array nums, return the number of subarrays filled with 0.
# A subarray is a contiguous non-empty sequence of elements within an array.

# Example 1:
# Input: nums = [1,3,0,0,2,0,0,4]
# Output: 6
# Explanation: 
# There are 4 occurrences of [0] as a subarray.
# There are 2 occurrences of [0,0] as a subarray.
# There is no occurrence of a subarray with a size more than 2 filled with 0. Therefore, we return 6.

# Example 2:
# Input: nums = [0,0,0,2,0,0]
# Output: 9
# Explanation:
# There are 5 occurrences of [0] as a subarray.
# There are 3 occurrences of [0,0] as a subarray.
# There is 1 occurrence of [0,0,0] as a subarray.
# There is no occurrence of a subarray with a size more than 3 filled with 0. Therefore, we return 9.

# Example 3:
# Input: nums = [2,10,2019]
# Output: 0
# Explanation: There is no subarray filled with 0. Therefore, we return 0.

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        if nums[-1] == 0:
            nums = nums+[1]
        subarrays: int = 0
        zeros: int = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            elif nums[i] != 0 and nums[i-1] == 0:
                subarrays += zeros*((zeros+1))//2
                zeros = 0
        return subarrays
