class Solution {
public:
    int firstUniqChar(string s)
    {
        unordered_map<char,int> hash_map;
        for(char c:s)
        {
            hash_map[c]++;
        }
        for (char c:s)
        {
            if (hash_map[c]==1)
            {
                return s.find(c);
            }
        }
        return -1;
    }
};