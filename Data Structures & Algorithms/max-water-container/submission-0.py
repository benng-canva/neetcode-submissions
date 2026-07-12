class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0
        i, j = 0, len(heights) - 1

        while i < j:
            currentArea = min(heights[i], heights[j]) * (j - i)
            maxA = max(maxA, currentArea)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        
        return maxA