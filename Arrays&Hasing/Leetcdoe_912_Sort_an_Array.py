'''
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) 
time complexity and with the smallest space complexity possible.

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed 
(for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
'''
'''
Solution

This is a merge sort algo and runs in O(nlogn) time and O(n) space
space => O(logn + n) => O(n)

Basically what you would do is you devide the orignal array in half and keep doing it till there are only
one element in the arry. Once the left array and right array hit the base case (one element in an array)
merge them and return the merged array.

Repeat that process with recurssion till every element is merged.
'''
class Solution:
    def sortArray(self, nums):

        def conquer(leftArr, rightArr):
            comb = []
            i = 0
            j = 0

            while i < len(leftArr) and j < len(rightArr):
                leftVal = leftArr[i]
                rightVal = rightArr[j]
                if leftVal <= rightVal:
                    comb.append(leftVal)
                    i += 1
                else:
                    comb.append(rightVal)
                    j += 1
            
            while i < len(leftArr):
                leftVal = leftArr[i]
                comb.append(leftVal)
                i += 1
            
            while j < len(rightArr):
                rightVal = rightArr[j]
                comb.append(rightVal)
                j += 1
            return comb
        

        def divide(arr):
            if len(arr) <= 1:
                return arr

            l = 0
            r = len(arr)
            mid = (l + r) // 2
            leftArr = divide(arr[:mid])
            rightArr = divide(arr[mid:])
            combArr = conquer(leftArr, rightArr)
            return combArr
        
        return divide(nums)