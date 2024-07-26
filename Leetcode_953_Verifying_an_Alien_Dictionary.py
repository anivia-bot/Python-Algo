class Solution:
    def isAlienSorted(self, words, order):
        # Time would be O(N) and space would be O(1) since there are only lowercase alpha 26 letters
        charIdx = {}
        
        for idx, char in enumerate(order):
            charIdx[char] = idx
        
        for i in range(len(words)):
            if i + 1 < len(words):
                w1 = words[i]
                w2 = words[i+1]
                minLen = min(len(w1), len(w2))
                if w1[:minLen] == w2[:minLen] and len(w1) > len(w2):
                    return False

                for j in range(minLen):
                    if charIdx[w1[j]] < charIdx[w2[j]]:
                        break
                    if w1[j] == w2[j]:
                        continue
                    if charIdx[w1[j]] > charIdx[w2[j]]:
                        return False

        return True