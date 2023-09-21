'''
Design an algorithm to encode a list of strings to a string. 
The encoded string is then sent over the network 
and is decoded back to the original list of strings.

Example 1:

Input: dummy_input = ["Hello","World"]
Output: ["Hello","World"]
Explanation:
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);

'''
'''
Solution:
for encoding: 
try to find the len of the str and 
add a self recognize delimeter inbetween num and the actual string.
use a for loop to repeat the process untill all str is processed
return the full string

for decoding:
initalize a list to store the decoded string
use a pointer i to track the position 
while i is less then the len of the input string

set another while loop to track how many numbers, 
we are going to process before the delimeter
use that number to slice the input str
append the updated str then update the ith position

'''

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    # The time and space complexity of this algo runs in O(N) and take O(N) space
    def encode(self, strs):
        res = ''
        for s in strs:
            sLen = str(len(s))
            sAdd = sLen+'#'+s
            res += sAdd
        return res
            

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, strs):
        # write your code here
        res = []
        i = 0

        while i < len(strs):
            j = i
            while strs[j] != '#':
                j += 1
            num = int(strs[i:j])
            s = strs[j+1: j+1+num]
            res.append(s)
            i = j+1+num
        return res
