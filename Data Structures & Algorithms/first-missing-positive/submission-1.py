class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        if not nums or max(nums) <= 0:
            return 1

        sorted_nums = sorted(set(nums))
        counter = 1
        for num in sorted_nums:
            if num == counter:
                counter += 1
        return counter