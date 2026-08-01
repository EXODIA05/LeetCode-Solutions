class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        emtpy ={}
        for i in nums:
            emtpy[i] = emtpy.get(i,0)+1
        for key,values in emtpy.items():
            if values ==1:
                return key