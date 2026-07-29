class Solution:
    def containsDuplicate(self, num: List[int]) -> bool:
        if len(num)>len(set(num)):
            return True
        else:
            return False
        """for i in range(len(num)):
            for j in range(len(num)):
                if i!=j:
                    if num[i]==num[j]:
                        return True
        return False"""