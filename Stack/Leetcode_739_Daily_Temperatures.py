class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # O(N) time and space
        res = [0] * len(temperatures)
        tmp = []

        for idx, val in enumerate(temperatures):
            while tmp and tmp[-1][1] < val:
                res[tmp[-1][0]] = (idx - tmp[-1][0])
                tmp.pop()
            tmp.append([idx, val])
        return res