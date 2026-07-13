class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0

        windowStart, windowEnd, maxF, freq = 0, 0, 0, {}

        while windowEnd < len(s):
            if s[windowEnd] not in freq:
                freq[s[windowEnd]] = 1
            else:
                freq[s[windowEnd]] += 1
                
            maxF = max(maxF, freq[s[windowEnd]])

            while (windowEnd - windowStart + 1) - maxF > k:
                freq[s[windowStart]] -= 1
                windowStart += 1
    
            maxLen = max(maxLen, windowEnd - windowStart + 1)
            windowEnd += 1

        return maxLen