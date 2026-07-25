class Solution:
    def isValid(self, s: str) -> bool:
        waiting_list=[]

        for i in s:
        
            if i in "[{(":
                waiting_list.append(i)
            
            else:
                if not waiting_list:
                    return False

                last = waiting_list.pop()
                diff = ord(i)-ord(last)
                if diff != 1 and diff != 2:
                    return False
        return len(waiting_list) == 0
        

            