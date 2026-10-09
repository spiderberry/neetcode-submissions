class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        sDict = {}
        tDict = {}

        for index in range(len(s)):
            sDict[s[index]] = sDict.get(s[index], 0) + 1
            tDict[t[index]] = tDict.get(t[index], 0) + 1

        for c in sDict:
            if sDict[c] != tDict.get(c, 0):
                return False
        return True