class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        seen = {}
        for i,j in enumerate(num):
            diff = target - j
            if diff in seen:
                return [seen[diff],i]
            else:
                seen[j] = i