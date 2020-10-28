// https://leetcode.com/problems/unique-paths/
//Optimized combinatorics solution
class Solution {
public:
    int uniquePaths(int m, int n) {
        long long x=1,y=min(m,n),z=max(m,n);
        for(int i=z;i<z+y-1;i++)
            x*=i;
        
        for(int i=2;i<y;i++)
            x/=i;
        return x;
        
    }
};
// //Optimized DP solution
// class Solution {
// public:
//     int uniquePaths(int m, int n) {
//         vector<vector<int>> grid(m, vector<int>(n));
//         grid[m - 1][0] = 1;
//         int i, j;
//         for(i = m - 1; i > -1; --i)
//         {
//             for(j = 0; j < n; ++j)
//             {
//                 if(j > 0)
//                     grid[i][j] += grid[i][j - 1];
//                 if(i < m - 1)
//                     grid[i][j] += grid[i + 1][j];
//             }
//         }
//         return grid[0][n - 1];
//     }
// };
// // DP solution
// int fun(vector<vector<int>> &dp, int i, int j, int m, int n){
//     if(i==m-1 && j==n-1)
//         return 1;
//     else if(i>=m || j>=n)
//         return 0;
//     else if(dp[i][j]==0){
//         dp[i][j]=fun(dp,i+1,j,m,n)+fun(dp,i,j+1,m,n);
//         return dp[i][j];
//     }
//     else
//         return dp[i][j];
// }
// class Solution {
// public:
//     int uniquePaths(int m, int n) {
//         vector<vector<int>> dp(m,vector<int>(n));
//         return fun(dp,0,0,m,n);
//     }
// };