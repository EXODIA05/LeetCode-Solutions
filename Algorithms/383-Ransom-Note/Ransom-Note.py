class Solution:
    def canConstruct(self, rn: str, mz: str) -> bool:
        available= {}
        for i in mz:
            available[i]=available.get(i,0)+1
        for i in rn:
            
            if available.get(i,0)==0:
                return False
            available[i]-=1
        return True
         