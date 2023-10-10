'''
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 
'''

'''
Solution:
This is a typical bucket sort problem
basically just loop through the nums list and store it's freq in a Dict as a value
create a freq array with a bunch of empty array then insert the freq val into the 
corresponding position.
ex: freq = [[],[],[],[1],[],[3]]

reverse loop the freq array since the most freq val will be sorted automatically
if the item is an empty [] just skip/continue it

count if the val in the res is equal to the k val
if they are equal then just return it


'''

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
