class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        lenght = len(nums)
        for num in nums:
            counts = sum(1 for i in nums if i == num)
            if counts > lenght//2:
                return num