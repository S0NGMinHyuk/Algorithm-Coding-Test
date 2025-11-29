// DFS를 사용하되 무지성 트리 순환이 아니다.
// visited 배열을 탐색하며 현재 갈 수 있는 노드인지 아닌지 모든 edges에 대해 탐색

import java.util.*;

class Solution {
    final int SHEEP = 0;
    final int WOLF = 1;
    
    int answer = 0;
    boolean[] visited;
    int[] info;
    int[][] edges;
    
    public int solution(int[] L_info, int[][] L_edges) {
        info = L_info;
        edges = L_edges;
        
        visited = new boolean[info.length];
        visited[0] = true;
        dfs(1, 0);
        return answer;
    }
    
    public void dfs(int sheeps, int wolves) {
        if (sheeps > wolves) {
            answer = Math.max(answer, sheeps);
        } else if (sheeps == wolves) {
            return;
        }
        
        for (int[] e : edges) {
            int parent = e[0], child = e[1];
            if (visited[parent] && !visited[child]) {
                visited[child] = true;
                if (info[child] == SHEEP) dfs(sheeps+1, wolves);
                if (info[child] ==  WOLF) dfs(sheeps, wolves+1);
                visited[child] = false;
            }
        }
    }
}