class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        # Time complexity would be O(N*(4^N)) as we use the backtracking approach
        # Space complexity would be O(N*(4^N)) as well
        
        res = []
        phone = {
         '2': 'abc',
         '3': 'def',
         '4': 'ghi',
         '5': 'jkl',
         '6': 'mno',
         '7': 'pqrs',
         '8': 'tuv',
         '9': 'wxyz'
        }

        def backtrack(i, currS):
            if len(currS) == len(digits):
                res.append(currS)
                return
            
            print(i)
            for c in phone[digits[i]]:
                currS += c
                backtrack(i+1, currS)
                currS = currS[:-1]
                

        if digits:
            backtrack(0, '')
        return res
                