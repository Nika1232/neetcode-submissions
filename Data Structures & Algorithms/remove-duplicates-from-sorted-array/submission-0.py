class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))  # Но лучше просто return len(set(nums))
        return len(nums)