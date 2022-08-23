class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # The time complexity would be O(V+E) since we need to go over everyone almost twice
        # Space complexity would be O(N)
        
        preRq = {c:[] for c in range(numCourses)}
        for crs, pre in prerequisites:
            preRq[crs].append(pre)
        visited, cycle = set(), set()
        res = []
        
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            
            cycle.add(crs)
            for pre in preRq[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
                