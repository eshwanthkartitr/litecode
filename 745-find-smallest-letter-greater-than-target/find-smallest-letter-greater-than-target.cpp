/* Be Humble */
class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        char cha = letters[0];
        reverse(letters.begin(),letters.end());
        for(auto ch:letters){
            if(ch - '0' <= target - '0'){
                return cha;
            }
            cha = ch;
        }
        return cha;
    }
};