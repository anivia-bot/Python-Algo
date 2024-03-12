class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # Time complexity would be O(N!)
        # Space complexity would be O(N)
        res = []
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

        def dfs(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return 
            for num in count:
                if count[num] > 0:
                    count[num] -= 1
                    curr.append(num)
                    dfs(curr)
                    count[num] += 1
                    curr.pop()
        dfs([])
        return res










