class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = 0 
        while True:
            if missing not in nums:
                return missing
            missing +=1

        
        