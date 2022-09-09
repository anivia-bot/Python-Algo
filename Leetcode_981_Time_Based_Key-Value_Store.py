class TimeMap:
    
    # init and set will have O(1) time complexity and get will have O(log(N)) time.
    # since timeMap will be holding up all the pairs, the space complexity would be O(N)

    def __init__(self):
        self.timeMap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
            self.timeMap[key].append([value, timestamp])
        else:
            self.timeMap[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        
        res = ""
        fullList = self.timeMap.get(key, [])
        l = 0
        r = len(fullList) - 1
        
        while r >= l:
            m = (r+l) // 2
            if fullList[m][1] <= timestamp:
                res = fullList[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)