class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = {}

        for s in strs:
            key = self.toCharCount(s)
            if key in anagramMap:
                anagramMap[key].append(s)
            else:
                anagramMap[key] = [s]

        result = [arr for arr in anagramMap.values()]

        return result
        
    def toCharCount(self, s: str) -> tuple:
        count = [0 for i in range(26)]

        for c in s:
            count[ord(c) - ord('a')] += 1
        
        return tuple(count)