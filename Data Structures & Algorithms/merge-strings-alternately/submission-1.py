class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len_word1, len_word2 = len(word1), len(word2)
        result = ""
        for i in range(max(len_word1, len_word2)):
            if i < len_word1:
                result += word1[i]
            if i < len_word2:
                result += word2[i]
        return result