'''
Given an integer array nums that may contain duplicates, return all possible 
subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
'''

'''
Solution:
This problem is very similar to the subset problem. The only difference
will be we are not able to incluse duplicates.
Since we cant include duplicate, we need to sort the array so that 
all duplicates will line next to each other.

We then add the following line after we pop the value from the subset
the avoid duplicates.

        while i + 1 < len(nums) and nums[i] == nums[i+1]:
            i+=1

For instance, if you have [1,2,2], treating both 2s independently would yield two identical subsets like [1,2] 
To handle this, your code includes the first occurrence of a number (via subset.append(nums[i])), 
then recurses (via backtrack(i + 1)), and then considers not including this number in the subset (via subset.pop()). 
After popping the number, you need to decide whether to include or exclude the next number. 
However, if the next number is a duplicate (i.e., the same as the current one), 
including it will lead to a duplicate subset because the previous recursive call has already considered subsets 
including this number.
'''


class Solution:
    def subsetsWithDup(self, nums):
        
        # The time complexity would be O(n*(2^n)) as we are using a backtracking approach
        # The decision would be either include nums[i] or don't include it. That is where the 2 is for
        # nlongn for time complexity on the sorting algo can be ignore as 2^n is way bigger than that
        # Space complexity would be O((2^n)) as we store all the subsets
        res = []
        nums.sort()

        def backtracking(i, subset):
            if i == len(nums):
                print(subset.copy())
                res.append(subset.copy())
                return
            
            # include the value
            subset.append(nums[i])
            backtracking(i+1, subset)
            # --> [1,2,2,3] 
            # not include the value
            subset.pop()
            # --> [1,2,2], i=3
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1 
            # adding [1,2,2] i=3
            backtracking(i+1, subset)
        backtracking(0, [])
        return res