class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProducts = [1]

        for i in range(len(nums) - 1):
            prefixProducts.append(prefixProducts[-1] * nums[i])

        postfixProducts = [1]

        for i in range(len(nums) - 1, 0, -1):
            postfixProducts.append(postfixProducts[-1] * nums[i])

        postfixProducts = postfixProducts[::-1]

        res = []
        for i in range(len(nums)):
            res.append(prefixProducts[i] * postfixProducts[i])
        
        return res