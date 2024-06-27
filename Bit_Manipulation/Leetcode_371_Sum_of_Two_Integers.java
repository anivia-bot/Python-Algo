'''
Given two integers a and b, return the sum of the two integers without using the operators + and -.
Example 1:

Input: a = 1, b = 2
Output: 3

Solution: 

The reasion we are using Java is because we python will have issue with the negative two compliments
and we need to use mask in order to solve it. 

The logic for this problem is quite straight forward, all you need to do is to keep track of a&b as 
they will detect if the current string has a carry. We shift it to the right by 1: << 1 is because the 
carry value will have to go to the next idx (since it is a carry value duh its like how basic addition works).
Once we calculated the carry value, we simply XOR with the original b because all the 1,1 pair, 0, 0 pair will be
0 and will be added in the next iteration when we XOR them again. b will store all the carry value since if b is 0
which means no more value we need to be carried over we simply end the while loop.
'''



class Solution {
    public int getSum(int a, int b) {
        // b will only contain the carries and loop untill no more carry will exist
        while (b != 0){
            // This calculate the only the carry value since if two bits are 1 then it will have a carry
            int tmp = (a & b) << 1;
            // New a will be a ^ b since XOR will only keep (0, 1) or (1, 0) pair, 0,0 and 1,1 will both be 0
            // tmp will take care of the carry in the next iteration as b will take in tmp and be XOR by a again
            a = a ^ b;
            // b will take in tmp
            b = tmp;
        }
        return a;
    }
}