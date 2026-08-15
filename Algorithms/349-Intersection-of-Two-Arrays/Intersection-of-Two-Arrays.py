class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_map1={}
        a=[]
        for i in nums1:
            hash_map1[i]=hash_map1.get(0,i)+1
        for key in hash_map1:
            if key in nums2:
                a.append(key)
        return a