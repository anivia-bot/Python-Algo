'''
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. 
The Pacific Ocean touches the island's left and top edges, 
and the Atlantic Ocean touches the island's right and bottom edges.
The island is partitioned into a grid of square cells. 
You are given an m x n integer matrix heights where heights[r][c] 
represents the height above sea level of the cell at coordinate (r, c).
The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, 
east, and west if the neighboring cell's height is less than or equal to the current cell's height. 
Water can flow from any cell adjacent to an ocean into the ocean.
Return a 2D list of grid coordinates result where result[i] = [ri, ci] 
denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
Example 1:
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
'''
'''
Solution:
This problem is a reverse DFS that starts from the edges (Pac and Alt) and
expend it inwards and add all valid path into Pac and Alt hashset (visited)

Key point to be careful is when you pass in pacSet or altSet rmbr to use
visited when creating the dfs function, since eihter one will be pass in
so it is better to keep it flexible. Another thing to be careful is 
keep track of the prev val. The path can only form is when the current val 
is greater than the prev val (water flows from high to low)

run DFS on both alt and pac edges and save all visited nodes into pacSet or altSet
run another double for loop to see if (r, c) are in both pacSet and altSet.
'''

class Solution:
    def pacificAtlantic(self, heights):
        # Time complexity would be O(N*M)
        # Space complexity would be O(N*M)
        rowLen = len(heights)
        colLen = len(heights[0])
        pacSet = set()
        altSet = set()
        res = []

        def dfs(r, c, visited, prevHeight):
            if (r < 0 or c < 0 or r >= rowLen or c >= colLen or
                 (r,c) in visited or heights[r][c] < prevHeight):
                return
            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
        
        for c in range(colLen):
            dfs(0, c, pacSet, heights[0][c])
            dfs(rowLen - 1, c, altSet, heights[rowLen - 1][c])
        
        for r in range(rowLen):
            dfs(r, 0, pacSet, heights[r][0])
            dfs(r, colLen - 1, altSet, heights[r][colLen - 1])
        
        for r in range(rowLen):
            for c in range(colLen):
                if (r, c) in pacSet and (r, c) in altSet:
                    res.append([r,c])
        return res

