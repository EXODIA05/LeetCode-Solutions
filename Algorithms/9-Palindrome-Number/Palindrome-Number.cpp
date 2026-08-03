class Solution {
public:
    bool isPalindrome(int x) {
        long long rev = 0;
        int original = x;
        while (x > 0) {
            rev = rev * 10 + x % 10;
            x = x / 10;
        }
        if (rev != original) {
            return false;
        }
        return true;
    }
};