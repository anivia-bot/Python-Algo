class Solution:
    def calPoints(self, operations):
        
        # O(N) operations and O(N) time complexity
        if not operations:
            return 0
        ansArray = []
        for op in operations:
            if op == '+':
                addedNum = ansArray[-1] + ansArray[-2]
                ansArray.append(addedNum)
            elif op == 'D':
                doubleNum = ansArray[-1]*2
                ansArray.append(doubleNum)
            elif op == 'C':
                ansArray.pop()
            else:
                ansArray.append(int(op))
        ans = sum(ansArray)
        return ans