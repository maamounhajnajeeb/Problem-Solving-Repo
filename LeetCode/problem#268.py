# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
# Example : Input : nums = [9,6,4,2,3,5,7,0,1]
# Output : 8

class Solution:
    def missingNumber(self, nums:list[int])->int:
        HashTable = {}
        for number in nums:
            HashTable[number] = True
        for i in range(len(nums)+1):
            try:
                HashTable[i]
            except KeyError:
                return i
