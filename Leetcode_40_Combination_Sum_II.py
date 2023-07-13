class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        # Time complexity would be O(2^N) and space will be O(N)
        def dfs(cur, pos, count):
            if count > target:
                return
            if count == target:
                res.append(cur.copy())
            
            prev = float('-inf')
            for idx in range(pos, len(candidates)):
                if candidates[idx] == prev:
                    continue
                cur.append(candidates[idx])
                dfs(cur, idx + 1, count + candidates[idx])
                cur.pop()
                prev = candidates[idx]
        dfs([], 0, 0)
        return res
