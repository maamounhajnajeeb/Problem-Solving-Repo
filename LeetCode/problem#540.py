# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

# Return the single element that appears only once.

# Your solution must run in O(log n) time and O(1) space.

# Example 1:
# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2

# Example 2:
# Input: nums = [3,3,7,7,10,11,11]
# Output: 10


class Solution:
    def singleNonDuplicate(self, nums:list[int]) -> int:
        start:int = 0
        end:int = len(nums)-1
        while start <= end:
            mid:int = (start+end)//2
            if mid+1 < len(nums) and nums[mid+1] == nums[mid]:
                if len(nums[:mid]) % 2 == 0:
                    start = mid+2
                else:
                    end = mid-1
            elif mid-1 >= 0 and nums[mid] == nums[mid-1]:
                if len(nums[:mid-1]) %2 == 0:
                    start = mid+1
                else:
                    end = mid-2
            else:
                break
        return nums[mid]
