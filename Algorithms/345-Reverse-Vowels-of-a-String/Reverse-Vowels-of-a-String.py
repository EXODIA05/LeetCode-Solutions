class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        reverse_list = []
        a=""
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
        return a