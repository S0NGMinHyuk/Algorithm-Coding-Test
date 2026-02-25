import java.io.*;
import java.util.*;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine());
    char[][] graph = new char[n][n];
    for (int i = 0; i < n; i++) {
      String input = br.readLine();
      for (int j = 0; j < n; j++) {
        graph[i][j] = input.charAt(j);
      }
    }

    int[] dx = new int[]{-1, 1, 0, 0};
    int[] dy = new int[]{0, 0, -1, 1};
    List<Integer> homes = new ArrayList<>();
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        if (graph[i][j] == '1') {
          // 새로운 집을 발견한 경우
          int size = 0;
          Queue<int[]> queue = new LinkedList<>();
          queue.offer(new int[]{i, j});
          graph[i][j] = '0';
          while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            size++;
            for (int k=0; k<4; k++) {
              int nx = curr[0] + dx[k];
              int ny = curr[1] + dy[k];
              if (nx >= 0 && ny >= 0 && nx < n && ny < n) {
                if (graph[nx][ny] == '1') {
                  queue.offer(new int[]{nx, ny});
                  graph[nx][ny] = '0';
                }
              }
            }
          }
          homes.add(size);
        }
      }
    }
    Collections.sort(homes);
    System.out.println(homes.size());
    for (int s : homes) {
      System.out.println(s);
    }
  }
}
