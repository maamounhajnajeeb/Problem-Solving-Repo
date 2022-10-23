# You are a product manager and currently leading a team to develop a new product.
# Unfortunately, the latest version of your product fails the quality check.
# Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version.
# You should minimize the number of calls to the API.

# Example : Input: n = 5, bad = 4, Output: 4
# Example : Input: n = 1, bad = 1, Output: 1

def isBadVersion(version: int) -> bool:
    pass

class Solution:
    def check(self, mid):
        result = isBadVersion(mid)
        if result == True:
            if mid-1 >= 0 and isBadVersion(mid-1):
                return "right"
            return "found"
        elif result == False:
            return "left"

    def firstBadVersion(self, n: int) -> int:
        start, end = 0, n
        while start <= end:
            mid = (start+end)//2
            result = self.check(mid)
            if result == "found":
                return mid
            elif result == "right":
                end = mid-1
            elif result == "left":
                start = mid+1
