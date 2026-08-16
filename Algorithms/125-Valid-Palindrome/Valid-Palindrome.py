class Solution:
    def isPalindrome(self, s: str) -> bool:
        pos = len(s)-1
        s =s.lower()
        i = 0
        while i<pos:
            while i<pos and not s[i].isalnum():
                i+=1
            while i < pos and not s[pos].isalnum():
                pos-=1
            if s[i]!=s[pos]:
                return False
            i +=1
            pos-=1
        return True


                
