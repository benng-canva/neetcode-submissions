class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.toCharMap(s) == self.toCharMap(t)
        
    def toCharMap(self, s: str) -> dict:
        charMap = {}

        for c in s:
            if c in charMap:
                charMap[c] += 1
            else:
                charMap[c] = 1

        return charMap
