'''
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number. 
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.
Return the indices of the two numbers, index1 and index2, 
added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
'''

'''
Solution:
Since the array is already sorted. We can just use the two pointers approach to solve this problem
The intuition behind this problem is quite simple. The array is already sorted so we just need to 
add two numbers together and see if it is greater than the target value.

if the sum is larger than the target, move the right ptr to the left and vice versa if the sum is smaller
than the target. move the left ptr to the right.

'''

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