'''
You are given a stream of points on the X-Y plane. Design an algorithm that:

Adds new points from the stream into a data structure. Duplicate points are allowed and 
should be treated as different points.
Given a query point, counts the number of ways to choose three points from the data structure such 
that the three points and the query point form an axis-aligned square with positive area.
An axis-aligned square is a square whose edges are all the same length and are either parallel or 
perpendicular to the x-axis and y-axis.

Implement the DetectSquares class:

DetectSquares() Initializes the object with an empty data structure.
void add(int[] point) Adds a new point point = [x, y] to the data structure.
int count(int[] point) Counts the number of ways to form axis-aligned squares with point point = [x, y] 
as described above.


Solution:

The trick for this problem is that you use a dict to count how many counts a point exisit at the same position.
Once the position has been calculate, now lets get into the bread and butter. The only thing you need to focus on
is to find a diagonal point and see if it forms a square with (px, y) and (x, py) -> only if they exist in the
dictionary. We skip the point if px-x != px-y abs value. We also skip if x == px and y == py since we cant form
a squre at its own position. Iterate over every points and see if it forms a square.
'''

# Time and Space complexity would be both O(N)

class DetectSquares:

    def __init__(self):
        self.ptsCount = {}

    def add(self, point):
        points = tuple(point)
        if points not in self.ptsCount:
            self.ptsCount[points] = 1
            return
        self.ptsCount[points] += 1
        
    def count(self, point):
        res = 0
        px, py = point
        for x, y in self.ptsCount:
            if abs((px - x)) != abs(py - y) or px == x or py == y:
                continue
            if (px, y) in self.ptsCount and (x, py) in self.ptsCount and (x, y) in self.ptsCount:
                # The reason we didnt multiply self.ptsCount[(px, py)] is because we are trying to find
                # how square can (px, py) (only that one specific dot, we dont care even if there are 
                # other dots that happens to be on the same position) form.
                res += self.ptsCount[(px, y)]*self.ptsCount[(x, py)]*self.ptsCount[(x, y)]
        return res
            