# You have a list of integers : [4, 5, 6, 7, 8, 9, 0, 1, 2, 3]
# find number of rotations with O(log n) Time Complexity

class Solution:
    def findRotations(self, nums:list[int]):
        start, end = 0, len(nums)-1
        while start <= end:
            mid = (start+end) // 2
            if nums[mid] >= nums[start] and nums[mid] > nums[mid-1]:
                start = mid+1
            elif nums[mid] < nums[end] and nums[mid] < nums[mid+1]:
                end = mid-1
            else:
                return mid
        return 0
