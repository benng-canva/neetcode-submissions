class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        pivotIndex = l

        print(pivotIndex)

        leftSearch = self.binarySearch(nums, 0, pivotIndex, target)
        rightSearch = self.binarySearch(nums, pivotIndex, len(nums), target)

        return leftSearch if leftSearch != -1 else rightSearch if rightSearch != -1 else -1

    def binarySearch(self, nums, start, end, target):
        print(nums[start:end])
        l, r = start, end - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return -1
