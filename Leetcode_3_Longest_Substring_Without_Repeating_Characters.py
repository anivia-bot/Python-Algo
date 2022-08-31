class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # This is a sliding windows problem that runs in O(N) time complexity
        # Since there will only be two pointers that traverse through the entire array
        # The space complexity would be O(M) where M is the unique characters in the array
        # If the array only contains alpha then it would be O(1) since there are only 26 alphabets
        
        if not s:
            return 0
        
        left = 0
        right = 0
        res = 0
        seen = set()
        
        while right < len(s):
            
            if s[right] in seen:
                seen.remove(s[left])
                left += 1
                continue
            
            if s[right] not in seen:
                seen.add(s[right])
                res = max(res, len(seen))
                right += 1
        return res
        