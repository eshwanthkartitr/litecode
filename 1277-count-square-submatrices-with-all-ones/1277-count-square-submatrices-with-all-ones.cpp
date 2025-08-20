class Solution {
public:
    int countSquares(vector<vector<int>>& matrix) {
        int m = matrix.size(),n =matrix[0].size();
        vector<vector<int>> irruku(m,vector<int>(n,0));
        // For 2x2
        // T T
        // T T
        int tmp = 0;
        for(int i=0;i<m;i++){
            if(matrix[i][0] == 1){
                irruku[i][0] = 1;
            }
        }

        for(int i=0;i<n;i++){
            if(matrix[0][i] == 1){
                irruku[0][i] = 1;
            }
        }

        for(int i=1;i<m;i++){
            for(int j=1;j<n;j++){
                if(matrix[i][j]==1){
                    irruku[i][j] = 1+min(min(irruku[i-1][j-1],irruku[i][j-1]),irruku[i-1][j]);
                }else{
                    irruku[i][j] = 0;
                }
            }
        }

        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                tmp += irruku[i][j];
            }
        }

        return tmp;
    }
};