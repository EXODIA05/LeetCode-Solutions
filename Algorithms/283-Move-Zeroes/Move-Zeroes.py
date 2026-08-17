class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        pos = 0 
        for i in range(1,len(nums)):
            if nums[pos]!=0:
                pos+=1
            nums[pos],nums[i]=nums[i],nums[pos]
        return nums