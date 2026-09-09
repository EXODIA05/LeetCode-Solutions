class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        window = set()
        for i,j in enumerate(nums):
            if j in window:
                return True
            window.add(j)

            if len(window)>k:
                window.remove(nums[i-k])
        return False
        