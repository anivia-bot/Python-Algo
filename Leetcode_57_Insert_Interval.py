class Solution:
    def insert(self, intervals: List[List[int]], newI: List[int]) -> List[List[int]]:
        
        # This runs in O(N) time and O(N) space        
        res = []
        addInterval = True
        i = 0
        while i < len(intervals):
            print(i)
            
            if newI[1] < intervals[i][0]:
                res.append(newI)
                addInterval = False
                for j in intervals[i:]:
                    print(j)
                    res.append(j)
                break

            elif newI[0] > intervals[i][1]:
                print("here")
                res.append(intervals[i])
            # this is when you deal with multiple overlapping
            # merging intervals to a wider intervals
            else:
                newI = [min(newI[0], intervals[i][0]), max(newI[1], intervals[i][1])]
            i += 1
            
        if addInterval:
            res.append(newI)
            
        return res