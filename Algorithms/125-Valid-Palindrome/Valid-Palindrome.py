class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum())
        s = s.lower().replace(" ", "")
        if s!=s[::-1]:
            return False
        return True
        
