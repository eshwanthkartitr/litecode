class Solution {
public:
    int findMaxK(vector<int>& nums) {
        unordered_map<int, int> freq;
        int maxK = -1;

        for (int num : nums) {
            if (freq.count(num)) {
                freq[num]++;
            } else {
                if (freq.count(-num)) {
                    maxK = max(maxK, abs(num));
                }
                freq[num] = 1;
            }
        }

        return maxK;
    }
};