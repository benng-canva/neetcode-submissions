class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNum = sorted(nums)
        res = set()

        for k in range(len(sortedNum) - 2):
            pairs = self.twoSum(sortedNum[k + 1:], -sortedNum[k])

            for pair in pairs:
                pair.append(sortedNum[k])
                res.add(tuple(pair))
        
        return [list(triplet) for triplet in res]


    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        i, j = 0, len(nums) - 1

        while i < j:
            if nums[i] + nums[j] < target:
                i += 1
            elif nums[i] + nums[j] > target:
                j -= 1
            else:
                res.append([nums[i], nums[j]])
                i += 1
                j -= 1
        
        return res