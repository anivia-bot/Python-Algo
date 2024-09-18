'''
Given a collection of numbers, nums, that might contain duplicates,
return all possible unique permutations in any order.

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],

Solution:

First count the occurance of each number with a hashmap
Then write a dfs with base case when len(tmp) == len(nums) and append the copy
iterate over the cnt hashmap and decrease it's count. Continue with the for loop
only if the cnt > 0 (means number are remaining and havent been used) append num in tmp
decrease the count and perform dfs. Remember we are iterating over the cnt and since
cnt is a dict, all we need to do is subtract the value from it. And the permutation will be
unique.


'''


class Solution:
    def permuteUnique(self, nums):
        
        res = []
        tmp = []
        cnt = {}
        for num in nums:
            if num not in cnt:
                cnt[num] = 1
                continue
            cnt[num] += 1
        
        def dfs():
            if len(tmp) == len(nums):
                res.append(tmp.copy())
                return
            
            for n in cnt:
                if cnt[n] > 0:
                    tmp.append(n)
                    cnt[n] -= 1
                    dfs()
                    cnt[n] += 1
                    tmp.pop()
        dfs()
        return res
