class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        maxLen = 0
        start, end = 0, 0

        while end < len(s):
            while s[end] in charSet:
                charSet.remove(s[start])
                start += 1

            charSet.add(s[end])
            maxLen = max(maxLen, len(charSet))
            end += 1

        return maxLen