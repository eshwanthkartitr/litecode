class Solution {
public:
    int lengthOfLastWord(string s) {
        int p1=0;
        bool counting = false;
        for(int i=s.size()-1;i>=0;i--){
            if(s[i] != ' '){
                counting = true;
                p1++;
            }
            else if(counting){
                break;
            }
        }

        return p1;
    }
};