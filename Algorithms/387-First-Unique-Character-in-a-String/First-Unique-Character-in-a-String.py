class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map={}
        for i in s:
            hash_map[i]=hash_map.get(i,0) + 1
        for i,j in hash_map.items():
            if j==1:
                return s.find(i)    
        return -1    