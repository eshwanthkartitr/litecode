class Solution {
public:
    vector<string> findRelativeRanks(vector<int>& score) {
        vector<int> sortedScore = score;
        sort(sortedScore.begin(), sortedScore.end(), greater<int>());
        unordered_map<int, string> rankMapping;
        for (int i = 0; i < sortedScore.size(); i++) {
            if (i == 0) {
                rankMapping[sortedScore[i]] = "Gold Medal";
            } else if(i == 1){
                rankMapping[sortedScore[i]] = "Silver Medal";
            }else if(i==2){
                rankMapping[sortedScore[i]] = "Bronze Medal";
            }else {
                rankMapping[sortedScore[i]] = to_string(i + 1);
            }
        }
        vector<string> result;
        for (int s : score) {
            result.push_back(rankMapping[s]);
        }
        return result;
    }
};