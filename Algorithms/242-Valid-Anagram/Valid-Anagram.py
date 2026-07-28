class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        new_dict = {}
        new_dict2 = {}
        for i in s:
            new_dict[i] = new_dict.get(i,0)+1
        for j in t :
            new_dict2[j] = new_dict2.get(j,0)+1
        if new_dict != new_dict2:
            return False
        return True