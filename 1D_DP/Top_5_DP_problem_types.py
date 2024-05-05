'''
These are the top 5 DP problem types:

1. Fibonacci Numbers

    Climbing Stairs
    House Robber
    Fibonacci Number
    Maximum Alternating Subsequence Sum

    Patterns:

    Bottom-Up DP (usually applis on 1D DP problem with 2 variables to 
    keep track to save memory)

    
2. Zero / One Knapsack

    Partition Equal Subset Sum
    Target Sum

    Patterns:

    We can either use it 0 time or 1 time. It will be a 2D DP problem and
    since this is NOT an unbounded Knapsack problem, if we use a coin once and move the 
    position to the lower right corner since we used a coin (so once less coin remaining) 
    and we subtracked the values. 

    
        5   4   3   2   1   0

    1   0   0   0   0   0   T

    2   0   0   0   0   0   T

    3   0   0   0   0   0   T
    

3. Unbounded Knapsack

    Coin Change
    Coin Change II
    Minimum Cost for Tickets

    Patterns:

    This is a bottom up approach as well, we rely on the computation from the right and bottom.

    Very similar to the Zero / One Knapsack problem. But instead of going to the lower right corner,
    we can move directly to the right or directly down since we can reuse the coin multiple times.
    For example, if the target is 5 and we reuse the '1 coin' 5 times then it will just nevigate from
    left to right and finally reached 0 and return True.

    The other case will be skipping the use of '1 coin' instead we use a '2 coin' we will nevigate the 
    2D array downwards. In sum we either move to the right or to the bottom to retrieve the value.
    Because of this trait, we simply just do a bottom up approach from the lower right corner and 
    moves all the way up to the upper right corner. We then compare the value from the right/down
    in order to calculate the return at the 0s index ex: array[0][0]

        5   4   3   2   1   0

    1   0   0   0   0   0   T

    2   0   0   0   0   0   T

    3   0   0   0   0   0   T


4. Longest Common Subsequence

    Longest Common Subsequence
    Longest Increasing Subsequence
    Edit Distance
    Distinct Subsequences

    Patterns: 

    This is 2D DP problem with a bottom-up approach.
    The difference is that you will be comparing to the
    right/bottom/bottom right to find the value.


5. Palindromes

    Longest Palindromic Substring
    Palindromic Substrings
    Longest Palindromic Subsequence

    Patterns:
    This will be a middle out approach. And it will be around O(n) time.

'''