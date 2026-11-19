class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        list_len = len(nums)
        result = [1] * list_len

        prefix = 1
        for i in range(list_len):
            result[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(list_len - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result