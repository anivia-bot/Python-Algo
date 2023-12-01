class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        # O(N) time and space
        good = set()

        for trip in triplets:
            goodTrip = True
            for i in range(len(trip)):
                if trip[i] > target[i]:
                    goodTrip = False
                    break
            
            if goodTrip:
                for i in range(len(trip)):
                    if target[i] == trip[i]:
                        good.add(i)
        return True if len(good) == len(target) else False