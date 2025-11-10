import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int answer = 0;
        int[] dx = {0, 0, 1, -1};
        int[] dy = {1, -1, 0, 0};
        boolean[][] visited = new boolean[maps.length][maps[0].length];
        Queue<int[]> q = new ArrayDeque<>();

        q.add(new int[] {0, 0, 1});
        visited[0][0] = true;
        
        int[] me;
        while (!q.isEmpty()) {
            me = q.poll();
            if (me[0] == maps.length-1 && me[1] == maps[0].length-1)
                return me[2];
            
            for (int i=0; i<4; i++) {
                int nx = me[0] + dx[i];
                int ny = me[1] + dy[i];
                if (nx >= 0 && nx < maps.length && 
                    ny >= 0 && ny < maps[0].length &&
                    !visited[nx][ny] && maps[nx][ny] == 1) {
                    visited[nx][ny] = true;
                    q.add(new int[]{nx, ny, me[2]+1});
                }
            }
        }
        
        return -1;
    }
}