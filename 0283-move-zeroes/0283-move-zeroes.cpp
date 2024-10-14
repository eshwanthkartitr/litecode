class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int left=0;
        int right=1;
        while(right<nums.size()){
            if(nums[left]==0 && nums[right]!=0){
                int tmp = nums[left];
                nums[left] = nums[right];
                nums[right]=tmp;
                left++;
            }else if(nums[left]!=0){
                left++;
            }
            right++;
        }
    }
};