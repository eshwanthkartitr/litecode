class Solution {
public:
    string sortVowels(string s) {
        vector<char> vowels;
        string vowelSet = "aeiouAEIOU";
        int n = s.length();
        for(int i=0;i<n;i++){
            if(vowelSet.find(s[i]) != string::npos)
                vowels.push_back(s[i]);
        }
        
        sort(vowels.begin(), vowels.end());
        int idx = 0;
    
        for(int i=0;i<n;i++){
            if(vowelSet.find(s[i]) != string::npos)
                s[i] = vowels[idx++];
        }
        return s;


    }
};