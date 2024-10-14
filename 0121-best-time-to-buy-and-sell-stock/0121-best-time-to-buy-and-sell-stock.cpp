class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int price=10000000000;
        int profit= 0;
        for(int i=0;i<prices.size();i++){
            price = min(price,prices[i]);
            if(prices[i] - price > profit){
                profit = prices[i]-price;
            }
        }
        return profit;
    }
};