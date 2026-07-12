class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanedStr = [c.lower() for c in s if c.isalnum()]

        l, r = 0, len(cleanedStr) - 1

        while l < r:
            if cleanedStr[l] != cleanedStr[r]:
                return False
            
            l += 1
            r -= 1
        
        return True