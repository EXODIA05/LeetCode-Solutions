class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        a = ""
        """reverse_list = []
        pos = len(reverse_list)-1
        for i in s :
            if i in vowels:
                reverse_list.append(i)
        for i in s:
            if i in vowels:
                a = a +reverse_list[pos]
                pos-=1
            else:
                a = a + i 
        return a"""
        left = 0
        right = len(s)-1
        s_list = list(s)
        while left < right:
            while left<right and s_list[left] not in vowels:
                left+=1
            while left<right and s_list[right] not in vowels:
                right-=1
            s_list[left],s_list[right]=s_list[right],s_list[left]
            left+=1
            right-=1
        return "".join(s_list)

                    
