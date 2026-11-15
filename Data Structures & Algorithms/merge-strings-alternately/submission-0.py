class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = "".join(letter1 + letter2 for letter1, letter2 in zip_longest(word1, word2, fillvalue=""))
        return result