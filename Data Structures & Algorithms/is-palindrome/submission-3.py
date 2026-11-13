class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = "".join(char for char in s if char.isalnum()).lower()
        if clean_text == clean_text[::-1]:
            return True
        return False
