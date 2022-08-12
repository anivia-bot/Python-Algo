# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        # The time complexity for this case would be O(log(N)) as we are using a binary search approach
        # The space complexity would be O(1) as we only use two poiinters in this solutions
        
        l = 0 
        r = n
        
        while l < r:
            mid = (l+r)//2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return l