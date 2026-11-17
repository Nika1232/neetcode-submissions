class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        unique = []
        count = Counter(arr)
        for letter in count:
            if count[letter] == 1:
                unique.append(letter)
        if len(unique) < k:
            return ""
        return unique[k-1]
        