'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that
 i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
'''

'''
Solution:
3 Sum is another classic two pointers problem but need to take care about some edge cases
Since the overall time complexity is O(n^2) the time to sort the input wouldn't be a problem.

The first approach would be sorting the array so we can implement the two pointers approach.
The next thing we need to take care about is the repeated val when iterating through the input

We have a nested loop so we need to make sure that both loops will not produce duplicate nums
The first edge cases would be 

The logic goes as if the starting number you picked has already been used then it might generate
a repeating arrays for example: [-4, -1, -1, 0, 1, 3] -> if we reuse the first number twice then we
will have repeated values
if i > 0 and nums[i] == nums[i-1]:
    continue
                
and the second edge cases would be
if we have a repeated second number then we might also create duplicates with the same reason.

while r > l and nums[l] == nums[l-1]:
    l += 1


In sum, cases like this 3sum, we need to sort the array then we check for repeated first num and 
repeated second num when we found a match.

The first num (i) ensure the starting num wont be repeated and the second num(j) ensure no middle num
will be repeated.
'''



class Solution:
    def threeSum(self, nums):

        # For the algo, the sorting part will take at least nlog(n) time and 
        # the two pointer approach in a nested loop will take O(n^2) time so in total it would be O(n^2)
        # Space complexity would take a O(N) or O(1) depends on the result or sorting algo

        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1
        return res 
