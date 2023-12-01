class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        tmp = []
        res = []

        def backtracking(left, right):
            if left == n and right == n:
                tmpString = ''.join(tmp)
                res.append(tmpString)
                return
            
            if left < n:
                tmp.append('(')
                backtracking(left + 1, right)
                tmp.pop()
            
            if right < left:
                tmp.append(')')
                backtracking(left, right + 1)
                tmp.pop()

        backtracking(0,0)
        return res

                