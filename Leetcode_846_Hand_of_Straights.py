class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        # nlog(n) time and O(n) space
        if len(hand) % groupSize:
            return False

        count = {}
        for h in hand:
            if h not in count:
                count[h] = 1
            else:
                count[h] += 1

        minH = list(count.keys())
        heapq.heapify(minH)

        while minH:
            first = minH[0]

            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                
                count[i] -= 1
                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True