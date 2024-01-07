'''
Subsets:
make 2 decisions every time and ALWAYS increase i value
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
The subset will either include or not include a value and it keep moving foward
-> Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Subset doesnt have duplicate values
base case for subsets are i >= len(nums)

If we dont wanna include duplicate subset rmbr to sort the array and 
run a while loop after you pop from the subset




Combination:
Combination can have duplicate values
            sub.append(candidate)
            dfs(i, total + candidate)
            sub.pop()
            dfs(i + 1, total)
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]] 
Combination either repeat the same value at the same spot (hence i isnt increasing) or 
i + 1 -> dfs(i + 1, total) 
that moves to the next position with the original total value then dfs(i, total + candidate) 
to add the current position's value.
base case:
            if total == target:
                res.append(sub.copy())
                return
            if total > target or i >= len(candidates):
                return



Permutation:
permutation needs to iterate through the orignal array over and over and ignore the current value
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
            for num in nums:
                if num not in seen:
                    curr.append(num)
                    seen.add(num)
                    backtrack(nums,curr)
                    curr.pop()
                    seen.remove(num)
if the current num has been visited we ignore it, if its not visited then we add it seen
we iterate over the entire array, if its seen then we just simply ignore and move to the next
num. once the iteration is over we pop it out from the curr array and remove it from seen and
continue with the for loop.

base case:
            if len(path) == len(nums):
                res.append(path)

                






'''