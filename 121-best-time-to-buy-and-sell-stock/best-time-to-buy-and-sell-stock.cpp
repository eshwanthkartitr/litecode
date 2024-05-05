class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxprofit  = 0;
        int number = __INT_MAX__;
        for(int i=0;i<prices.size();i++){
            number = min(number,prices[i]);
            maxprofit = max(maxprofit,prices[i]-number);
        }
        
        return maxprofit;
    }
};