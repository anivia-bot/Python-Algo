class Solution:
    def topKFrequent(self, nums, k):

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
    
# second solution:
        count = {}
        array = [[]]
        res = []
        for num in nums:
            array.append([])
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

        for key, val in count.items():
            array[val].append(key)

        for knum in reversed(array):
            if not knum:
                next
            else:
                for i in knum:
                    if k == 0:
                        break
                    res.append(i)
                    k -= 1
        return res
