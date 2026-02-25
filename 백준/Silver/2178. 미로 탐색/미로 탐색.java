import java.io.*;
import java.util.*;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int N = Integer.parseInt(st.nextToken());
    int M = Integer.parseInt(st.nextToken());
    char[][] graph = new char[N+1][M+1];
    for (int i = 1; i <= N; i++) {
      String input = br.readLine();
      for (int j = 1; j <= M; j++) {
        graph[i][j] = input.charAt(j-1);
      }
    }

    Queue<int[]> queue = new ArrayDeque<>();
    int[][] visited = new int[N+1][M+1];
    int[] dx = new int[]{0,1,0,-1};
    int[] dy = new int[]{-1,0,1,0};
    queue.add(new int[] {1, 1, 1}); // x, y, distance
    visited[1][1] = 1;
    while (!queue.isEmpty()) {
      int[] cur = queue.poll();
      int x = cur[0];
      int y = cur[1];
      int distance = cur[2];
      if (x == N && y == M) {
        System.out.println(distance);
        break;
      }

      for (int i=0; i<4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (nx >= 1 && nx <= N && ny >= 1 && ny <= M) {
          if (visited[nx][ny] == 0 && graph[nx][ny] == '1') {
            queue.add(new int[]{nx, ny, distance+1});
            visited[nx][ny] = 1;
          }
        }
      }
    }
  }
}
