class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Time complexity would be O(2^t) as t is the target size or the height of the decision tree
        # Since we are making 2 decisions every time so we are having a 2 to the power solution

        # The space complexity would be O(H) as H would be the height of the tree 
        
        res = []
        
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i+1, cur, total)
        
        dfs(0,[],0)
        return res