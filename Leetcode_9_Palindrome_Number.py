class Solution:
    def isPalindrome(self, x):

        # This algo takes O(N) time and O(N) space
        if x < 0:
            return False
        
        pn = list(str(x))
        
        left = 0
        right = len(pn) - 1
        while right >= left:
            if pn[left] != pn[right]:
                return False
            left += 1
            right -= 1
        return True