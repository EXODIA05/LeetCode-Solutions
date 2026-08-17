class Solution:
    def reverseString(self, s: List[str]) -> None:
        pos = len(s)-1
        i = 0
        while(i<pos):
            s[i],s[pos]=s[pos],s[i]
            i=i+1
            pos=pos-1
        return None
