class Solution:
    def intersect(self, a: List[int], b: List[int]) -> List[int]:
        freq = {}
        result = []
        for i in a:
            freq[i]=freq.get(i,0) + 1
        
        for j in b:
            if j in freq and freq[j]>0:
                result.append(j)
                freq[j]-=1
        return result

