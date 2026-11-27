class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counts = {}
        unique = []
        for letter in arr:
            counts[letter] = counts.get(letter, 0) + 1
        for letter in counts:
            if counts[letter] == 1:
                unique.append(letter)
        if len(unique) < k:
            return ""
        return unique[k-1]
        