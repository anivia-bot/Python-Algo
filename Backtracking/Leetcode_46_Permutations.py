'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
'''
'''
Solution:
There are two ways to solve permutation problem
They are both back-tracking approach. 

Both require a for loop to iterate through all permutation

The first approach is to follow a typical backtracking templete.
-> add the value then remove it when the recursive call is over
-> same approach is often use in DFS
We set a seen hashset and append every visited value into the set.
If it's not visited, we add it to the curr list, if the list is at the
len of nums then we successfully found a pair.
for example -> 
for i in [1,2,3]:
    check if its in seen then we add 1 into the curr list repeat the process when we have
    [1, 2, 3] -> at this point we start popping the value -> [1, 2] -> [1]
    At this point we start finishing the for loop -> [1, 3] -> [1, 3, 2] -> then we went all the way
    back by popping all elements and begin iterating the loop again -> [2] -> [2, 1] -> [2, 1, 3]

The second approach does not require an extra hashset,
This require a for loop and a clever way to split the list and path
curr[:i]+curr[i+1:] -> this is the way to cleverly avoiding the current i index in the for loop
use path + [curr[i]] to pass down all the permutation calculated so far.

Both require the iterate over a for loop to completely cover every permutation cases.
the first one just repeatl iterate over nums completely [1,2,3], [1,2,3], [1,2,3] and just
ignore the visited value

The second method iterate over the modified array by curr[:i]+curr[i+1:], thus the for loop 
will be iterate over curr instead of nums. 
'''

class Solution:
    def permute(self, nums):
        # Time complexity would be O(N!) N factorial
        # Space complexity would be O(N)
        if len(nums) == 0:
            return [[]]

        def backtrack(splitNums):
            # Skipping the first element and create the sub problem
            # [1,2,3] -> [2,3] -> [3] -> []
            if len(splitNums) == 0:
                return [[]]
            permu = backtrack(splitNums[1:])
            res = []

            #iterate over and insert the first element that you skipped
            for perm in permu:
                # +1 because we are now including the first element and we could be
                # inserted into the last position
                for i in range(len(perm) + 1):
                    tmpPerm = perm.copy()
                    tmpPerm.insert(i, splitNums[0])
                    res.append(tmpPerm)
            return res
        return backtrack(nums)

    

class Solution:
    def permute(self, nums):
        res = []
        def backTrack(curr, path):
            # This is the base case for the DFS approach
            if len(path) == len(nums):
                res.append(path)
                return
            for i in range(len(curr)):
                # curr[:i]+curr[i+1] is to remove the current element
                # and pass in a smaller list
                # ex: [1,2,3] -> [2,3]
                backTrack(curr[:i]+curr[i+1:], path+[curr[i]])
        backTrack(nums, [])
        return res