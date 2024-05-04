/* Be Humble mf \U0001fae1 */
class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        /*solution 1 " OWN "*/
        /*char cha = letters[0];
        reverse(letters.begin(),letters.end());
        for(auto ch:letters){
            if(ch - '0' <= target - '0'){
                return cha;
            }
            cha = ch;
        }
        return cha;*/
        /* Top solution */
        int n = letters.size();
        int l=0;
        int r=n-1;
        int mid;
        int pos = -1;
        while(l<=r){
            mid=l+(r-l)/2;
            if(letters[mid]>target){
                pos=mid;
                r=mid-1;
            }
            else{
                l=mid+1;
            }
        }
        if(pos==-1)
        return letters[0];
        return letters[pos];
    
    }
};