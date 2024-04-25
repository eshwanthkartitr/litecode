class Solution {
public:
    bool is_suits(vector<char>&suits)
    {
        return suits[0]==suits[ suits.size()-1 ];
    }
    bool three_kind(vector<int>&ranks)
    {
        for(int i=2;i<ranks.size();i++)
        {
            if(ranks[i]==ranks[i-1]&&ranks[i-1]==ranks[i-2])
                return true;
        }
        return false;
    }
    bool two_kind(vector<int>&ranks)
    {
        for(int i=1;i<ranks.size();i++)
        {
            if(ranks[i]==ranks[i-1])
                return true;
        }
        return false;
    }
    string bestHand(vector<int>& ranks, vector<char>& suits) {
        sort(ranks.begin(),ranks.end());
        sort(suits.begin(),suits.end());
        if(is_suits(suits))
        {
            return "Flush";
        }
        else if(three_kind(ranks))
        {
            return "Three of a Kind";
        }
        else if (two_kind(ranks))
        {
            return "Pair";
        }
        else
        {
            return "High Card";
        }
    }
};