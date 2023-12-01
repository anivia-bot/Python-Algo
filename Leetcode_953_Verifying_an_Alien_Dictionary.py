class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Time would be O(N) and space would be O(1) since there are only lowercase alpha 26 letters
        orderDict = {}
        for idx, val in enumerate(order):
            orderDict[val] = idx

        for i in range(len(words)):             
            if i + 1 < len(words):
                w1 = words[i]
                w2 = words[i+1]
                minLen = min(len(w1), len(w2))
                for j in range(minLen):
                    if w1[:minLen] == w2[:minLen] and len(w2) < len(w1):
                        return False
                    if w1[j] == w2[j]:
                        continue
                    if orderDict[w1[j]] > orderDict[w2[j]]:
                        return False
                    break
        return True               