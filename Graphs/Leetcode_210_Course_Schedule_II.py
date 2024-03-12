'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] 
indicates that you must take course bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. 
If there are many valid answers, return any of them. If it is impossible to finish all courses, 
return an empty array.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
'''
'''
Solution:
This problem is essentially a cycle dectect and DFS traversal order problem.
First create an adj list:
{
    0: [1,2,3],
    1: [],
    2: [3,4],
    3: [6]
}
Then create a visited and done hashset, the visited will track cycle and the done will
mark each valid path's course to completed 
perform dfs, if dfs return false then return [] else return res
if the crs is in visited then we can return false since we found a cycle.
if crs in done then we dont need to visit it since we already added to res

DFS will travese to the end where the first course should be taken. 
we add the crs to res then return back up and repeat (check the code for comments)
'''


class Solution:
    def findOrder(self, numCourses, prerequisites):
        
        # The time complexity would be O(V+E) since we need to go over everyone almost twice
        # Space complexity would be O(N)
        
        preMap = {n:[] for n in range(numCourses)}
        visited = set()
        done = set()
        res = []
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        def dfs(crs):
            if crs in visited:
                return False
            if crs in done:
                return True
            visited.add(crs)
            for pre in preMap[crs]:
                cycle = dfs(pre)
                if not cycle:
                    return False
            # Since there might be different path leads to crs and this will no longer
            # be consider for cycle
            visited.remove(crs)
            # We are now at the end of the dfs and we are processing this node
            # add it to done and res as this node will not be visited again as we 
            # already processed it.
            done.add(crs)
            res.append(crs)
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res
                