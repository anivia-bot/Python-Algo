'''
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, 
with timestamp_prev <= timestamp. If there are multiple such values, 
it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
 
Example 1:

Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", 
since there is no value corresponding to foo at timestamp 3 and timestamp 2, 
then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"

'''
'''
Since the problem invloves timestamp and it will always be in an increasing order.
Which mean the list is somewhat sorted. Which mean it is a give a way tip to 
use binary search to speed up the algorithms.

Use l and r ptr (right ptr will be the len of the list inside the dict)
if timestamp has greater val then we store it in res temp until we reach
to the closest timestamp with the while loop.


When dealing with binary search that have value that are not even distributed ex: 1, 3, 7, 14, 129
It is best to have a tmp/res variable to keep track on what is the bottom line that satisfied the needs
of the problem. Since we are having a stack and the problem ask for the nearest result that is smaller or 
equal to the given timestamp, when updating the left ptr, it is guarentee that the middle ptr could be on of
the result so we should saved it in tmp.
'''
    
    # init and set will have O(1) time complexity and get will have O(log(N)) time.
    # since timeMap will be holding up all the pairs, the space complexity would be O(N)

class TimeMap:

    def __init__(self):
        self.keyStack = {}

    def set(self, key, value, timestamp):
        if key not in self.keyStack:
            self.keyStack[key] = [(value, timestamp)]
            return
        self.keyStack[key].append((value, timestamp))

    def get(self, key, timestamp):
        
        if key not in self.keyStack:
            return ""
        
        currentStack = self.keyStack[key] # [(v,t), (v,t)] in sorted order.
        l = 0
        r = len(currentStack) - 1
        res = 0
        while r >= l:
            m = (l + r) // 2
            currentTime = currentStack[m][-1]
            currentValue = currentStack[m][0]
            if currentTime == timestamp:
                return currentValue
            elif currentTime < timestamp:
                res = m
                l = m + 1
            else:
                r = m - 1
        return "" if currentStack[res][-1] > timestamp else currentStack[res][0]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)