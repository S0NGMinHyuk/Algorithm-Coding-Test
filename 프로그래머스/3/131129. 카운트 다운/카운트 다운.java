class Solution {
    int TOTAL = 0;
    int SB = 1;
    
    public int[] solution(int target) {
        int[][] answer = new int[target+1][2];
        
        for (int n=1; n<=target; n++) {
            if (n <= 20 || n == 50) {   // 싱글, 불로 맞추는 경우
                answer[n][TOTAL] = 1;
                answer[n][SB] = 1;
                continue;
            }
            
            if (n <= 40 && n%2 == 0) {  // 더블로 맞추는 경우
                answer[n][TOTAL] = 1;
                answer[n][SB] = 0;
                continue;
            }
            
            if (n <= 60 && n%3 == 0) {  // 트리플로 맞추는 경우
                answer[n][TOTAL] = 1;
                answer[n][SB] = 0;
                continue;
            }
            
            for (int i=1; i<=60; i++) { // 내 앞에 60만큼 DP 검사
                if (i >= n) 
                    break;
                int[] left = answer[i];
                int[] right = answer[n-i];
                    
                // 값이 없던 경우
                if (answer[n][TOTAL] == 0) {    
                    answer[n][TOTAL] = left[TOTAL] + right[TOTAL];
                    answer[n][SB] = left[SB] + right[SB];
                } 
                // 총 다트 개수가 더 적은 경우
                else if (left[TOTAL] + right[TOTAL] < answer[n][TOTAL]) {
                    answer[n][TOTAL] = left[TOTAL] + right[TOTAL];
                    answer[n][SB] = left[SB] + right[SB];
                } 
                // 총 싱글+불 개수가 더 많은 경우
                else if (left[TOTAL] + right[TOTAL] == answer[n][TOTAL]
                          && left[SB] + right[SB] > answer[n][SB]) {
                    answer[n][TOTAL] = left[TOTAL] + right[TOTAL];
                    answer[n][SB] = left[SB] + right[SB];
                }
            }
            
            if (n > 50) {
                if (answer[n][TOTAL] == 0) {
                    answer[n][TOTAL] = answer[n-50][TOTAL] + 1;
                    answer[n][SB] = answer[n-50][SB] + 1;
                } else if (answer[n-50][TOTAL] + 1 < answer[n][TOTAL]) {
                    answer[n][TOTAL] = answer[n-50][TOTAL] + 1;
                    answer[n][SB] = answer[n-50][SB] + 1;
                } else if (answer[n-50][TOTAL] + 1 == answer[n][TOTAL]
                          && answer[n-50][SB] + 1 > answer[n][SB]) {
                    answer[n][TOTAL] = answer[n-50][TOTAL] + 1;
                    answer[n][SB] = answer[n-50][SB] + 1;
                }
            }
        }
        
        return answer[target];
    }
}