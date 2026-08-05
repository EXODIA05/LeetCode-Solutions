class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n= 0
        for i in range(len(digits)):
            n = n*10+digits[i]
        n+=1
        return [int(i) for i in str(n)]
        