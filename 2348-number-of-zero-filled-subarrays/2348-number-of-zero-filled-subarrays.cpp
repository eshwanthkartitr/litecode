class Solution {
public:
    long long zeroFilledSubarray(vector<int>& nums) {
        long long res = 0;
        int tmp = 0;
        for(auto&it:nums){
            if(it!=0){
                tmp = 0;
            }else{
                tmp++;
            }
            res += tmp;
        }

        return res;
    }
};