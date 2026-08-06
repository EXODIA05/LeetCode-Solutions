class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = {}
        for i in nums:
            hash_map[i]=hash_map.get(i,0)+1
        for i,j in hash_map.items():
            if j>=(len(nums)/2):
                return i
        