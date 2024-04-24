class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> re;
        for(int i=0;i<nums.size();i++){
            int comp = target - nums[i];
            if (re.find(comp) != re.end()){
                return {re[comp],i};
            }else{
                re[nums[i]] = i;
            }
        }
        return {};
    }
};