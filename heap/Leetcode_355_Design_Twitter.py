
'''
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, 
and is able to see the 10 most recent tweets in the user's news feed.
Implement the Twitter class:
Twitter() Initializes your twitter object.
void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. 
Each call to this function will be made with a unique tweetId.
List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. 
Each item in the news feed must be posted by users who the user followed or by the user themself. 
Tweets must be ordered from most recent to least recent.
void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
void unfollow(int followerId, int followeeId) 
The user with ID followerId started unfollowing the user with ID followeeId.

Example 1:

Input
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
Output
[null, null, [5], null, null, [6, 5], null, [5]]

Explanation
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2);    // User 1 follows user 2.
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. 
Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], 
since user 1 is no longer following user 2.
'''
'''
Solution:
This is quite a difficult problem that needs to pay attention to details
First initalize count (to keep track of the tweet time), create tweetMap and followMap 
to track all the tweet a specifc user post and followMap to track all the follow and unfollow

when a user follow someone, simple add the followee to the dictionary ex: {user: (followee1, follwee2)}
remember to use a hashset so that the lookup will be constent
unfollow will simply just perform a unfollow opperation on the dictionary
Be careful for edge cases when followerId and followeeId are not in the dictionary yet. 
You need to create an empty set for it.

Same logic can be apply to postTweet, if userId isnt in tweetMap we need to initalize a list
then we simply add the count(time) and tweetId to the dictionary
ex: {userId: [[time1, tweetId1], [time2, tweetId2]]}

When retreiving tweet we first need to create res [] to store the 10 tweetIds and create a heap 
so we can get the latest tweet when it only takes log(k) to retrieve.

Another edge case is to add the user as to the followMap (user will be following themselves)
Be careful for edge cases when userId is not in the followMap dictionary yet. 
Once we took care of all the edge cases iterate through the followee that the user followed.
store the index of the tweet the followee posted (since a user might post multiple tweets)
The most recent will be at the end of the list since we are appended to the end of the list 
whenever theres a new tweet.
Retrieve the count and tweetId from tweetMap with followeeId and index
we store all the value into a heap and we heapify it when all most recent 

Since we maintain a minHeap structure, we can perform heappop() and add the value
into res, check if the index is still inbounce in the tweetMap, if the followee has some
older posts, we add it back to the heap. Since if the older post is still newer than 
all the other posts from other followee it will still be push to the top of the heap.
return res.
'''

from collections import defaultdict, heapq
class Twitter:
    # Time O(K) for making the heap and runs in O(klogK) to get feed so overall its still O(K)
    # Space O(K) depends on how many follows

    def __init__(self):
        self.count = 0
        self.tweetMap = {}
        self.followMap = {}

    def postTweet(self, userId, tweetId):
        if userId not in self.tweetMap:
            self.tweetMap[userId] = []
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId):
        res = []
        minHeap = []
        if userId not in self.followMap:
            self.followMap[userId] = set()
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([count, tweetId, followeeId, index])
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index > 0:
                count, tweetId = self.tweetMap[followeeId][index-1]
                heapq.heappush(minHeap,[count, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId, followeeId):
        if followerId not in self.followMap:
            self.followMap[followerId] = set()
        self.followMap[followerId].add(followeeId)
        
    def unfollow(self, followerId, followeeId):
        if followerId not in self.followMap:
            self.followMap[followerId] = set()
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)