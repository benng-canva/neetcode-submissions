class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqNums = set(nums)

        startCandidates = []
        for num in nums:
            if num - 1 not in uniqNums:
                startCandidates.append(num)
        
        maxLen = 0
        for num in startCandidates:
            curLen = 1
            curNum = num
            while curNum + 1 in uniqNums:
                curLen += 1
                curNum += 1
            maxLen = max(maxLen, curLen)
        
        return maxLen