class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        a_list = s.split()
        hash_map1 = {}
        hash_map2 = {}

        if len(a_list) != len(pattern):
            return False

        for i in range(len(pattern)):
            if pattern[i] in hash_map1 and hash_map1[pattern[i]]!=a_list[i]:
                return False
            if a_list[i] in hash_map2 and hash_map2[a_list[i]]!=pattern[i]:
                return False
            
            hash_map1[pattern[i]] = a_list[i]
            hash_map2[a_list[i]] = pattern[i]


        return True