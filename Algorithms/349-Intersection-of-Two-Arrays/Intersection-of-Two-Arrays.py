class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=[]
        b = list(set(nums1))
        for i in range(len(b)):
            flag = False
            if b[i] in nums2:
                flag = True
            if flag:
                 a.append(b[i])
        return a