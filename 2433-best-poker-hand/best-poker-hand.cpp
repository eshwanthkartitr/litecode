class Solution {
public:
    string bestHand(vector<int>& ranks, vector<char>& suits) {
        if(suits[0] == suits[1] && suits[2] == suits[1] && suits[3] == suits[2] && suits[4] == suits[2]) return "Flush";
        sort(ranks.begin(),ranks.end());
        unordered_map<int,int> q;
        for(auto num:ranks){
            q[num]++;
        }
        for(int i=0;i<ranks.size();i++){
            if(q[ranks[i]] >= 3){
                return "Three of a Kind";
            }
        }
        for(int i=0;i<ranks.size();i++){
            if(q[ranks[i]] ==2){
                return "Pair";
            }
        }

        return "High Card";

    }
};