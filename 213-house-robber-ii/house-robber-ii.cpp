class Solution {
    int helper(vector<int> arra){
        int val_1 = 0;
        int val_2 = 0;
        for(int i=0;i<arra.size();i++){
            int temp = max(val_1+arra[i],val_2);
            val_1 = val_2;
            val_2 = temp;
        }
        return val_2;
    }
public:
    int rob(vector<int>& nums) {
        vector<int> subvec1(nums.begin() + 1, nums.end());
        vector<int> subvec2(nums.begin(), nums.end() - 1);
        int val = helper(subvec1);
        int val2 = helper(subvec2);
        int val_3  = max(val, val2);
        return max(nums[0],val_3);
    }
};