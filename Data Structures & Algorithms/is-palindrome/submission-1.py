class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = "".join(char for char in s if char.isalnum()).lower()
        print(result)
        if result==result[::-1]:
            return True
        else:
            return False
        