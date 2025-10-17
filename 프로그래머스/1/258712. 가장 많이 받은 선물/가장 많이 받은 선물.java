// 배열 선언법, HashMap 선언법 체크
// dict.put(key, value) 형태로 값 주입
// dict.get(key) 형태로 값 획득

import java.util.*;

class Solution {
    public int solution(String[] friends, String[] gifts) {
        int answer = 0;
        int n = friends.length;
        HashMap<String, Integer> dict = new HashMap<>();
        int[] degree = new int[n];
        int[][] graph = new int[n][n];
        
        // 해시맵에 값 주입
        for (int i = 0; i < n; i++) {
            dict.put(friends[i], i);
        }
        
        // 선물 기록으로 지금까지 주고받은 기록과 지수 계산
        for (String gift : gifts) {
            String[] giftName = gift.split(" ");
            degree[dict.get(giftName[0])]++;
            degree[dict.get(giftName[1])]--;
            graph[dict.get(giftName[0])][dict.get(giftName[1])]++;    
        }
        
        for (int i =0; i < n; i++) {
            int num = 0;
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                if (graph[i][j] > graph[j][i]) num++;   // 내가 더 준 경우
                if (graph[i][j] == graph[j][i]          // 내가 선물지수가 더 큰 경우
                   && degree[i] > degree[j]) num++;
            }
            
            if (answer < num) answer = num;
        }
        return answer;
    }
}