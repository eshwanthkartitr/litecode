class Solution {
private:
    bool zero_checker(const vector<int>& example) {
        return find(example.begin(), example.end(), 0) == example.end();
    }

public:
    long long maximumHappinessSum(vector<int>& happiness, int k) {
        long long answer = 0;
        sort(happiness.begin(),happiness.end());
        for(int i=0;i<k;i++){
            answer += max(0,happiness[happiness.size()-1]-i);
            happiness.pop_back();
        }
        return answer;
    }
};