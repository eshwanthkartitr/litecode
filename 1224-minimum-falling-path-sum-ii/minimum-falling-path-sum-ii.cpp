class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& grid) {
        int n =grid.size();
        int m = grid[0].size();
        int res = __INT_MAX__;
        vector<vector<int>> dp(n,vector<int>(m,-1));
        for(int j =0;j<m;j++){
            dp[0][j] = grid[0][j];
        }
        for(int i=1;i<n;i++){
            for(int j=0;j<m;j++){
                int tr = __INT_MAX__;
                for(int k=0;k<m;k++){
                    if(k!=j){
                        tr = min(tr,grid[i][j]+dp[i-1][k]);
                    }
                    dp[i][j] = tr;
                }
            }
        }
        for(int j = 0; j < m; ++j) {
            res = min(res, dp[n - 1][j]);
        }

        return res;
    }
};