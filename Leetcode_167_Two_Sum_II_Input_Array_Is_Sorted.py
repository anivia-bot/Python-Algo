class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # This solution runs in O(N) time as we are using a two pointers approach
        # We do not need have extra memory so it is O(1)
        l = 0
        r = len(numbers)-1
        res = []
        while r > l:
            if numbers[l] + numbers[r] == target:
                res.append(l+1)
                res.append(r+1)
            elif numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
        return res