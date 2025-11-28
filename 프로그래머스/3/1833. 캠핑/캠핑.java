import java.util.*;

class Solution {
    public int solution(int n, int[][] data) {
        int answer = 0;
        
        // x, y축 기준 오름차순 정렬
        Arrays.sort(data, (o1, o2) -> {
            if (o1[0] == o2[0]) return o1[1] - o2[1];
            return o1[0]-o2[0];
        });
        
        for (int i=0; i<n; i++) {
            for (int j=i+1; j<n; j++) {
                int[] a = data[i];
                int[] b = data[j];
                
                if (a[0] == b[0] || a[1] == b[1]) // 넓이가 0인 경우 스킵
                    continue;
                
                boolean buildable = true;
                for (int k=i+1; k<j; k++) {
                    int[] mid = data[k];
                    if ((a[0] < mid[0] && mid[0] < b[0]) 
                        && Math.min(a[1], b[1]) < mid[1] 
                        && Math.max(a[1], b[1]) > mid[1]) {
                        buildable = false;
                        break;
                    }
                }
                if (buildable) answer++;
            }
        }
        return answer;
    }
}