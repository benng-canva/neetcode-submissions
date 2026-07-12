class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqSet = set()

        for num in nums:
            if num in uniqSet:
                return True

            uniqSet.add(num)
        
        return False
        