import java.util.*;

class Solution {
    int MOD = 20170805;
    int LEFT = 0;
    int DOWN = 1;
    
    public int solution(int m, int n, int[][] cityMap) {
        int answer = 0;
        int[][][] table = new int[m][n][2];
        
        for (int i=0; i<m; i++) {
            if (cityMap[i][0] != 1)
                table[i][0][DOWN] = 1;
            else
                break;
        }
        for (int i=0; i<n; i++) {
            if (cityMap[0][i] != 1)
                table[0][i][LEFT] = 1;
            else
                break;
        }
        
        for (int i=1; i<m; i++) {
            for (int j=1; j<n; j++) {
                if (cityMap[i][j-1] == 0)
                    table[i][j][LEFT] = table[i][j-1][LEFT] + table[i][j-1][DOWN];
                else if (cityMap[i][j-1] == 2)
                    table[i][j][LEFT] = table[i][j-1][LEFT];
                table[i][j][LEFT] %= MOD;
                
                if (cityMap[i-1][j] == 0)
                    table[i][j][DOWN] = table[i-1][j][LEFT] + table[i-1][j][DOWN];
                else if (cityMap[i-1][j] == 2)
                    table[i][j][DOWN] = table[i-1][j][DOWN];
                table[i][j][DOWN] %= MOD;
            }
        }
        return (table[m-1][n-1][LEFT] + table[m-1][n-1][DOWN]) % MOD;
    }
}