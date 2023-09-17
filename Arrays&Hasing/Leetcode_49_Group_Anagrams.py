'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
'''


'''
Solution:
First use a dict to store all the same anagram into a list
The key is the way to categorize each anagram by using a list count
For example: 'acd' -> [1,0,1,1,0,0,0,.......,0] -> make this into a tuple
since tuples are immutable and it can be use as a key
All anagram should produce the same tuple/list since they all used 
the same char the same amount of times

Once it has been completed, store it back into a res list
Check edge cases eg: len of the input is less than or eaual to 1


'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # This algo runs in O(M*N) time and O(M) space
        
        resDict = defaultdict(list)
        res = []
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')] += 1
            resDict[tuple(count)].append(s)
        
        for val in resDict.values():
            res.append(val)
        return res

print(ord('a'))
print(ord('b'))
print([0]*26)