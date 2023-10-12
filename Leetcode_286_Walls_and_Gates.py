class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # Time and space complexity are both O(MN)
        rowLen = len(rooms)
        colLen = len(rooms[0])
        q = deque()
        visited = set()
        distance = 1
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for r in range(rowLen):
            for c in range(colLen):
                if rooms[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))
        
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in direction:
                    row = dr + r
                    col = dc + c
                    if (row < 0 or col < 0 or row >= rowLen or col >= colLen or
                        (row, col) in visited or rooms[row][col] == -1):
                        continue
                    visited.add((row, col))
                    q.append([row, col])
                    rooms[row][col] = distance
            distance += 1
        return rooms


