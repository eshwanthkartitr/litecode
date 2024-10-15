class Solution {
public:
    long long minimumSteps(string s) {
        long long ans = 0;
        long long myans=0;
        for(int i=s.size()-1;i>-1;i--){
            if(s[i]=='0'){
                ans++;
            }
            else{
                myans = myans+ans;
            }
        }
        return myans;
    }
};