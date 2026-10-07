class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        sDict = {}
        tDict = {}

        for i in range(len(s)):
            sDict[s[i]] = sDict.get(s[i], 0) + 1
            tDict[t[i]] = tDict.get(t[i], 0) + 1

        for c in sDict:
            if sDict[c] != tDict.get(c, 0):
                print(tDict)
                print(sDict)
                return False
        
        return True