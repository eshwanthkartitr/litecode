class Solution {
    public int[][] dp;
    public int maxCoins(int[] nums) {
        dp=new int[nums.length][nums.length];
        for(int[] row : dp)
            Arrays.fill(row,-1);
        return solve(nums,0,nums.length-1);
    }
    int solve(int[] arr,int i,int j){
        if (i>j) return 0;
        if(dp[i][j]!=-1){
            return dp[i][j];
        }
        int max=0;
        for(int k=i;k<=j;k++){
            int tmp = solve(arr,i,k-1)+solve(arr,k+1,j)+arr[k]*(i-1<0?1:arr[i-1])*(j+1>=arr.length?1:arr[j+1]);
            max = Math.max(tmp,max);
        }
        return dp[i][j]=max;
    }
}