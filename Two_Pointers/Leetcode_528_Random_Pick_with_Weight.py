'''
You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.
You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] 
(inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).
For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), 
and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).
 
Example 1:

Input
["Solution","pickIndex"]
[[[1]],[]]
Output
[null,0]

Explanation
Solution solution = new Solution([1]);
solution.pickIndex(); // return 0. The only option is to return 0 since there is only one element in w.

Solution:

The trick is to realize this is a two pointer problem. you first have to create a probability list
-> [1, 3, 6] will be come [1, 4, 10] as you add up all the weight progressively. The range will be 
the probabilty for example: For target = 5 and cumulative_weights = [1, 4, 10]:
Start by comparing 5 with the middle value (4 at index 1).
Since 5 is greater than 4, move to the right half.
Compare 5 with the next value (10 at index 2).
Since 5 is less than 10, bisect_left determines that 5 should be inserted before 10.
Therefore, bisect_left returns 2, meaning that index 2 is the correct index for the random number 5.


'''

import random

class Solution:

    def __init__(self, w):
        self.w = w
        self.prob = []
        self.total = 0
        for i in self.w:
            self.total += i
            self.prob.append(self.total)

    def pickIndex(self):
        randomInt = random.randint(1, self.total)
        l = 0
        r = len(self.prob) - 1
        
        while l < r:
            m = (l + r) // 2
            if randomInt > self.prob[m]:
                l = m + 1
            else:
                r = m
        return l
