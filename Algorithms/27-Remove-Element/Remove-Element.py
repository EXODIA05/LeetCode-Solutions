class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pos = 0 
        while pos<len(nums):
            if nums[pos]==val:
                del nums[pos]
            else:
                pos+=1
        return pos 