class Solution {
public:
    int numSubmat(vector<vector<int>>& mat) {
        int m = mat.size(), n = mat[0].size(), tmp = 0;
        vector<vector<int>> dp(m,vector<int>(n,0));
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(mat[i][j] == 1){
                    dp[i][j] = (j==0 ? 1 : dp[i][j-1] + 1);
                    int mi = dp[i][j];
                    for(int k=i;k>=0 && dp[k][j]>0;k--){
                        mi = min(mi, dp[k][j]);
                        tmp += mi;
                    }
                }
            }
        }
        return tmp;
    }
};
