class Solution:
    def canConstruct(self, rn: str, mz: str) -> bool:
        rnn={}
        mzz={}
        for i in rn:
            rnn[i]=rnn.get(i,0) + 1
        for j in mz:
            mzz[j]=mzz.get(j,0) + 1
        for i in rnn:
            if i not in mzz:
                return False 
            if rnn[i]>mzz[i]:
                return False
        return True