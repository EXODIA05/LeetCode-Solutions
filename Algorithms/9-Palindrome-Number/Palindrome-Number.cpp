class Solution {
public:
bool isPalindrome(int x)
    {
        string a = to_string(x);
        int pos = a.size()-1;
        for(int i =0;i<a.size();i++)
        {
            if (a[i]!=a[pos])
            {
                return false;
            }
            pos--;
        }
        return true;}};