# An array arr a mountain if the following properties hold:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

# You must solve it in O(log(arr.length)) time complexity.

# Example : input : arr = [0,1,0], output : 1
#           input : arr = [0,2,1,0], output : 1

class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        start, end = 0, len(arr)-1
        while start <= end:
            mid = (start+end)//2
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid] >= arr[mid-1] or arr[mid] <= arr[mid+1]:
                start = mid+1
            else:
                end = mid-1
