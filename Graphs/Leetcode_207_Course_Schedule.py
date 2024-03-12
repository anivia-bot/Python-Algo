'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] 
indicates that you must take course bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
'''

'''
Solution:
In simple words, this is algo focus on finding cycle in graphs

First we create a adjacency list (with pre work such as empty [] for all crs)
once the adj list has been created
ex:
{
    0: [1,2,3],
    1: [],
    2: [3,4],
    3: [6]
}

we can start implementing our dfs traversal function.
For all dfs function base cases are necessary.
for example if the course has been visited then we found a cycle.
return False immediately. If node has been processed (in done) then we simply return True.

if none of the base cases meet, that means we are visiting a new node (add it to visited)
Then we iterate over it's preReq and run DFS on it as well. return False if dfs found a cycle.
remove node from visited and add the current node to done since if some other nodes visit it again
we know that all crs can be completed.

Remeber one edge cases when some nodes are seperated. Be sure to iterate through every nodes and run dfs 
'''

class Solution:
    def canFinish(self, numCourses, prerequisites):
        
        # The time complexity would be O(N+P) as P would be the prerequisites in of the courses
        # The space complexity would be O(N)
        preMap = {n:[] for n in range(numCourses)}
        visited = set()
        done = set()
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
                # This will stop all DFS and will return Flase to the beginning
                if not cycle:
                    return False
            visited.remove(crs)
            done.add(crs)
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True                
