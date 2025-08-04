class Solution {
public:
    int totalFruit(vector<int>& nums) {
        int max_val = 0;
        int left = 0;
        int n = nums.size();
        unordered_map<int,int> umap;
        for(int right = 0;right < n;right++){
            umap[nums[right]]++;

            while(umap.size() >2){
                umap[nums[left]]--;
                if(umap[nums[left]] == 0){
                    umap.erase(nums[left]);
                }
                left++;
            }
            max_val = max(max_val,right-left+1);
        }

        return max_val;
    }
};