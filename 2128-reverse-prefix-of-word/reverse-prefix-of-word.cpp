class Solution {
public:
    string reversePrefix(string word, char ch) {
        string result = "";
        size_t ch_idx = word.find(ch);
        if(ch_idx == 18446744073709551615){
            return word;
        }
        for(int i=0;i<word.size();i++){
            if(i<=ch_idx){
                result = word[i] + result; 
            }
            else{
                result = result + word[i];
            }
        }
        return result;
    }
};