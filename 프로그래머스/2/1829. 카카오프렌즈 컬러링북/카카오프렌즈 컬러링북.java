import java.util.*;

class Solution {
    static final int EMPTY = 0;
    
    public int[] solution(int m, int n, int[][] picture) {
        boolean[][] visited = new boolean[m][n];
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;
        
        int[] dx = {0, 0, 1, -1};
        int[] dy = {1, -1, 0, 0};
        Queue<int[]> q = new LinkedList<>();
        
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (picture[i][j] == EMPTY || visited[i][j]) continue;
                
                // 새로운 영역을 발견한 경우
                numberOfArea++;
                int newAreaSize = 0;
                int newAreaColor = picture[i][j];
                q.add(new int[]{i, j});
                visited[i][j] = true;
                
                while (!q.isEmpty()) {  // BFS
                    int[] curr = q.poll();
                    newAreaSize++;
                    for (int d=0; d<4; d++) {   // 상하좌우 블록 탐색
                        int nx = curr[0]+dx[d];
                        int ny = curr[1]+dy[d];
                        if (nx<0 || nx==m || ny<0 || ny==n)
                            continue;
                        if (picture[nx][ny] != newAreaColor || visited[nx][ny])
                            continue;
                        visited[nx][ny] = true;
                        q.add(new int[]{nx, ny});
                    }
                }
                if (newAreaSize > maxSizeOfOneArea) // 영역 최대크기 갱신
                    maxSizeOfOneArea = newAreaSize;
            }
        }    
        
        
        return new int[]{numberOfArea, maxSizeOfOneArea};
    }
}