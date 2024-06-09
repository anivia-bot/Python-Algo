class Solution:
    def isHappy(self, n: int) -> bool:
        # O(n) time and O(n) space
        visited = set()

        def sumOfSquares(n):
            n = str(n)
            tmp = sum([(int(i))**2 for i in n])
            return tmp

        while n not in visited:
            visited.add(n)
            n = sumOfSquares(n)

            if n == 1:
                return True
        return False
    
