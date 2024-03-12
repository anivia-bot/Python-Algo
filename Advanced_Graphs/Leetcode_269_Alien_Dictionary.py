'''
There is a foreign language language which uses the latin alphabet, 
but the order among letters is not "a", "b", "c" ... "z" as in English.
You receive a list of non-empty strings words from the dictionary, where the words are sorted 
lexicographically based on the rules of this new language.
Derive the order of letters in this language. If the order is invalid, return an empty string. 
If there are multiple valid order of letters, return any of them.
A string a is lexicographically smaller than a string b if either of the following is true:
The first letter where they differ is smaller in a than in b.
There is no index i such that a[i] != b[i] and a.length < b.length.
Example 1:
Input: ["z","o"]
Output: "zo"
Explanation:
From "z" and "o", we know 'z' < 'o', so return "zo".
'''
'''
Solution:
This is topological sorting algo with DFS.
This problem has a lot of prework that we need to do 
First we need to create an adj with set since we dont want duplicate values
Second iterate through the words list and compare two words at a time
We use range(len(words)-1) to make sure the second word does not go out of bounce
next we need to take care of the edge case when the two words prefix are indentical But
word1 len is greater than word2 -> that will make the ordering incorrect.
We then iterate through the min len of the two words and check each char one by one
once we encouter a different char we simply add it to the adj set as w1 will have
higher priority than w2. ex: a-->b

Once all the prework has been completed we can now work on the dfs portion.
We need to have path and visited to track if we add duplicate char into res
for example:
  ______________
 /              \ 
a ----> b ---->  c
a to c and a to b to c

Lets say we start from b, we will be adding b, c. then lets say we start at a,
we will be adding a, b, c. At that point we will have [c,b,c,b,a] in our result list
So if we are visited a node we already visited in the past, we simply return and not
added into res. We need a path set to keep track if there are a cycle.

Iterate with a for loop on all the neighbor the char has. If it return True
which means theres a cycle. Thus we return True.
We remove char from path when we reached the end and add the char into res.

Iterate over all the char in adjList, the order does not matter since we wont be adding duplicates
and dfs will always reaches the end and add all char in reverse order.
reverse res and return.
'''

class Solution:
    def alienOrder(self, words):
        # Time complexity would be O(C) and O(1)
        adjList = {}
        for word in words:
            for char in word:
                if char not in adjList:
                    adjList[char] = set()
        
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ''
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adjList[w1[j]].add(w2[j])
                    break
        path = set()
        added = set()
        res = []
        
        def dfs(char):
            if char in path:
                return True
            if char in added:
                return False
            path.add(char)
            added.add(char)
            for nei in adjList[char]:
                if dfs(nei):
                    return True
            path.remove(char)
            res.append(char)
            return False
        
        for c in adjList:
            if dfs(c):
                return ''
        res.reverse()
        return ''.join(res)