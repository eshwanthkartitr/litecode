class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        int finalxor = 0;
        for (int n : nums) {
            finalxor = finalxor ^ n;
        }
        finalxor = finalxor^k;
        int count = 0;
        while(finalxor > 0){
            if(finalxor&1){
                count++;
            }
            finalxor/=2;
        }
        return count;
    }
};