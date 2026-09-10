class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        max_value = 1000000
        nums.sort()
        for i in range(len(nums)-k+1):
            
            difference = nums[i+k-1]-nums[i]
            if difference < max_value:
                max_value =difference
        return max_value
