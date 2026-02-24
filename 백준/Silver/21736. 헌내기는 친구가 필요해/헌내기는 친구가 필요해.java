import java.io.*;
import java.util.*;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int N = Integer.parseInt(st.nextToken());
    int M = Integer.parseInt(st.nextToken());
    int answer = 0;

    char[][] graph = new char[N][M];
    int[][] visited = new int[N][M];
    int[] start = new int[2];

    // 캠퍼스 입력 받으며 도연이 위치 저장하기
    for (int i = 0; i < N; i++) {
      String line = br.readLine();
      for (int j = 0; j < M; j++) {
        graph[i][j] = line.charAt(j);
        if (graph[i][j] == 'I') {
          start[0] = i;
          start[1] = j;
        }
      }
    }

    // 도연이 위치부터 BFS 알고리즘으로 이동하기
    int[] dx = new int[]{0, 1, 0, -1};
    int[] dy = new int[]{1, 0, -1, 0};
    Queue<int[]> queue = new ArrayDeque<>();
    queue.add(start);
    visited[start[0]][start[1]] = 1;

    while (!queue.isEmpty()) {
      int[] curr = queue.poll();
      int x = curr[0];
      int y = curr[1];
      if (graph[x][y] == 'P') {
        // 사람 칸에 오면 answer 1 증가
        answer++;
      }
      for (int i=0; i<4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (0 <= nx && nx < N && 0 <= ny && ny < M) {
          if (graph[nx][ny] != 'X' && visited[nx][ny] == 0) {
            // 그래프를 벗어나지 않고, 벽이 아니며, 방문하지 않은 칸인 경우
            visited[nx][ny] = 1;
            queue.offer(new int[] {nx, ny});
          }
        }
      }
    }
    
    // 결과 출력. 0이면 TT 출력
    if (answer > 0) {
      System.out.println(answer);
    } else {
      System.out.println("TT");
    }
  }
}
