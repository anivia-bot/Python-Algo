class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Bucktet sort runs in O(N) time and take O(N) space
        countDict = {}
        frequency = [[] for i in range(len(nums)+1)]
        for num in nums:
            if num not in countDict:
                countDict[num] = 1
            else:
                countDict[num] += 1
        for num, freq in countDict.items():
            frequency[freq].append(num)

        res = []
        for num in reversed(range(len(frequency))):
            if frequency[num]:
                for item in frequency[num]:
                    if len(res) == k:
                        break
                    res.append(item)
        return res