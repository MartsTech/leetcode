# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    # O(logn) time | O(1) space
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n
        while left < right:
            middle = (left + right) // 2
            if isBadVersion(middle):
                right = middle
            else:
                left = middle + 1
        return left