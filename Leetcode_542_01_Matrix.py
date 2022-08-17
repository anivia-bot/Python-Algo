class Solution:
    def updateMatrix(self, mat):
        # This is the slow BFS Solution invoke BFS everytime it when it finds a "1"
        # Worst case O(N*M)^(N*M) run time and O(N*M) space time
        
        from collections import deque
        def bfs(node):
            q = deque()
            q.append((node,0))
            visited = set()
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            
            while q:
                for i in range(len(q)):
                    coor, d = q.popleft()
                    x, y = coor
                    if mat[x][y] == 0:
                        return d
                    visited.add((x,y))
                    for dirs in directions:
                        newX, newY = x+dirs[0], y+dirs[1]
                        lenX, lenY = len(mat)-1, len(mat[0])-1
                        
                        if newX >= 0 and newX <= lenX and newY >= 0 and newY <= lenY:
                            if (newX, newY) not in visited:
                                q.append(((newX, newY), d+1))
                        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    d = bfs((i,j))
                    mat[i][j] = d
        return mat

    def updateMatrix(self, mat):
        # This is the fast BFS Solution invoke BFS only once by starting from "0"
        # O(N*M) run time and O(N*M) space time
        
        from collections import deque
        visited = set()
        q = deque()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.append((i,j))
                    visited.add((i,j))
        while q:
            x, y = q.popleft()
            lenX, lenY = len(mat)-1, len(mat[0])-1
            for dirs in directions:
                newX, newY = x+dirs[0], y+dirs[1]
                if newX >= 0 and newX <= lenX and newY >= 0 and newY <= lenY and (newX, newY) not in visited:
                    mat[newX][newY] = mat[x][y]+1
                    visited.add((newX, newY))
                    q.append((newX, newY))
        return mat
                