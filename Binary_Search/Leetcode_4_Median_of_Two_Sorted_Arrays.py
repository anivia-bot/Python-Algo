'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
'''
'''
Solution:

To solve this problem using binary search you need to first realize we are only
dealing with half size of both array and we just need to choose one to do binary 
search.

For faster completion we choose the smaller array to perform binary search on
hence the A, B = B, A swap
Set l and r ptr on the smaller array (A)
find the middle val in this case i, j will be the middle value for B
the j = half - i - 2 is because both A and B are starting at index 0 
and -2 is make the math works out
A => [1,2,3,4,5,6] => i = 2
B => [2,3,4,5,6,7,8,9] = > j = 7(half) - 2(i) - 2

set variables for both sides Aleft Aright and Bleft Bright
set values for edge cases

The successful condition is that both Aleft and Bleft is smaller than Aright Bright
then we can just compute the median (care for odd and even cases)
if its odd then just return the smallest on the right
if its even combine the max on the left and min on the right and divided by 2

if the successful condition has not been met, then we check the condition and 
perform binary search on array A. We either move the left ptr or right ptr.
'''


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Time complexity runs in O(log(n+m)) space complexity O(1)
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2
            
            Aleft = A[i] if i >=0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >=0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft < Aright:
                if total % 2:
                    return min(Aright, Bright)
                
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
        