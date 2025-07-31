class Solution {
public:
    int subarrayBitwiseORs(vector<int>& arr) {
        set<int> uni;
        set<int> subs;
        int n =arr.size();
        for(int i=0;i<n;i++){
            int tmp = arr[i];
            set<int> ubs;
            ubs.insert(tmp);
            for(auto y:subs){
                tmp = tmp | y;
                ubs.insert(tmp);
            }

            uni.insert(ubs.begin(),ubs.end());
            subs = ubs;
        }

        return uni.size();
    }
};