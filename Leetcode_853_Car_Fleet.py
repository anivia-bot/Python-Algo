class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # Time complexity would be O(NlogN) due to sorting
        # Space complexity would be O(N)

        pairs = [[p, s] for p, s in zip(position, speed)]
        stack = []

        for pair in reversed(sorted(pairs)):
            p, s = pair[0], pair[1]
            time = (target - p) / s
            stack.append(time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)