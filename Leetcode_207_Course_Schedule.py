class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # The time complexity would be O(N+P) as P would be the prerequisites in of the courses
        # The space complexity would be O(N)
        preReq = {}
        if not prerequisites:
            return True
        for crs, pre in prerequisites:  
            if pre not in preReq:
                preReq[pre] = []
            if crs not in preReq:
                preReq[crs] = []
                preReq[crs].append(pre)
            else:
                preReq[crs].append(pre)
        
        print(preReq)
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            print(crs)
            if preReq[crs] == []:
                return True
            
            visited.add(crs)
            for pres in preReq[crs]:
                if not dfs(pres):
                    return False
            
            visited.remove(crs)
            preReq[crs] = []
            return True
        
        for crs, value in preReq.items():
            if not dfs(crs):
                return False
        return True
            