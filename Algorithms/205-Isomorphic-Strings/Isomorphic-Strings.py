class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap={}
        hash_map2={}
        for i in range(len(s)):
            if s[i] in hashmap and hashmap[s[i]]!=t[i]:
                return False
            if t[i] in hash_map2 and hash_map2[t[i]]!=s[i]:
                return False
            hashmap[s[i]]=t[i]
            hash_map2[t[i]]=s[i]
        return True