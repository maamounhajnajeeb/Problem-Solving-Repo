# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# Example:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

def binarySearch(arr, tar):
    start, end = 0, len(arr)-1
    midponit_index = (start+end)//2
    while start <= end:
        midponit_index = (start+end)//2
        if arr[midponit_index] > tar:
            end = midponit_index-1
        elif arr[midponit_index] < tar:
            start = midponit_index+1
        elif arr[midponit_index] == tar:
            return midponit_index
    return start
