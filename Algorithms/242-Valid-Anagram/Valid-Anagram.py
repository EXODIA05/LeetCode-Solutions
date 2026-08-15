class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        valid = {}
        anagram = {}
        for i in s:
            valid[i] = valid.get(i,0)+1
        for j in t:
            anagram[j]=anagram.get(j,0)+1
        if valid == anagram:
            return True
        else:
            return False
                
            
            

        