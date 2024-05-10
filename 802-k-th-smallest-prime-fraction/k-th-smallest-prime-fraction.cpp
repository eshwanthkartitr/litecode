class Solution {
public:
    vector<int> kthSmallestPrimeFraction(vector<int>& arr, int k) {
        vector<pair<int, vector<int>>> result;
        for (int i = 0; i < arr.size(); i++) {
            for (int j = i + 1; j < arr.size(); j++) {
                result.emplace_back(arr[i]/arr[j], vector<int>{arr[i], arr[j]});
            }
        }

        sort(result.begin(), result.end(), [](const pair<int, vector<int>>& a, const pair<int, vector<int>>& b) {
            int num1 = a.second[0];
            int den1 = a.second[1];
            int num2 = b.second[0];
            int den2 = b.second[1];
            return num1 * den2 < num2 * den1;
        });

        return result[k - 1].second;
    }
};