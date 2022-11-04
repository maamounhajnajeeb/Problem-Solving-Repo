# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
# Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.

# Example 1:

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

# Example 2:

# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

# Example 3:

# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

class Solution:
    def downRightSide(self, numbers: list[int], target: int, i: int, j: int, operator: str) -> int:
        while i <= j:
            mid = (i+j) // 2
            if numbers[mid] == target:
                return mid
            elif numbers[mid] > target:
                j = mid-1
            elif numbers[mid] < target:
                i = mid+1
        return j if operator == "j" else i

    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i: int; j:int
        i, j = 0, len(numbers)-1
        while i < j:
            condition = target-numbers[j]
            if condition == numbers[i]:
                return [i+1, j+1]
            elif condition > numbers[i]:
                # left
                i = self.downRightSide(numbers, condition, i, j, "i")
            elif condition < numbers[i]:
                # right
                cond2 = target-numbers[i]
                j = self.downRightSide(numbers, cond2, i+1, j+1, "j")
        return False
