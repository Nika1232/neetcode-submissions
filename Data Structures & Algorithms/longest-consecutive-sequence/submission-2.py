class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sort = sorted(set((nums)))
        max_counter = 1
        current_counter = 1
        for current_num, next_num in zip(sort, sort[1:]):
            if current_num+1 == next_num:
                current_counter += 1
                max_counter = max(max_counter, current_counter)
            else:
                current_counter = 1
        return max_counter
