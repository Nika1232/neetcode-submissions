class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        if target > max(nums):
            return len(nums)
        for num in nums:
            if num > target:
                return nums.index(num)