class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum())
        s = s.lower()
        pos = len(s)-1
        for i in range(len(s)):
            if s[i]!=s[pos]:
                return False
            pos-=1
        return True
        
