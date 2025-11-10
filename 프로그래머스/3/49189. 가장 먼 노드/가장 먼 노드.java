import java.util.*;

class Solution {
    public int solution(int n, int[][] edge) {
        boolean[] visited = new boolean[n+1];
        Queue<int[]> q = new ArrayDeque<>();
        HashSet<Integer>[] graph = getGraph(n, edge);
        int answer = 0;
        int maxDistance = 0;
        
        q.add(new int[]{1, 0});
        visited[1] = true;
        
        while(!q.isEmpty()) {
            int[] curr = q.poll();
            int node = curr[0];
            int dist = curr[1];
            if (dist == maxDistance) {
                answer++;
            } else if (dist > maxDistance) {
                maxDistance = dist;
                answer = 1;
            }
            
            for (int child=1; child<=n; child++) {
                if (graph[node].contains(child) && !visited[child]) {
                    visited[child] = true;
                    q.add(new int[]{child, dist+1});
                }
            }
        }
        return answer;
    }
    
    public HashSet<Integer>[] getGraph(int n, int[][] edge) {
        HashSet<Integer>[] g = new HashSet[n+1];
        for (int i = 1; i <= n; i++) 
            g[i] = new HashSet<>();
        
        for (int[] e : edge) {
            int a = e[0]; 
            int b = e[1];
            g[a].add(b);
            g[b].add(a);
        }
        
        return g;
    }
}