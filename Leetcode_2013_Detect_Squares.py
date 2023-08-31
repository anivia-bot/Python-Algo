class DetectSquares:

    def __init__(self):
        # O(N) space
        self.ptsCount = {}

    def add(self, point: List[int]) -> None:
        # O(1) time 
        point = tuple(point)
        if point not in self.ptsCount:
            self.ptsCount[point] = 1
        else:
            self.ptsCount[point] += 1

    def count(self, point: List[int]) -> int:
        # O(N) time and O(1) space
        res = 0
        px, py = point
        for x, y in self.ptsCount:
            if abs(px - x) != abs(py - y) or x == px or y == py:
                continue
            if (px, y) in self.ptsCount and (x, py) in self.ptsCount and (x, y) in self.ptsCount:
                res += self.ptsCount[(px,y)] * self.ptsCount[(x,py)] * self.ptsCount[(x,y)]
        return res
        