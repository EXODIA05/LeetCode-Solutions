class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = "".join(char for char in s if char.isalnum())
        a = a.lower().replace(" ", "")
        if a !=a[::-1]:
            return False
        return True
        
